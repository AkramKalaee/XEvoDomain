# Copyright (c) # Copyright (c) 2018-2020 CVC.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

""" This module implements an agent that roams around a track following random
waypoints and avoiding other vehicles.
The agent also responds to traffic lights. """

import sys
import math

from enum import Enum

import carla
from agents.tools.misc import is_within_distance_ahead, is_within_distance, compute_distance
from instrumentation import evaluate_condition

class AgentState(Enum):
    """
    AGENT_STATE represents the possible states of a roaming agent
    """
    NAVIGATING = 1
    BLOCKED_BY_VEHICLE = 2
    BLOCKED_RED_LIGHT = 3


class Agent(object):
    """Base class to define agents in CARLA"""
    def __init__(self, vehicle):
        """
        Constructor method.

            :param vehicle: actor to apply to local planner logic onto
        """
        self._vehicle = vehicle
        self._proximity_tlight_threshold = 5.0
        self._proximity_vehicle_threshold = 10.0
        self._local_planner = None
        self._world = self._vehicle.get_world()
        try:
            self._map = self._world.get_map()
        except RuntimeError as error:
            print('RuntimeError: {}'.format(error))
            print('  The server could not send the OpenDRIVE (.xodr) file:')
            print(
                '  Make sure it exists, has the same name of your town, and is correct.'
                )
            sys.exit(1)
        self._last_traffic_light = None


    def get_local_planner(self):
        """Get method for protected member local planner"""
        return self._local_planner

    @staticmethod
    def run_step(debug=False):
        """
        Execute one step of navigation.

            :param debug: boolean flag for debugging
            :return: control
        """
        control = carla.VehicleControl()
        if evaluate_condition('agent.py', 1, 'Pb', debug, None, 0, ['#']):
            control.steer = 0.0
            control.throttle = 0.0
            control.brake = 0.0
            control.hand_brake = False
            control.manual_gear_shift = False
        return control


    def _is_light_red(self, lights_list):
        """
        Method to check if there is a red light affecting us. This version of
        the method is compatible with both European and US style traffic lights.

        :param lights_list: list containing TrafficLight objects
        :return: a tuple given by (bool_flag, traffic_light), where
                 - bool_flag is True if there is a traffic light in RED
                   affecting us and False otherwise
                 - traffic_light is the object itself or None if there is no
                   red traffic light affecting us
        """
        ego_vehicle_location = self._vehicle.get_location()
        ego_vehicle_waypoint = self._map.get_waypoint(ego_vehicle_location)
        n = len(lights_list)
        i = 0
        while evaluate_condition('agent.py', 2, 'In', i, range(n), 1, ['#']):
            traffic_light = lights_list[i]
            i += 1
            object_location = self._get_trafficlight_trigger_location(traffic_light
                )
            object_waypoint = self._map.get_waypoint(object_location)
            if evaluate_condition('agent.py', 3, 'NotEq', object_waypoint.
                road_id, ego_vehicle_waypoint.road_id, 1, ['#']):
                continue
            ve_dir = ego_vehicle_waypoint.transform.get_forward_vector()
            wp_dir = object_waypoint.transform.get_forward_vector()
            dot_ve_wp = ve_dir.x * wp_dir.x + ve_dir.y * wp_dir.y + ve_dir.z * wp_dir.z
            if evaluate_condition('agent.py', 4, 'Lt', dot_ve_wp, 0, 1, ['#']):
                continue
            if evaluate_condition('agent.py', 5, 'Pb', is_within_distance_ahead(object_waypoint.transform, self.
                _vehicle.get_transform(), self._proximity_tlight_threshold), None, 1, ['#']):
                if evaluate_condition('agent.py', 6, 'Eq', traffic_light.state,
                    carla.TrafficLightState.Red, 1, ['#']):
                    return True, traffic_light
        return False, None


    def _get_trafficlight_trigger_location(self, traffic_light):
        """
        Calculates the yaw of the waypoint that represents the trigger volume of the traffic light
        """

        def rotate_point(point, radians):
            """
            rotate a given point by a given angle
            """
            rotated_x = math.cos(radians) * point.x - math.sin(radians) * point.y
            rotated_y = math.sin(radians) * point.x - math.cos(radians) * point.y
            return carla.Vector3D(rotated_x, rotated_y, point.z)
        base_transform = traffic_light.get_transform()
        base_rot = base_transform.rotation.yaw
        area_loc = base_transform.transform(traffic_light.trigger_volume.location)
        area_ext = traffic_light.trigger_volume.extent
        point = rotate_point(carla.Vector3D(0, 0, area_ext.z), math.radians(
            base_rot))
        point_location = area_loc + carla.Location(x=point.x, y=point.y)
        return carla.Location(point_location.x, point_location.y, point_location.z)


    def _bh_is_vehicle_hazard(self, ego_wpt, ego_loc, vehicle_list,
        proximity_th, up_angle_th, low_angle_th=0, lane_offset=0):
        """
        Check if a given vehicle is an obstacle in our way. To this end we take
        into account the road and lane the target vehicle is on and run a
        geometry test to check if the target vehicle is under a certain distance
        in front of our ego vehicle. We also check the next waypoint, just to be
        sure there's not a sudden road id change.

        WARNING: This method is an approximation that could fail for very large
        vehicles, which center is actually on a different lane but their
        extension falls within the ego vehicle lane. Also, make sure to remove
        the ego vehicle from the list. Lane offset is set to +1 for right lanes
        and -1 for left lanes, but this has to be inverted if lane values are
        negative.

            :param ego_wpt: waypoint of ego-vehicle
            :param ego_log: location of ego-vehicle
            :param vehicle_list: list of potential obstacle to check
            :param proximity_th: threshold for the agent to be alerted of
            a possible collision
            :param up_angle_th: upper threshold for angle
            :param low_angle_th: lower threshold for angle
            :param lane_offset: for right and left lane changes
            :return: a tuple given by (bool_flag, vehicle, distance), where:
            - bool_flag is True if there is a vehicle ahead blocking us
                   and False otherwise
            - vehicle is the blocker object itself
            - distance is the meters separating the two vehicles
        """
        if evaluate_condition('agent.py', 7, 'Lt', ego_wpt.lane_id, 0, 0, ['#', 'and, 8']
            ) and evaluate_condition('agent.py', 8, 'NotEq', lane_offset, 0, 0, ['#']):
            lane_offset *= -1

        n = len(vehicle_list)
        i = 0
        while evaluate_condition('agent.py', 9, 'In', i, range(n), 2, ['#']):
            target_vehicle = vehicle_list[i]
            i += 1
            target_vehicle_loc = target_vehicle.get_location()
            target_wpt = self._map.get_waypoint(target_vehicle_loc)
            if evaluate_condition('agent.py', 10, 'NotEq', target_wpt.road_id,
                ego_wpt.road_id, 2, ['or, 11']) or evaluate_condition('agent.py', 11, 'NotEq',
                target_wpt.lane_id, ego_wpt.lane_id + lane_offset, 2, ['#']):
                next_wpt = self._local_planner.get_incoming_waypoint_and_direction(
                    steps=5)[0]
                if evaluate_condition('agent.py', 12, 'NotEq', target_wpt.
                    road_id, next_wpt.road_id, 2, ['or, 13']) or evaluate_condition('agent.py',
                    13, 'NotEq', target_wpt.lane_id, next_wpt.lane_id + lane_offset
                    , 2, ['#']):
                    continue
            if evaluate_condition('agent.py', 14, 'Pb', is_within_distance(target_vehicle_loc, ego_loc, self._vehicle.
                get_transform().rotation.yaw, proximity_th, up_angle_th,
                low_angle_th), None, 2, ['#']):
                return True, target_vehicle, compute_distance(target_vehicle_loc,
                    ego_loc)
        return False, None, -1


    def _is_vehicle_hazard(self, vehicle_list):
        """

        :param vehicle_list: list of potential obstacle to check
        :return: a tuple given by (bool_flag, vehicle), where
                 - bool_flag is True if there is a vehicle ahead blocking us
                   and False otherwise
                 - vehicle is the blocker object itself
        """
        ego_vehicle_location = self._vehicle.get_location()
        ego_vehicle_waypoint = self._map.get_waypoint(ego_vehicle_location)
        n = len(vehicle_list)
        i = 0
        while evaluate_condition('agent.py', 15, 'In', i, range(n), 3, ['#']):
            target_vehicle = vehicle_list[i]
            i += 1
            if evaluate_condition('agent.py', 16, 'Eq', target_vehicle.id, self
                ._vehicle.id, 3, ['#']):
                continue
            target_vehicle_waypoint = self._map.get_waypoint(target_vehicle.
                get_location())
            if evaluate_condition('agent.py', 17, 'NotEq',
                target_vehicle_waypoint.road_id, ego_vehicle_waypoint.road_id
                , 3, ['or, 18']) or evaluate_condition('agent.py', 18, 'NotEq',
                target_vehicle_waypoint.lane_id, ego_vehicle_waypoint.lane_id, 3, ['#']):
                continue
            if evaluate_condition('agent.py', 19, 'Pb', is_within_distance_ahead(target_vehicle.get_transform(), self.
                _vehicle.get_transform(), self._proximity_vehicle_threshold), None, 3, ['#']):
                return True, target_vehicle
        return False, None

    @staticmethod
    def emergency_stop():
        """
        Send an emergency stop command to the vehicle

            :return: control for braking
        """
        control = carla.VehicleControl()
        control.steer = 0.0
        control.throttle = 0.0
        control.brake = 1.0
        control.hand_brake = False
        return control

