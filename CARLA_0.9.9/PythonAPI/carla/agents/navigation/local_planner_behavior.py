#!/usr/bin/env python

# Copyright (c) 2018 Intel Labs.
# authors: German Ros (german.ros@intel.com)
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

""" This module contains a local planner to perform
low-level waypoint following based on PID controllers. """

from collections import deque
from enum import Enum

import carla
from agents.navigation.controller import VehiclePIDController
from agents.tools.misc import distance_vehicle, draw_waypoints
from instrumentation import evaluate_condition

class RoadOption(Enum):
    """
    RoadOption represents the possible topological configurations
    when moving from a segment of lane to other.
    """
    VOID = -1
    LEFT = 1
    RIGHT = 2
    STRAIGHT = 3
    LANEFOLLOW = 4
    CHANGELANELEFT = 5
    CHANGELANERIGHT = 6


class LocalPlanner(object):
    """
    LocalPlanner implements the basic behavior of following a trajectory
    of waypoints that is generated on-the-fly.
    The low-level motion of the vehicle is computed by using two PID controllers,
    one is used for the lateral control
    and the other for the longitudinal control (cruise speed).

    When multiple paths are available (intersections)
    this local planner makes a random choice.
    """

    # Minimum distance to target waypoint as a percentage
    # (e.g. within 80% of total distance)

    # FPS used for dt
    FPS = 20

    def __init__(self, agent):
        """
        :param agent: agent that regulates the vehicle
        :param vehicle: actor to apply to local planner logic onto
        """
        self._vehicle = agent.vehicle
        self._map = agent.vehicle.get_world().get_map()
        self._target_speed = None
        self.sampling_radius = None
        self._min_distance = None
        self._current_waypoint = None
        self.target_road_option = None
        self._next_waypoints = None
        self.target_waypoint = None
        self._vehicle_controller = None
        self._global_plan = None
        self._pid_controller = None
        self.waypoints_queue = deque(maxlen=20000)
        self._buffer_size = 5
        self._waypoint_buffer = deque(maxlen=self._buffer_size)
        self._init_controller()


    def reset_vehicle(self):
        """Reset the ego-vehicle"""
        self._vehicle = None
        print('Resetting ego-vehicle!')


    def _init_controller(self):
        """
        Controller initialization.

        dt -- time difference between physics control in seconds.
        This is can be fixed from server side
        using the arguments -benchmark -fps=F, since dt = 1/F

        target_speed -- desired cruise speed in km/h

        min_distance -- minimum distance to remove waypoint from queue

        lateral_dict -- dictionary of arguments to setup the lateral PID controller
                            {'K_P':, 'K_D':, 'K_I':, 'dt'}

        longitudinal_dict -- dictionary of arguments to setup the longitudinal PID controller
                            {'K_P':, 'K_D':, 'K_I':, 'dt'}
        """
        self.args_lat_hw_dict = {'K_P': 0.75, 'K_D': 0.02, 'K_I': 0.4, 'dt': 
            1.0 / self.FPS}
        self.args_lat_city_dict = {'K_P': 0.58, 'K_D': 0.02, 'K_I': 0.5, 'dt': 
            1.0 / self.FPS}
        self.args_long_hw_dict = {'K_P': 0.37, 'K_D': 0.024, 'K_I': 0.032, 'dt':
            1.0 / self.FPS}
        self.args_long_city_dict = {'K_P': 0.15, 'K_D': 0.05, 'K_I': 0.07, 'dt':
            1.0 / self.FPS}
        self._current_waypoint = self._map.get_waypoint(self._vehicle.
            get_location())
        self._global_plan = False
        self._target_speed = self._vehicle.get_speed_limit()
        self._min_distance = 3


    def set_speed(self, speed):
        """
        Request new target speed.

            :param speed: new target speed in km/h
        """
        self._target_speed = speed


    def set_global_plan(self, current_plan):
        """
        Sets new global plan.

            :param current_plan: list of waypoints in the actual plan
        """
        n = len(current_plan)
        i = 0
        while evaluate_condition('local_planner_behavior.py', 1, 'In', i, range(n), 1, ['#']):
            elem = current_plan[i]
            i += 1
            self.waypoints_queue.append(elem)
        self._global_plan = True


    def get_incoming_waypoint_and_direction(self, steps=3):
        """
        Returns direction and waypoint at a distance ahead defined by the user.

            :param steps: number of steps to get the incoming waypoint.
        """
        if evaluate_condition('local_planner_behavior.py', 2, 'Gt', len(self.
            waypoints_queue), steps, 0, ['#']):
            return self.waypoints_queue[steps]
        else:
            try:
                wpt, direction = self.waypoints_queue[-1]
                return wpt, direction
            except IndexError as i:
                print(i)
                return None, RoadOption.VOID
        return None, RoadOption.VOID


    def run_step(self, target_speed=None, debug=False):
        """
        Execute one step of local planning which involves
        running the longitudinal and lateral PID controllers to
        follow the waypoints trajectory.

            :param target_speed: desired speed
            :param debug: boolean flag to activate waypoints debugging
            :return: control
        """
        if evaluate_condition('local_planner_behavior.py', 3, 'IsNot',
            target_speed, None, 0, ['#']):
            self._target_speed = target_speed
        else:
            self._target_speed = self._vehicle.get_speed_limit()
        if evaluate_condition('local_planner_behavior.py', 4, 'Eq', len(self.
            waypoints_queue), 0, 0, ['#']):
            control = carla.VehicleControl()
            control.steer = 0.0
            control.throttle = 0.0
            control.brake = 1.0
            control.hand_brake = False
            control.manual_gear_shift = False
            return control
        if evaluate_condition('local_planner_behavior.py', 5, 'Nb', not self._waypoint_buffer, None, 0, ['#']):
            i = 0
            while evaluate_condition('local_planner_behavior.py', 6, 'In', i, range(self._buffer_size), 2, ['#']):
                i += 1
                if evaluate_condition('local_planner_behavior.py', 7, 'Pb', self.waypoints_queue, None, 2, ['#']):
                    self._waypoint_buffer.append(self.waypoints_queue.popleft())
                else:
                    break
        self._current_waypoint = self._map.get_waypoint(self._vehicle.
            get_location())
        self.target_waypoint, self.target_road_option = self._waypoint_buffer[0]
        if evaluate_condition('local_planner_behavior.py', 8, 'Gt',
            target_speed, 50, 0, ['#']):
            args_lat = self.args_lat_hw_dict
            args_long = self.args_long_hw_dict
        else:
            args_lat = self.args_lat_city_dict
            args_long = self.args_long_city_dict
        self._pid_controller = VehiclePIDController(self._vehicle, args_lateral
            =args_lat, args_longitudinal=args_long)
        control = self._pid_controller.run_step(self._target_speed, self.
            target_waypoint)
        vehicle_transform = self._vehicle.get_transform()
        max_index = -1

        n = len(self._waypoint_buffer)
        i = 0
        while evaluate_condition('local_planner_behavior.py', 9, 'In', i, range(n), 3, ['#']):
            (waypoint, _) = self._waypoint_buffer[i]

            if evaluate_condition('local_planner_behavior.py', 10, 'Lt',
                distance_vehicle(waypoint, vehicle_transform), self._min_distance, 3, ['#']):
                max_index = i

            i += 1

        if evaluate_condition('local_planner_behavior.py', 11, 'GtE', max_index, 0, 0, ['#']):
            i = 0
            while evaluate_condition('local_planner_behavior.py', 12, 'In', i, range(max_index + 1), 4, ['#']):
                i += 1
                self._waypoint_buffer.popleft()
        if evaluate_condition('local_planner_behavior.py', 13, 'Pb', debug, None, 0, ['#']):
            draw_waypoints(self._vehicle.get_world(), [self.target_waypoint], 1.0)
        return control

