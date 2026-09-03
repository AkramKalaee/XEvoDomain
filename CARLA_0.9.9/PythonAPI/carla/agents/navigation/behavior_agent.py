# Copyright (c) # Copyright (c) 2018-2020 CVC.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

""" This module implements an agent that roams around a track following random
waypoints and avoiding other vehicles. The agent also responds to traffic lights,
traffic signs, and has different possible configurations. """

import random
import numpy as np
import carla
from instrumentation import evaluate_condition
from agents.navigation.agent import Agent
from agents.navigation.local_planner_behavior import LocalPlanner, RoadOption
from agents.navigation.global_route_planner import GlobalRoutePlanner
from agents.navigation.global_route_planner_dao import GlobalRoutePlannerDAO
from agents.navigation.types_behavior import Cautious, Aggressive, Normal

from agents.tools.misc import get_speed, positive


class BehaviorAgent(Agent):
    """
    BehaviorAgent implements an agent that navigates scenes to reach a given
    target destination, by computing the shortest possible path to it.
    This agent can correctly follow traffic signs, speed limitations,
    traffic lights, while also taking into account nearby vehicles. Lane changing
    decisions can be taken by analyzing the surrounding environment,
    such as overtaking or tailgating avoidance. Adding to these are possible
    behaviors, the agent can also keep safety distance from a car in front of it
    by tracking the instantaneous time to collision and keeping it in a certain range.
    Finally, different sets of behaviors are encoded in the agent, from cautious
    to a more aggressive ones.
    """

    def __init__(self, vehicle, ignore_traffic_light=False, behavior='normal'):
        """
        Constructor method.

            :param vehicle: actor to apply to local planner logic onto
            :param ignore_traffic_light: boolean to ignore any traffic light
            :param behavior: type of agent to apply
        """

        super(BehaviorAgent, self).__init__(vehicle)
        self.vehicle = vehicle
        self.ignore_traffic_light = ignore_traffic_light
        self._local_planner = LocalPlanner(self)
        self._grp = None
        self.look_ahead_steps = 0

        # Vehicle information
        self.speed = 0
        self.speed_limit = 0
        self.direction = None
        self.incoming_direction = None
        self.incoming_waypoint = None
        self.start_waypoint = None
        self.end_waypoint = None
        self.is_at_traffic_light = 0
        self.light_state = "Green"
        self.light_id_to_ignore = -1
        self.min_speed = 5
        self.behavior = None
        self._sampling_resolution = 4.5

        # Parameters for agent behavior
        if evaluate_condition('behavior_agent.py', 1, 'Eq', behavior,
            'cautious', 0, ['#']):
            self.behavior = Cautious()

        elif evaluate_condition('behavior_agent.py', 2, 'Eq', behavior,
            'normal', 0, ['#']):
            self.behavior = Normal()

        elif evaluate_condition('behavior_agent.py', 3, 'Eq', behavior,
            'aggressive', 0, ['#']):
            self.behavior = Aggressive()

    def update_information(self, world):
        """
        This method updates the information regarding the ego
        vehicle based on the surrounding world.

            :param world: carla.world object
        """
        self.speed = get_speed(self.vehicle)
        self.speed_limit = world.player.get_speed_limit()
        self._local_planner.set_speed(self.speed_limit)
        self.direction = self._local_planner.target_road_option
        if evaluate_condition('behavior_agent.py', 4, 'Is', self.direction, None, 0, ['#']):
            self.direction = RoadOption.LANEFOLLOW
        self.look_ahead_steps = int((self.speed_limit) / 10)
        self.incoming_waypoint, self.incoming_direction = (self._local_planner.
            get_incoming_waypoint_and_direction(steps=self.look_ahead_steps))
        if evaluate_condition('behavior_agent.py', 5, 'Is', self.
            incoming_direction, None, 0, ['#']):
            self.incoming_direction = RoadOption.LANEFOLLOW
        self.is_at_traffic_light = world.player.is_at_traffic_light()
        if evaluate_condition('behavior_agent.py', 6, 'Pb', self.ignore_traffic_light, None, 0, ['#']):
            self.light_state = 'Green'
        else:
            self.light_state = str(self.vehicle.get_traffic_light_state())


    def set_destination(self, start_location, end_location, clean=False):
        """
        This method creates a list of waypoints from agent's position to destination location
        based on the route returned by the global router.

            :param start_location: initial position
            :param end_location: final position
            :param clean: boolean to clean the waypoint queue
        """
        if evaluate_condition('behavior_agent.py', 7, 'Pb', clean, None, 0, ['#']):
            self._local_planner.waypoints_queue.clear()
        self.start_waypoint = self._map.get_waypoint(start_location)
        self.end_waypoint = self._map.get_waypoint(end_location)
        route_trace = self._trace_route(self.start_waypoint, self.end_waypoint)
        self._local_planner.set_global_plan(route_trace)


    def reroute(self, spawn_points):
        """
        This method implements re-routing for vehicles approaching its destination.
        It finds a new target and computes another path to reach it.

            :param spawn_points: list of possible destinations for the agent
        """
        print('Target almost reached, setting new destination...')
        random.shuffle(spawn_points)
        new_start = self._local_planner.waypoints_queue[-1][0].transform.location
        destination = spawn_points[0].location if evaluate_condition(
            'behavior_agent.py', 8, 'NotEq', spawn_points[0].location, new_start, 0, ['#']
            ) else spawn_points[1].location
        print('New destination: ' + str(destination))
        self.set_destination(new_start, destination)


    def _trace_route(self, start_waypoint, end_waypoint):
        """
        This method sets up a global router and returns the
        optimal route from start_waypoint to end_waypoint.

            :param start_waypoint: initial position
            :param end_waypoint: final position
        """
        if evaluate_condition('behavior_agent.py', 9, 'Is', self._grp, None, 0, ['#']):
            wld = self.vehicle.get_world()
            dao = GlobalRoutePlannerDAO(wld.get_map(), sampling_resolution=self
                ._sampling_resolution)
            grp = GlobalRoutePlanner(dao)
            grp.setup()
            self._grp = grp
        route = self._grp.trace_route(start_waypoint.transform.location,
            end_waypoint.transform.location)
        return route


    def traffic_light_manager(self, waypoint):
        """
        This method is in charge of behaviors for red lights and stops.

        WARNING: What follows is a proxy to avoid having a car brake after running a yellow light.
        This happens because the car is still under the influence of the semaphore,
        even after passing it. So, the semaphore id is temporarely saved to
        ignore it and go around this issue, until the car is near a new one.

            :param waypoint: current waypoint of the agent
        """
        light_id = self.vehicle.get_traffic_light().id if evaluate_condition(
            'behavior_agent.py', 10, 'IsNot', self.vehicle.get_traffic_light(), None
            , 0, ['#']) else -1
        if evaluate_condition('behavior_agent.py', 11, 'Eq', self.light_state,
            'Red', 0, ['#']):
            if evaluate_condition('behavior_agent.py', 12, 'Nb', not waypoint.is_junction, None, 0, ['#', 'and, 13, 14']) and\
                (evaluate_condition('behavior_agent.py', 13, 'NotEq', self.light_id_to_ignore, light_id, 0, ['#', 'or, 14']) or
                 evaluate_condition('behavior_agent.py', 14, 'Eq', light_id, -1, 0, ['#'])):
                return 1
            elif evaluate_condition('behavior_agent.py', 15, 'Pb', not waypoint.is_junction, None, 0, ['#', 'and,16']) and evaluate_condition('behavior_agent.py',
                16, 'NotEq', light_id, -1, 0, ['#']):
                self.light_id_to_ignore = light_id
        if evaluate_condition('behavior_agent.py', 17, 'NotEq', self.
            light_id_to_ignore, light_id, 0, ['#']):
            self.light_id_to_ignore = -1
        return 0


    def _overtake(self, location, waypoint, vehicle_list):
        """
        This method is in charge of overtaking behaviors.

            :param location: current location of the agent
            :param waypoint: current waypoint of the agent
            :param vehicle_list: list of all the nearby vehicles
        """
        left_turn = waypoint.left_lane_marking.lane_change
        right_turn = waypoint.right_lane_marking.lane_change
        left_wpt = waypoint.get_left_lane()
        right_wpt = waypoint.get_right_lane()
        if (evaluate_condition('behavior_agent.py', 18, 'Eq', left_turn, carla.
            LaneChange.Left, 0, ['or,19', 'and, 20']) or evaluate_condition('behavior_agent.py', 19,
            'Eq', left_turn, carla.LaneChange.Both), 0, ['#', 'and, 20']) and evaluate_condition(
            'behavior_agent.py', 20, 'Gt', waypoint.lane_id * left_wpt.lane_id, 0, 0, ['#', 'and,21']
            ) and evaluate_condition('behavior_agent.py', 21, 'Eq', left_wpt.
            lane_type, carla.LaneType.Driving, 0, ['#']):
            new_vehicle_state, _, _ = self._bh_is_vehicle_hazard(waypoint,
                location, vehicle_list, max(self.behavior.
                min_proximity_threshold, self.speed_limit / 3), up_angle_th=180,
                lane_offset=-1)
            if evaluate_condition('behavior_agent.py', 22, 'Nb', not new_vehicle_state, None, 0, ['#']):
                print('Overtaking to the left!')
                self.behavior.overtake_counter = 200
                self.set_destination(left_wpt.transform.location, self.
                    end_waypoint.transform.location, clean=True)
        elif evaluate_condition('behavior_agent.py', 23, 'Eq', right_turn,
            carla.LaneChange.Right, 0, ['#', 'and,24']) and evaluate_condition('behavior_agent.py',
            24, 'Gt', waypoint.lane_id * right_wpt.lane_id, 0, 0, ['#', 'and,25']
            ) and evaluate_condition('behavior_agent.py', 25, 'Eq', right_wpt.
            lane_type, carla.LaneType.Driving, 0, ['#']):
            new_vehicle_state, _, _ = self._bh_is_vehicle_hazard(waypoint,
                location, vehicle_list, max(self.behavior.
                min_proximity_threshold, self.speed_limit / 3), up_angle_th=180,
                lane_offset=1)
            if evaluate_condition('behavior_agent.py', 26, 'Nb', not new_vehicle_state, None, 0, ['#']):
                print('Overtaking to the right!')
                self.behavior.overtake_counter = 200
                self.set_destination(right_wpt.transform.location, self.
                    end_waypoint.transform.location, clean=True)


    def _tailgating(self, location, waypoint, vehicle_list):
        """
        This method is in charge of tailgating behaviors.

            :param location: current location of the agent
            :param waypoint: current waypoint of the agent
            :param vehicle_list: list of all the nearby vehicles
        """
        left_turn = waypoint.left_lane_marking.lane_change
        right_turn = waypoint.right_lane_marking.lane_change
        left_wpt = waypoint.get_left_lane()
        right_wpt = waypoint.get_right_lane()
        behind_vehicle_state, behind_vehicle, _ = self._bh_is_vehicle_hazard(
            waypoint, location, vehicle_list, max(self.behavior.
            min_proximity_threshold, self.speed_limit / 2), up_angle_th=180,
            low_angle_th=160)
        if evaluate_condition('behavior_agent.py', 27, 'Pb', behind_vehicle_state, None, 0, ['#', 'and,28'])  and evaluate_condition('behavior_agent.py', 28,
            'Lt', self.speed, get_speed(behind_vehicle), 0, ['#']):
            if (evaluate_condition('behavior_agent.py', 29, 'Eq', right_turn,
                carla.LaneChange.Right, 0, ['or,30', 'and,31']) or evaluate_condition(
                'behavior_agent.py', 30, 'Eq', right_turn, carla.LaneChange.Both), 0, ['#', 'and,31']
                ) and evaluate_condition('behavior_agent.py', 31, 'Gt',
                waypoint.lane_id * right_wpt.lane_id, 0, 0, ['#', 'and,32']) and evaluate_condition(
                'behavior_agent.py', 32, 'Eq', right_wpt.lane_type, carla.
                LaneType.Driving, 0, ['#']):
                new_vehicle_state, _, _ = self._bh_is_vehicle_hazard(waypoint,
                    location, vehicle_list, max(self.behavior.
                    min_proximity_threshold, self.speed_limit / 2), up_angle_th
                    =180, lane_offset=1)
                if evaluate_condition('behavior_agent.py', 33, 'Nb', not new_vehicle_state, None, 0, ['#']):
                    print('Tailgating, moving to the right!')
                    self.behavior.tailgate_counter = 200
                    self.set_destination(right_wpt.transform.location, self.
                        end_waypoint.transform.location, clean=True)
            elif evaluate_condition('behavior_agent.py', 34, 'Eq', left_turn,
                carla.LaneChange.Left, 0, ['#', 'and,35']) and evaluate_condition('behavior_agent.py',
                35, 'Gt', waypoint.lane_id * left_wpt.lane_id, 0
                , 0, ['#', 'and,36']) and evaluate_condition('behavior_agent.py', 36, 'Eq',
                left_wpt.lane_type, carla.LaneType.Driving, 0, ['#']):
                new_vehicle_state, _, _ = self._bh_is_vehicle_hazard(waypoint,
                    location, vehicle_list, max(self.behavior.
                    min_proximity_threshold, self.speed_limit / 2), up_angle_th
                    =180, lane_offset=-1)
                if evaluate_condition('behavior_agent.py', 37, 'Nb', not new_vehicle_state, None, 0, ['#']):
                    print('Tailgating, moving to the left!')
                    self.behavior.tailgate_counter = 200
                    self.set_destination(left_wpt.transform.location, self.
                        end_waypoint.transform.location, clean=True)


    def collision_and_car_avoid_manager(self, location, waypoint):
        """
        This module is in charge of warning in case of a collision
        and managing possible overtaking or tailgating chances.

            :param location: current location of the agent
            :param waypoint: current waypoint of the agent
            :return vehicle_state: True if there is a vehicle nearby, False if not
            :return vehicle: nearby vehicle
            :return distance: distance to nearby vehicle
        """
        vehicle_list = self._world.get_actors().filter('*vehicle*')

        def dist(v):
            return v.get_location().distance(waypoint.transform.location)

        n = len(vehicle_list)
        i = 0
        _vehicle_list = []
        while evaluate_condition('behavior_agent.py', 38, 'In', i, range(n), 1, ['#']):
            v = vehicle_list[i]
            i += 1
            if evaluate_condition('behavior_agent.py', 39, 'Lt', dist(v), 45, 1, ['#', 'and,40']) and \
               evaluate_condition('behavior_agent.py', 40, 'NotEq', v.id, self.vehicle.id, 1, ['#']):
                    _vehicle_list.append(v)
        vehicle_list = _vehicle_list

        # vehicle_list = [v for v in vehicle_list if evaluate_condition(
        #     'behavior_agent.py', 38, 'Lt', dist(v), 45, 1, ['#', 'and,39']) and evaluate_condition(
        #     'behavior_agent.py', 39, 'NotEq', v.id, self.vehicle.id, 1, ['#'])]
        if evaluate_condition('behavior_agent.py', 41, 'Eq', self.direction,
            RoadOption.CHANGELANELEFT, 0, ['#']):
            vehicle_state, vehicle, distance = self._bh_is_vehicle_hazard(waypoint,
                location, vehicle_list, max(self.behavior.
                min_proximity_threshold, self.speed_limit / 2), up_angle_th=180,
                lane_offset=-1)
        elif evaluate_condition('behavior_agent.py', 42, 'Eq', self.direction,
            RoadOption.CHANGELANERIGHT, 0, ['#']):
            vehicle_state, vehicle, distance = self._bh_is_vehicle_hazard(waypoint,
                location, vehicle_list, max(self.behavior.
                min_proximity_threshold, self.speed_limit / 2), up_angle_th=180,
                lane_offset=1)
        else:
            vehicle_state, vehicle, distance = self._bh_is_vehicle_hazard(waypoint,
                location, vehicle_list, max(self.behavior.
                min_proximity_threshold, self.speed_limit / 3), up_angle_th=30)
            if evaluate_condition('behavior_agent.py', 43, 'Pb', vehicle_state, None, 0, ['#', 'and,44']) and evaluate_condition('behavior_agent.py', 44,
                'Eq', self.direction, RoadOption.LANEFOLLOW
                , 0, ['#', 'and,45']) and evaluate_condition('behavior_agent.py', 45, 'Nb', not waypoint.is_junction, None, 0, ['#', 'and,46']) and evaluate_condition(
                'behavior_agent.py', 46, 'Gt', self.speed, 10
                , 0, ['#', 'and,47']) and evaluate_condition('behavior_agent.py', 47, 'Eq', self.
                behavior.overtake_counter, 0, 0, ['#', 'and,48']) and evaluate_condition(
                'behavior_agent.py', 48, 'Gt', self.speed, get_speed(vehicle), 0, ['#']):
                self._overtake(location, waypoint, vehicle_list)
            elif evaluate_condition('behavior_agent.py', 49, 'Nb', not vehicle_state, None, 0, ['#', 'and,50']) and evaluate_condition('behavior_agent.py',
                50, 'Eq', self.direction, RoadOption.LANEFOLLOW
                , 0, ['#', 'and,51']) and evaluate_condition('behavior_agent.py', 51, 'Nb', not waypoint.is_junction, None, 0, ['#', 'and,52'])  and evaluate_condition(
                'behavior_agent.py', 52, 'Gt', self.speed, 10
                , 0, ['#', 'and,53']) and evaluate_condition('behavior_agent.py', 53, 'Eq', self.
                behavior.tailgate_counter, 0, 0, ['#']):
                self._tailgating(location, waypoint, vehicle_list)
        return vehicle_state, vehicle, distance


    def pedestrian_avoid_manager(self, location, waypoint):
        """
        This module is in charge of warning in case of a collision
        with any pedestrian.

            :param location: current location of the agent
            :param waypoint: current waypoint of the agent
            :return vehicle_state: True if there is a walker nearby, False if not
            :return vehicle: nearby walker
            :return distance: distance to nearby walker
        """
        walker_list = self._world.get_actors().filter('*walker.pedestrian*')

        def dist(w):
            return w.get_location().distance(waypoint.transform.location)

        n = len(walker_list)
        i = 0
        _walker_list = []
        while evaluate_condition('behavior_agent.py', 54, 'In', i, range(n), 2, ['#']):
            w = walker_list[i]
            i += 1
            if evaluate_condition(
                    'behavior_agent.py', 55, 'Lt', dist(w), 10, 2, ['#']):
                _walker_list.append(w)
        walker_list = _walker_list
        # walker_list = [w for w in walker_list if evaluate_condition(
        #     'behavior_agent.py', 54, 'Lt', dist(w), 10, 2, ['#'])]
        if evaluate_condition('behavior_agent.py', 56, 'Eq', self.direction,
            RoadOption.CHANGELANELEFT, 0, ['#']):
            walker_state, walker, distance = self._bh_is_vehicle_hazard(waypoint,
                location, walker_list, max(self.behavior.
                min_proximity_threshold, self.speed_limit / 2), up_angle_th=90,
                lane_offset=-1)
        elif evaluate_condition('behavior_agent.py', 57, 'Eq', self.direction,
            RoadOption.CHANGELANERIGHT, 0, ['#']):
            walker_state, walker, distance = self._bh_is_vehicle_hazard(waypoint,
                location, walker_list, max(self.behavior.
                min_proximity_threshold, self.speed_limit / 2), up_angle_th=90,
                lane_offset=1)
        else:
            walker_state, walker, distance = self._bh_is_vehicle_hazard(waypoint,
                location, walker_list, max(self.behavior.
                min_proximity_threshold, self.speed_limit / 3), up_angle_th=60)
        return walker_state, walker, distance


    def car_following_manager(self, vehicle, distance, debug=True):
        """
        Module in charge of car-following behaviors when there's
        someone in front of us.

            :param vehicle: car to follow
            :param distance: distance from vehicle
            :param debug: boolean for debugging
            :return control: carla.VehicleControl
        """
        vehicle_speed = get_speed(vehicle)
        delta_v = max(1, (self.speed - vehicle_speed) / 3.6)
        ttc = distance / delta_v if evaluate_condition('behavior_agent.py', 58,
            'NotEq', delta_v, 0, 0, ['#']) else distance / np.nextafter(0.0, 1.0)
        if evaluate_condition('behavior_agent.py', 59, 'Gt', self.behavior.
            safety_time, ttc, 0, ['#','and, 60']) and evaluate_condition('behavior_agent.py', 60, 'Gt', ttc, 0,  0, ['#']):
            control = self._local_planner.run_step(target_speed=min(positive(
                vehicle_speed - self.behavior.speed_decrease), min(self.
                behavior.max_speed, self.speed_limit - self.behavior.
                speed_lim_dist)), debug=debug)
        elif evaluate_condition('behavior_agent.py', 61, 'Gt', 2 * self.
            behavior.safety_time, ttc, 0, ['#']):
            control = self._local_planner.run_step(target_speed=min(max(self.
                min_speed, vehicle_speed), min(self.behavior.max_speed, self.
                speed_limit - self.behavior.speed_lim_dist)), debug=debug)
        else:
            control = self._local_planner.run_step(target_speed=min(self.
                behavior.max_speed, self.speed_limit - self.behavior.
                speed_lim_dist), debug=debug)
        return control


    def run_step(self, debug=True):
        """
        Execute one step of navigation.

            :param debug: boolean for debugging
            :return control: carla.VehicleControl
        """
        control = None
        if evaluate_condition('behavior_agent.py', 62, 'Gt', self.behavior.
            tailgate_counter, 0, 0, ['#']):
            self.behavior.tailgate_counter -= 1
        if evaluate_condition('behavior_agent.py', 63, 'Gt', self.behavior.
            overtake_counter, 0, 0, ['#']):
            self.behavior.overtake_counter -= 1
        ego_vehicle_loc = self.vehicle.get_location()
        ego_vehicle_wp = self._map.get_waypoint(ego_vehicle_loc)
        if evaluate_condition('behavior_agent.py', 64, 'NotEq', self.
            traffic_light_manager(ego_vehicle_wp), 0, 0, ['#']):
            return self.emergency_stop()
        walker_state, walker, w_distance = self.pedestrian_avoid_manager(
            ego_vehicle_loc, ego_vehicle_wp)
        if evaluate_condition('behavior_agent.py', 65, 'Pb', walker_state, None, 0, ['#']):
            distance = w_distance - max(walker.bounding_box.extent.y, walker.
                bounding_box.extent.x) - max(self.vehicle.bounding_box.extent.y,
                self.vehicle.bounding_box.extent.x)
            if evaluate_condition('behavior_agent.py', 66, 'Lt', distance, self
                .behavior.braking_distance, 0, ['#']):
                return self.emergency_stop()
        vehicle_state, vehicle, distance = self.collision_and_car_avoid_manager(
            ego_vehicle_loc, ego_vehicle_wp)
        if evaluate_condition('behavior_agent.py', 67, 'Pb', vehicle_state, None, 0, ['#']):
            distance = distance - max(vehicle.bounding_box.extent.y, vehicle.
                bounding_box.extent.x) - max(self.vehicle.bounding_box.extent.y,
                self.vehicle.bounding_box.extent.x)
            if evaluate_condition('behavior_agent.py', 68, 'Lt', distance, self
                .behavior.braking_distance, 0, ['#']):
                return self.emergency_stop()
            else:
                control = self.car_following_manager(vehicle, distance)
        elif evaluate_condition('behavior_agent.py', 69, 'IsNot', self.
            incoming_waypoint, None, 0, ['#', 'and,70']) and evaluate_condition('behavior_agent.py', 70, 'Pb',  self.incoming_waypoint.is_junction, None, 0, ['#', 'and,71, 72']) and (
            evaluate_condition('behavior_agent.py', 71, 'Eq', self.
            incoming_direction, RoadOption.LEFT, 0, ['#', 'or, 72']) or evaluate_condition(
            'behavior_agent.py', 72, 'Eq', self.incoming_direction, RoadOption.
            RIGHT, 0, ['#'])):
            control = self._local_planner.run_step(target_speed=min(self.
                behavior.max_speed, self.speed_limit - 5), debug=debug)
        else:
            control = self._local_planner.run_step(target_speed=min(self.
                behavior.max_speed, self.speed_limit - self.behavior.
                speed_lim_dist), debug=debug)
        return control

