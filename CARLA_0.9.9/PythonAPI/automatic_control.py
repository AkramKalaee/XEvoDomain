#!/usr/bin/env python

# Copyright (c) 2018 Intel Labs.
# authors: German Ros (german.ros@intel.com)
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""Example of automatic vehicle control from client side."""

from __future__ import print_function

import linecache

import signal

import threading

import subprocess
import setting
import time
import coverage
import argparse
import collections
import csv
import datetime
import glob
import logging
import math
import os
import random
import re
import sys
import weakref


#from srunner.challenge.envs.sensor_interface import CANBusSensor, CallBack, SensorInterface
#from srunner.challenge.envs.scene_layout_sensors import threaded
# from agents.navigation.basic_agent import BasicAgent
# from agents.navigation.behavior_agent import BehaviorAgent
# from agents.navigation.roaming_agent import RoamingAgent

try:
    import pygame
    from pygame.locals import KMOD_CTRL
    from pygame.locals import K_ESCAPE
    from pygame.locals import K_q
except ImportError:
    raise RuntimeError('cannot import pygame, make sure pygame package is installed')

try:
    import numpy as np
except ImportError:
    raise RuntimeError(
        'cannot import numpy, make sure numpy package is installed')

# ==============================================================================
# -- Find CARLA module ---------------------------------------------------------
# ==============================================================================
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

# ==============================================================================
# -- Add PythonAPI for release mode --------------------------------------------
# ==============================================================================
try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/carla')
except IndexError:
    pass

import carla
from carla import ColorConverter as cc



# ==============================================================================
# -- Global functions ----------------------------------------------------------
# ==============================================================================


def find_weather_presets():
    """Method to find weather presets"""
    rgx = re.compile('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)')
    def name(x): return ' '.join(m.group(0) for m in rgx.finditer(x))
    presets = [x for x in dir(carla.WeatherParameters) if re.match('[A-Z].+', x)]
    return [(getattr(carla.WeatherParameters, x), name(x)) for x in presets]


def get_actor_display_name(actor, truncate=250):
    """Method to get actor display name"""
    name = ' '.join(actor.type_id.replace('_', '.').title().split('.')[1:])
    return (name[:truncate - 1] + u'\u2026') if len(name) > truncate else name


# ==============================================================================
# -- World ---------------------------------------------------------------
# ==============================================================================

class World(object):
    """ Class representing the surrounding environment """

    def __init__(self, carla_world, hud, args):
        """Constructor method"""
        self.world = carla_world
        try:
            self.map = self.world.get_map()
        except RuntimeError as error:
            print('RuntimeError: {}'.format(error))
            print('  The server could not send the OpenDRIVE (.xodr) file:')
            print('  Make sure it exists, has the same name of your town, and is correct.')
            sys.exit(1)
        self.hud = hud
        self.hud.pathId = args.pathId
        self.hud.round = args.round
        self.hud.scenario = args.scenario
        self.player = None
        self.walker = None
        self.can_bus_sensor = None
        self.collision_sensor = None
        self.obstacle_detection_sensor = None
        self.lane_invasion_sensor = None
        self.gnss_sensor = None
        self.camera_manager = None
        self.can_bus_sensor = None
        self._weather_presets = find_weather_presets()
        self._weather_index = 0
        self._actor_filter = args.filter
        self._gamma = args.gamma
        self.restart(args)
        self.world.on_tick(hud.on_world_tick)
        self.recording_enabled = False
        self.recording_start = 0

    def restart(self, args):
        """Restart the world"""
        # Keep same camera config if the camera manager exists.
        cam_index = self.camera_manager.index if self.camera_manager is not None else 0
        cam_pos_id = self.camera_manager.transform_index if self.camera_manager is not None else 0
        # Set the seed if requested by user
        if args.seed is not None:
            random.seed(args.seed)

        # Get a random blueprint.
        blueprint = random.choice(self.world.get_blueprint_library().filter(self._actor_filter))
        blueprint.set_attribute('role_name', 'hero')
        if blueprint.has_attribute('color'):
            color = random.choice(blueprint.get_attribute('color').recommended_values)
            blueprint.set_attribute('color', color)
        # Spawn the player.
        print("Spawning the player")
        if self.player is not None:
            print("self.player is not None")
            spawn_point = self.player.get_transform()
            spawn_point.location.z += 2.0
            spawn_point.rotation.roll = 0.0
            spawn_point.rotation.pitch = 0.0

            self.destroy()
            self.player = self.world.try_spawn_actor(blueprint, spawn_point)

        while self.player is None:
            if not self.map.get_spawn_points():
                print('There are no spawn points available in your map/town.')
                print('Please add some Vehicle Spawn Point to your UE4 scene.')
                sys.exit(1)
            spawn_points = self.map.get_spawn_points()
            # print(len(self.map.get_topology()))
            # all_lanes = [lane[0].lane_type for lane in self.map.get_topology()]
            # my_dict = {i: all_lanes.count(i) for i in all_lanes}
            # print(my_dict)
            # print(self.map.get_topology()[0][0])
            # print(self.map.get_topology()[0][1])
            #
            # print(self.map.get_topology()[5][0])
            # print(self.map.get_topology()[5][1])

            spawn_point = random.choice(spawn_points) if spawn_points else carla.Transform()
            # _x = -9.0040346145629854e+1  # Real(road[0][2], road[1][2]).rand()
            # _y = -135.23939514160156  # Real(road[2][2], road[3][2]).rand()
            # _z = 0.055450439453125  # Real(road[4][2], road[5][2]).rand()
            # _yaw = 0.44256171584129333  # Real(road[6][2], road[7][2]).rand()
            #
            #
            # spawn_point = carla.Transform(carla.Location(_x, _y, _z), carla.Rotation(pitch=0, yaw=_yaw, roll=0))
            # print(spawn_point)
            # print(blueprint)
            # print("try_spawn_actor...")
            # print("**************************")
            self.player = self.world.try_spawn_actor(blueprint, spawn_point)
        print("Set up the sensors")
        # Set up the sensors.

        self.can_bus_sensor = CANBusSensor(self.player, self.world, 65)
        CANBusSensor._set_ref(weakref.ref(self.can_bus_sensor))


        self.lane_invasion_sensor = LaneInvasionSensor(self.player, self.hud)
        self.gnss_sensor = GnssSensor(self.player)
        self.obstacle_detection_sensor = ObstacleDetectionSensor(self.player)
        self.collision_sensor = CollisionSensor(self.player, self.hud)  # , weakref.ref(self.can_bus_sensor)

        # setup callback


        # while not self.sensor_interface.all_sensors_ready():
        #     print(" waiting for one data reading from sensors...")
        #     CarlaDataProvider.perform_carla_tick()

        self.camera_manager = CameraManager(self.player, self.hud, self._gamma)
        self.camera_manager.transform_index = cam_pos_id
        self.camera_manager.set_sensor(cam_index, notify=False)
        actor_type = get_actor_display_name(self.player)
        self.hud.notification(actor_type)

    def next_weather(self, reverse=False):
        """Get next weather setting"""
        self._weather_index += -1 if reverse else 1
        self._weather_index %= len(self._weather_presets)
        preset = self._weather_presets[self._weather_index]
        self.hud.notification('Weather: %s' % preset[1])
        self.player.get_world().set_weather(preset[0])

    def tick(self, clock):
        """Method for every tick"""
        self.hud.tick(self, clock)

    def render(self, display):
        """Render world"""
        self.camera_manager.render(display)
        self.hud.render(display)

    def destroy_sensors(self):
        """Destroy sensors"""
        self.camera_manager.sensor.destroy()
        self.camera_manager.sensor = None
        self.camera_manager.index = None

    def destroy(self):
        """Destroys all actors"""
        actors = [
            self.camera_manager.sensor,
            self.collision_sensor.sensor,
            self.lane_invasion_sensor.sensor,
            self.gnss_sensor.sensor,
            self.obstacle_detection_sensor.sensor,
            self.player]
        for actor in actors:
            if actor is not None:
                actor.destroy()


# ==============================================================================
# -- KeyboardControl -----------------------------------------------------------
# ==============================================================================


class KeyboardControl(object):
    def __init__(self, world):
        world.hud.notification("Press 'H' or '?' for help.", seconds=4.0)

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYUP:
                if self._is_quit_shortcut(event.key):
                    return True

    @staticmethod
    def _is_quit_shortcut(key):
        """Shortcut for quitting"""
        return (key == K_ESCAPE) or (key == K_q and pygame.key.get_mods() & KMOD_CTRL)

# ==============================================================================
# -- HUD -----------------------------------------------------------------------
# ==============================================================================


class HUD(object):
    """Class for HUD text"""

    def __init__(self, width, height):
        """Constructor method"""
        self.dim = (width, height)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        font_name = 'courier' if os.name == 'nt' else 'mono'
        fonts = [x for x in pygame.font.get_fonts() if font_name in x]
        default_font = 'ubuntumono'
        mono = default_font if default_font in fonts else fonts[0]
        mono = pygame.font.match_font(mono)
        self._font_mono = pygame.font.Font(mono, 12 if os.name == 'nt' else 14)
        self._notifications = FadingText(font, (width, 40), (0, height - 40))
        self.help = HelpText(pygame.font.Font(mono, 24), width, height)
        self.server_fps = 0
        self.frame = 0
        self.simulation_time = 0
        self._show_info = True
        self._info_text = []
        self._server_clock = pygame.time.Clock()
        self.log = []
        self._collision_occured = False
        self.pathId = 0
        self.round = 0
        self.scenario = ''
        self.counter = 1
        self.cov = None

    def on_world_tick(self, timestamp):
        # while True:
        #     if self.cov is None:
        #         print('---------------------------->_on_cov_start', self.counter)
        #         self.cov = coverage.Coverage(
        #         data_file='C:/CARLA/experiment/path_{}/round_{}/{}_coverage/.coverage'.format(self.pathId, self.round,
        #                                                                                       self.scenario),
        #         data_suffix='{}'.format(self.counter), branch=True)#,
        #         # include=['*automatic_control*', '*agent*', '*behavior_agent*', '*controller*',
        #         #          '*local_planner_behavior*'])
        #         #CANBusSensor.weak_self.cov = self.cov
        #         #self.cov.start()
        #
        #         break
        #     else:
        #         print('---------------------------->_on_cov_stop', self.counter)
        #
        #         #self.cov.stop()
        #
        #         #self.cov.save()
        #         self.cov = None
        #         #CANBusSensor.weak_self.cov = None
        #         self.counter += 1


        """Gets informations from the world at every tick"""
        #print('*')
        self._server_clock.tick()
        self.server_fps = self._server_clock.get_fps()
        self.frame = timestamp.frame_count
        self.simulation_time = timestamp.elapsed_seconds
        #print('-------------->on_world_tick',self.frame)

    def tick(self, world, clock):
        #print('---------------------------->on_hud_tick',self.frame, '                  ', clock.get_time())
        """HUD method for every tick"""
        self._notifications.tick(world, clock)

        can_bus_history = CANBusSensor._get_ref().get_history()
        if len(can_bus_history) == 0:
            return
        can_bus_history.sort(key = lambda x: (x[0], x[1]['timestamp']))
        collision_history = world.collision_sensor.get_collision_frame_history()
        for can_bus_data in can_bus_history:
            _frame = can_bus_data[0]
            _data = can_bus_data[1]

            _collision_list = [item for item in collision_history if item[0] == _frame]
            if len(_collision_list) == 0:
                _collision = ''
            else:
                _collision = _collision_list[0]

            ego_transform = _data['transform']  # world.player.get_transform()
            ego_location_x = ego_transform['x']
            ego_location_y = ego_transform['y']
            ego_location_z = ego_transform['z']
            ego_location_yaw = ego_transform['yaw']
            ego_location_pitch = ego_transform['pitch']
            ego_location_roll = ego_transform['roll']

            ego_velocity = _data['simple_velocity']  # world.player.get_velocity()

            #weather
            weather = _data['weather']
            cloudiness = weather['cloudiness']
            fog_density = weather['fog_density']
            fog_distance = weather['fog_distance']
            precipitation = weather['precipitation']
            precipitation_deposits = weather['precipitation_deposits']
            sun_altitude_angle = weather['sun_altitude_angle']
            sun_azimuth_angle = weather['sun_azimuth_angle']
            wetness = weather['wetness']
            wind_intensity = weather['wind_intensity']
            #
            _pedestrain = _data['walker']
            other_actor_target_velocity = 0
            other_actor_yaw = None
            start_distance = None
            ped_location_x = None
            ped_location_y = None
            ped_location_y = None
            ped_location_z = None
            other_actor_yaw = None
            ped_location_pitch = None
            ped_location_roll = None
            start_distance = None
            if _pedestrain is not None:
                other_actor_target_velocity = _pedestrain['speed']
                ped_location = _pedestrain['transform']
                ped_location_x = ped_location['x']
                ped_location_y = ped_location['y']
                ped_location_z = ped_location['z']
                other_actor_yaw = ped_location['yaw']
                ped_location_pitch = ped_location['pitch']
                ped_location_roll = ped_location['roll']
                start_distance = _pedestrain['distance']

            # if _collision == '' and  _ped_speed == 0:
            #     continue
            road = _data['road']
            road_id = road['road_id']
            lane_id = road['lane_id']
            curvature = road['curvature']

            _obstacle = _data['obstacle']
            _timestamp = _data['timestamp']
            _coverage_path = _data['coverage_path']

            speed = _data['speed']
            lateral_speed = _data['lateral_speed']
            linear_velocity = _data['linear_velocity']
            simple_velocity = _data['simple_velocity']
            linear_acceleration = _data['linear_acceleration']
            torque_curve = _data['torque_curve']
            max_rpm = _data['max_rpm']
            moi = _data['moi']
            damping_rate_full_throttle = _data['damping_rate_full_throttle']
            damping_rate_zero_throttle_clutch_disengaged = _data['damping_rate_zero_throttle_clutch_disengaged']
            use_gear_autobox = _data['use_gear_autobox']
            clutch_strength = _data['clutch_strength']
            mass = _data['mass']
            center_of_mass = _data['center_of_mass']
            center_of_mass_x = center_of_mass['x']
            center_of_mass_y = center_of_mass['y']
            center_of_mass_z = center_of_mass['z']

            steering_curve = _data['steering_curve']
            wheels = _data['wheels']
            tire_friction = wheels[0]['tire_friction']
            steer_angle = wheels[0]['steer_angle']

            self.log.append(
                [_frame,  _timestamp, _collision, _obstacle, _coverage_path,
                 cloudiness, precipitation, precipitation_deposits, wind_intensity, sun_azimuth_angle,
                 sun_altitude_angle, fog_density, fog_distance,
                 wetness, start_distance, other_actor_target_velocity, other_actor_yaw, tire_friction, ego_location_x,
                 ego_location_y, ego_location_z, ego_location_yaw, ego_velocity, road_id, lane_id, curvature, ped_location_x,
                 ped_location_y, ped_location_z, linear_acceleration, torque_curve, steering_curve,steer_angle, lateral_speed , _data])

            #todo: append other useful info

    def toggle_info(self):
        """Toggle info on or off"""
        self._show_info = not self._show_info

    def notification(self, text, seconds=2.0):
        """Notification text"""
        self._notifications.set_text(text, seconds=seconds)

    def error(self, text):
        """Error text"""
        self._notifications.set_text('Error: %s' % text, (255, 0, 0))

    def render(self, display):
        """Render for HUD class"""
        if self._show_info:
            info_surface = pygame.Surface((220, self.dim[1]))
            info_surface.set_alpha(100)
            display.blit(info_surface, (0, 0))
            v_offset = 4
            bar_h_offset = 100
            bar_width = 106
            for item in self._info_text:
                if v_offset + 18 > self.dim[1]:
                    break
                if isinstance(item, list):
                    if len(item) > 1:
                        points = [(x + 8, v_offset + 8 + (1 - y) * 30) for x, y in enumerate(item)]
                        pygame.draw.lines(display, (255, 136, 0), False, points, 2)
                    item = None
                    v_offset += 18
                elif isinstance(item, tuple):
                    if isinstance(item[1], bool):
                        rect = pygame.Rect((bar_h_offset, v_offset + 8), (6, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect, 0 if item[1] else 1)
                    else:
                        rect_border = pygame.Rect((bar_h_offset, v_offset + 8), (bar_width, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect_border, 1)
                        fig = (item[1] - item[2]) / (item[3] - item[2])
                        if item[2] < 0.0:
                            rect = pygame.Rect(
                                (bar_h_offset + fig * (bar_width - 6), v_offset + 8), (6, 6))
                        else:
                            rect = pygame.Rect((bar_h_offset, v_offset + 8), (fig * bar_width, 6))
                        pygame.draw.rect(display, (255, 255, 255), rect)
                    item = item[0]
                if item:  # At this point has to be a str.
                    surface = self._font_mono.render(item, True, (255, 255, 255))
                    display.blit(surface, (8, v_offset))
                v_offset += 18
        self._notifications.render(display)
        self.help.render(display)

# ==============================================================================
# -- FadingText ----------------------------------------------------------------
# ==============================================================================


class FadingText(object):
    """ Class for fading text """

    def __init__(self, font, dim, pos):
        """Constructor method"""
        self.font = font
        self.dim = dim
        self.pos = pos
        self.seconds_left = 0
        self.surface = pygame.Surface(self.dim)

    def set_text(self, text, color=(255, 255, 255), seconds=2.0):
        """Set fading text"""
        text_texture = self.font.render(text, True, color)
        self.surface = pygame.Surface(self.dim)
        self.seconds_left = seconds
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(text_texture, (10, 11))

    def tick(self, _, clock):
        """Fading text method for every tick"""
        delta_seconds = 1e-3 * clock.get_time()
        self.seconds_left = max(0.0, self.seconds_left - delta_seconds)
        self.surface.set_alpha(500.0 * self.seconds_left)

    def render(self, display):
        """Render fading text method"""
        display.blit(self.surface, self.pos)

# ==============================================================================
# -- HelpText ------------------------------------------------------------------
# ==============================================================================


class HelpText(object):
    """ Helper class for text render"""

    def __init__(self, font, width, height):
        """Constructor method"""
        lines = __doc__.split('\n')
        self.font = font
        self.dim = (680, len(lines) * 22 + 12)
        self.pos = (0.5 * width - 0.5 * self.dim[0], 0.5 * height - 0.5 * self.dim[1])
        self.seconds_left = 0
        self.surface = pygame.Surface(self.dim)
        self.surface.fill((0, 0, 0, 0))
        for i, line in enumerate(lines):
            text_texture = self.font.render(line, True, (255, 255, 255))
            self.surface.blit(text_texture, (22, i * 22))
            self._render = False
        self.surface.set_alpha(220)

    def toggle(self):
        """Toggle on or off the render help"""
        self._render = not self._render

    def render(self, display):
        """Render help text method"""
        if self._render:
            display.blit(self.surface, self.pos)

# ==============================================================================
# -- CollisionSensor -----------------------------------------------------------
# ==============================================================================


class CollisionSensor(object):
    """ Class for collision sensors"""

    def __init__(self, parent_actor, hud):
        """Constructor method"""
        self.sensor = None
        self.history = []
        #Akram Kalaee
        self.frame_history = []
        #end
        self._parent = parent_actor
        self.hud = hud
        world = self._parent.get_world()
        blueprint = world.get_blueprint_library().find('sensor.other.collision')
        self.sensor = world.spawn_actor(blueprint, carla.Transform(), attach_to=self._parent)
        # We need to pass the lambda a weak reference to
        # self to avoid circular reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: CollisionSensor._on_collision(weak_self, event))

    #Akram Kalaee
    def get_collision_frame_history(self):
        result, self.frame_history = self.frame_history, []
        return result

    def get_collision_history(self):
        """Gets the history of collisions"""
        history = collections.defaultdict(int)
        for frame, intensity in self.history:
            history[frame] += intensity
        return history

    @staticmethod
    def _on_collision(weak_self, event):

        self = weak_self()
        if not self:
            return
        #print("------------------>_on_collision", event.frame)
        CANBusSensor._on_can_bus_event(event)

        # actor_type = get_actor_display_name(event.other_actor)
        # self.hud.notification('Collision with %r' % actor_type)
        #Akram Kalaee

        #self.hud.set_collision_status(True)
        #print(self.frame_history)

        impulse = event.normal_impulse
        intensity = math.sqrt(impulse.x ** 2 + impulse.y ** 2 + impulse.z ** 2)
        actor_type = get_actor_display_name(event.other_actor)
        self.hud.notification('Collision with %r' % actor_type)
        self.frame_history.append((event.frame, actor_type, intensity))

        self.history.append((event.frame, intensity))
        if len(self.history) > 4000:
            self.history.pop(0)

# ==============================================================================
# -- LaneInvasionSensor --------------------------------------------------------
# ==============================================================================


class LaneInvasionSensor(object):
    """Class for lane invasion sensors"""

    def __init__(self, parent_actor, hud):
        """Constructor method"""
        self.sensor = None
        self._parent = parent_actor
        self.hud = hud
        world = self._parent.get_world()
        bp = world.get_blueprint_library().find('sensor.other.lane_invasion')
        self.sensor = world.spawn_actor(bp, carla.Transform(), attach_to=self._parent)
        # We need to pass the lambda a weak reference to self to avoid circular
        # reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: LaneInvasionSensor._on_invasion(weak_self, event))

    @staticmethod
    def _on_invasion(weak_self, event):

        """On invasion method"""
        self = weak_self()
        if not self:
            return
        lane_types = set(x.type for x in event.crossed_lane_markings)
        text = ['%r' % str(x).split()[-1] for x in lane_types]
        self.hud.notification('Crossed line %s' % ' and '.join(text))


# ==============================================================================
# -- ObstacleDetectionSensor --------------------------------------------------------
# ==============================================================================
class ObstacleDetectionSensor(object):

    def __init__(self, parent_actor):
        self.sensor = None
        self._parent = parent_actor
        self.distance = None
        self._event_count = 0
        world = self._parent.get_world()
        bp = world.get_blueprint_library().find('sensor.other.obstacle')
        bp.set_attribute('distance', '5')
        bp.set_attribute('hit_radius', '0.5')
        bp.set_attribute('only_dynamics', 'true')
        # bp.set_attribute('debug_linetrace', 'true')
        bp.set_attribute('sensor_tick', '1')
        self.sensor = world.spawn_actor(bp, carla.Transform(), attach_to=self._parent)
        # We need to pass the lambda a weak reference to self to avoid circular
        # reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: ObstacleDetectionSensor._on_obstacle(weak_self, event))

    @staticmethod
    def _on_obstacle(weak_self, event):
        self = weak_self()
        if not self:
            return
        if event.other_actor.type_id.startswith('walker.'):
            #print("------------------>_on_obstacle", event.frame)
            CANBusSensor._on_can_bus_event(event)
            self.distance = event.distance
            self._event_count += 1

            print ("Event %s, in line of sight with %s at distance %u" % (self._event_count, event.other_actor.type_id, event.distance))


# ==============================================================================
# -- CANBUSSensor --------------------------------------------------------
# ==============================================================================
class CANBusSensor(object):
    """
    CAN BUS pseudo sensor that gets to read all the vehicle proprieties including speed.
    This sensor is not placed at the CARLA environment. It is
    only an asynchronous interface to the forward speed.
    """
    MAX_CONNECTION_ATTEMPTS = 10
    weak_self = None
    coverage_path = None
    def __init__(self, vehicle, world, reading_frequency):
        # The vehicle where the class reads the speed
        self._vehicle = vehicle
        self._world = world
        self._map = self._world.get_map()
        # How often do you look at your speedometer in hz
        self._reading_frequency = reading_frequency
        #  Counts the frames
        self._frame = 0
        self._timestamp = 0
        self._data = None
        self._history = []
        self._run_ps = True


    @classmethod
    def _set_ref(cls, ref):
        cls.weak_self = ref()

    @classmethod
    def _get_ref(cls):
        return cls.weak_self

    def _get_forward_speed(self, transform=None, velocity=None):
        """ Convert the vehicle transform directly to forward speed """
        if not velocity:
            velocity = self._vehicle.get_velocity()
        if not transform:
            transform = self._vehicle.get_transform()

        vel_np = np.array([velocity.x, velocity.y, velocity.z])
        pitch = np.deg2rad(transform.rotation.pitch)
        yaw = np.deg2rad(transform.rotation.yaw)
        orientation = np.array([np.cos(pitch) * np.cos(yaw), np.cos(pitch) * np.sin(yaw), np.sin(pitch)])
        speed = np.dot(vel_np, orientation)
        return speed

    def _get_rotation_matrix(self, transform=None):
        """
        from: https://github.com/xmyqsh/scenario_runner/tree/development
        Generate the rotation matrix from Euler angles (actually, Tait-Bryan angles)
        with intrinsic sequence ZYX
        """
        if not transform:
            transform = self._vehicle.get_transform()

        roll = np.deg2rad(-transform.rotation.roll)
        pitch = np.deg2rad(-transform.rotation.pitch)
        yaw = np.deg2rad(transform.rotation.yaw)
        sr, cr = np.sin(roll), np.cos(roll)
        sp, cp = np.sin(pitch), np.cos(pitch)
        sy, cy = np.sin(yaw), np.cos(yaw)
        rotation_matrix = np.array([[cy * cp, -sy * sr + cy * sp * sr, cy * sp * cr + sy * sr],
                                    [sy * cp, cy * sp * sr + cy * sr, -cy * sr + sy * sp * cr],
                                    [-sp, cp * sr, cp * cr]])
        return rotation_matrix

    def _get_linear_velocity(self, velocity=None):
        """
        from: https://github.com/xmyqsh/scenario_runner/tree/development
        Convert linear velocity from world frame to vehicle reference frame
        """

        if not velocity:
            velocity = self._vehicle.get_velocity()

        rotation_matrix = self._get_rotation_matrix()
        linear_velocity_vrf = rotation_matrix.transpose().dot(velocity)
        result = []
        for row in linear_velocity_vrf:
            for v3d in row:
                result.append(
                    {'x': v3d.x,
                     'y': v3d.y,
                     'z': v3d.z
                     }
                )

        return result

    def _get_linear_acceleration(self, acceleration=None):
        """
        from: https://github.com/xmyqsh/scenario_runner/tree/development
        Convert linear acceleration from world frame to vehicle reference frame
        """

        if not acceleration:
            acceleration = self._vehicle.get_acceleration()

        rotation_matrix = self._get_rotation_matrix()
        linear_acceleration_vrf = rotation_matrix.transpose().dot(acceleration)
        result = []
        for row in linear_acceleration_vrf:
            for v3d in row:
                result.append(
                    {'x': v3d.x,
                     'y': v3d.y,
                     'z': v3d.z
                     }
                )
        return result

    def _get_angular_velocity(self, angular_velocity=None):
        """ Convert angular velocity from world frame to vehicle reference frame """

        if not angular_velocity:
            angular_velocity = self._vehicle.get_angular_velocity()

        rotation_matrix = self._get_rotation_matrix()
        angular_velocity_vrf = rotation_matrix.transpose().dot(angular_velocity)

        result = []
        for row in angular_velocity_vrf:
            for v3d in row:
                result.append(
                    {'x': v3d.x,
                     'y': v3d.y,
                     'z': v3d.z
                     }
                )
        return result

    def _get_simple_velocity(self, velocity=None):
        if not velocity:
            velocity = self._vehicle.get_velocity()
        return 3.6 * math.sqrt(velocity.x ** 2 + velocity.y ** 2 + velocity.z ** 2)

    def _get_weather(self, weather = None):
        if not weather:
            weather = self._world.get_weather()
        return {
            'cloudiness': weather.cloudiness,
            'fog_density': weather.fog_density,
            'fog_distance': weather.fog_distance,
            'precipitation': weather.precipitation,
            'precipitation_deposits': weather.precipitation_deposits,
            'sun_altitude_angle': weather.sun_altitude_angle,
            'sun_azimuth_angle': weather.sun_azimuth_angle,
            'wetness': weather.wetness,
            'wind_intensity': weather.wind_intensity}

    def _get_walker_info(self, vehicle_transform):
        walkers = self._world.get_actors().filter('walker.*')
        if len(walkers) == 0:
            return None

        walker = walkers[0]
        if walker is not None:
            _ped_Speed = walker.get_control().speed
            _ped_transform = walker.get_transform()
            #_ped_Location = '(% 5.1f, % 5.1f, % 5.1f, % 5.1f)' % (_ped_transform.location.x, _ped_transform.location.y, _ped_transform.location.z, _ped_transform.rotation.yaw)
            def distance(l): return math.sqrt(
                (l.x - vehicle_transform.location.x) ** 2 + (l.y - vehicle_transform.location.y) ** 2 + (l.z - vehicle_transform.location.z) ** 2)
            _distance = '% 20s' % distance(walker.get_location())

        return {
            'speed':_ped_Speed,
            'transform':self._get_transform(_ped_transform),
            'distance': _distance
        }

    def _get_road_info(self, transform):
        waypoint = self._map.get_waypoint(transform.location)
        return {'road_id': waypoint.road_id,
                'lane_id': waypoint.lane_id,
                'curvature': get_curvature(waypoint, 1.0)}

    def _get_transform(self, transform):
        location = transform.location
        rotation = transform.rotation
        return {'x': location.x,
                'y': location.y,
                'z': location.z,
                'yaw': rotation.yaw,
                'pitch': rotation.pitch,
                'roll': rotation.roll}

    def __call__(self):
        """ We convert the vehicle physics information into a convenient dictionary """

        # protect this access against timeout
        attempts = 0
        while attempts < self.MAX_CONNECTION_ATTEMPTS:
            try:
                vehicle_physics = self._vehicle.get_physics_control()
                velocity = self._vehicle.get_velocity()
                angular_velocity = self._vehicle.get_angular_velocity()
                transform = self._vehicle.get_transform()
                acceleration = self._vehicle.get_acceleration()
                weather = self._world.get_weather()

                break
            except Exception:
                attempts += 1
                print('======[WARNING] The server is frozen [{}/{} attempts]!!'.format(attempts,
                                                                                       self.MAX_CONNECTION_ATTEMPTS))
                time.sleep(1.0)
                continue

        wheels_list_dict = []
        for wheel in vehicle_physics.wheels:
            wheels_list_dict.append(
                {'tire_friction': wheel.tire_friction,
                 'damping_rate': wheel.damping_rate,
                 'steer_angle': wheel.max_steer_angle
                 }
            )

        torque_curve = []
        for point in vehicle_physics.torque_curve:
            torque_curve.append({'x': point.x,
                                 'y': point.y
                                 })
        steering_curve = []
        for point in vehicle_physics.steering_curve:
            steering_curve.append({'x': point.x,
                                   'y': point.y
                                   })

        return {
            'coverage_path':'',
            'timestamp':'',
            'obstacle':'',
            'weather': self._get_weather(weather = weather),
            'transform': self._get_transform(transform),
            'walker': self._get_walker_info(transform),
            'road': self._get_road_info(transform),
            'dimensions': {'length': self._vehicle.bounding_box.extent.x,
                           'width': self._vehicle.bounding_box.extent.y,
                           'height': self._vehicle.bounding_box.extent.z},
            'speed': self._get_forward_speed(transform=transform, velocity=velocity),
            'lateral_speed': self._get_angular_velocity(angular_velocity=angular_velocity),
            'linear_velocity': self._get_linear_velocity(velocity=velocity),
            'simple_velocity': self._get_simple_velocity(velocity=velocity),
            'linear_acceleration': self._get_linear_acceleration(acceleration=acceleration),
            'torque_curve': torque_curve,
            'max_rpm': vehicle_physics.max_rpm,
            'moi': vehicle_physics.moi,
            'damping_rate_full_throttle': vehicle_physics.damping_rate_full_throttle,
            'damping_rate_zero_throttle_clutch_disengaged':
                vehicle_physics.damping_rate_zero_throttle_clutch_disengaged,
            'use_gear_autobox': vehicle_physics.use_gear_autobox,
            'clutch_strength': vehicle_physics.clutch_strength,
            'mass': vehicle_physics.mass,
            'drag_coefficient': vehicle_physics.drag_coefficient,
            'center_of_mass': {'x': vehicle_physics.center_of_mass.x,
                               'y': vehicle_physics.center_of_mass.y,
                               'z': vehicle_physics.center_of_mass.z
                               },
            'steering_curve': steering_curve,
            'wheels': wheels_list_dict
        }

    @classmethod
    def _on_can_bus_event(cls, event):

        cls.weak_self._data = cls.weak_self.__call__()
        cls.weak_self._frame = event.frame
        cls.weak_self._timestamp = event.timestamp
        cls.weak_self._data['timestamp'] = event.timestamp
        try:
            if cls.coverage_path is not None:
                cls.weak_self._data['coverage_path'], cls.coverage_path = cls.coverage_path, None

            if event.other_actor is not None:
                actor_type = get_actor_display_name(event.other_actor)
                cls.weak_self._data['obstacle'] = (actor_type, event.distance)
        except:
            pass

        cls.weak_self._history.append((event.frame, cls.weak_self._data))
        transform = cls.weak_self._data['transform']
        import numpy as np
        loc = (np.float32(transform['x']), np.float32(transform['y']), np.float32(transform['z']))
        loc64 = (np.float64(transform['x']), np.float64(transform['y']), np.float64(transform['z']))
        #print('-------------->_on_can_bus_event')


    def get_history(self):
        #print("---------------------->get data from can bus", self._frame)
        result, self._history = self._history, []
        return result

    def stop(self):
        self._run_ps = False

    def destroy(self):
        self._run_ps = False

# ==============================================================================
# -- GnssSensor --------------------------------------------------------
# ==============================================================================
class GnssSensor(object):
    """ Class for GNSS sensors"""

    def __init__(self, parent_actor):
        """Constructor method"""
        self.sensor = None
        self._parent = parent_actor
        self.lat = 0.0
        self.lon = 0.0
        world = self._parent.get_world()
        blueprint = world.get_blueprint_library().find('sensor.other.gnss')
        self.sensor = world.spawn_actor(blueprint, carla.Transform(carla.Location(x=1.0, z=2.8)),
                                        attach_to=self._parent)
        # We need to pass the lambda a weak reference to
        # self to avoid circular reference.
        weak_self = weakref.ref(self)
        self.sensor.listen(lambda event: GnssSensor._on_gnss_event(weak_self, event))

    @staticmethod
    def _on_gnss_event(weak_self, event):
        self = weak_self()
        if not self:
            return
        #print("------------------>_on_gnss_event", event.frame)
        CANBusSensor._on_can_bus_event(event)
        self.lat = event.latitude
        self.lon = event.longitude

# ==============================================================================
# -- CameraManager -------------------------------------------------------------
# ==============================================================================


class CameraManager(object):
    """ Class for camera management"""

    def __init__(self, parent_actor, hud, gamma_correction):
        """Constructor method"""
        self.sensor = None
        self.surface = None
        self._parent = parent_actor
        self.hud = hud
        self.recording = False
        bound_y = 0.5 + self._parent.bounding_box.extent.y
        attachment = carla.AttachmentType
        self._camera_transforms = [
            (carla.Transform(
                carla.Location(x=-5.5, z=2.5), carla.Rotation(pitch=8.0)), attachment.SpringArm),
            (carla.Transform(
                carla.Location(x=1.6, z=1.7)), attachment.Rigid),
            (carla.Transform(
                carla.Location(x=5.5, y=1.5, z=1.5)), attachment.SpringArm),
            (carla.Transform(
                carla.Location(x=-8.0, z=6.0), carla.Rotation(pitch=6.0)), attachment.SpringArm),
            (carla.Transform(
                carla.Location(x=-1, y=-bound_y, z=0.5)), attachment.Rigid)]
        self.transform_index = 1
        self.sensors = [
            ['sensor.camera.rgb', cc.Raw, 'Camera RGB'],
            ['sensor.camera.depth', cc.Raw, 'Camera Depth (Raw)'],
            ['sensor.camera.depth', cc.Depth, 'Camera Depth (Gray Scale)'],
            ['sensor.camera.depth', cc.LogarithmicDepth, 'Camera Depth (Logarithmic Gray Scale)'],
            ['sensor.camera.semantic_segmentation', cc.Raw, 'Camera Semantic Segmentation (Raw)'],
            ['sensor.camera.semantic_segmentation', cc.CityScapesPalette,
             'Camera Semantic Segmentation (CityScapes Palette)'],
            ['sensor.lidar.ray_cast', None, 'Lidar (Ray-Cast)']]
        world = self._parent.get_world()
        bp_library = world.get_blueprint_library()
        for item in self.sensors:
            blp = bp_library.find(item[0])
            if item[0].startswith('sensor.camera'):
                blp.set_attribute('image_size_x', str(hud.dim[0]))
                blp.set_attribute('image_size_y', str(hud.dim[1]))
                if blp.has_attribute('gamma'):
                    blp.set_attribute('gamma', str(gamma_correction))
            elif item[0].startswith('sensor.lidar'):
                blp.set_attribute('range', '50')
            item.append(blp)
        self.index = None

    def toggle_camera(self):
        """Activate a camera"""
        self.transform_index = (self.transform_index + 1) % len(self._camera_transforms)
        self.set_sensor(self.index, notify=False, force_respawn=True)

    def set_sensor(self, index, notify=True, force_respawn=False):
        """Set a sensor"""
        index = index % len(self.sensors)
        needs_respawn = True if self.index is None else (
            force_respawn or (self.sensors[index][0] != self.sensors[self.index][0]))
        if needs_respawn:
            if self.sensor is not None:
                self.sensor.destroy()
                self.surface = None
            self.sensor = self._parent.get_world().spawn_actor(
                self.sensors[index][-1],
                self._camera_transforms[self.transform_index][0],
                attach_to=self._parent,
                attachment_type=self._camera_transforms[self.transform_index][1])

            # We need to pass the lambda a weak reference to
            # self to avoid circular reference.
            weak_self = weakref.ref(self)
            self.sensor.listen(lambda image: CameraManager._parse_image(weak_self, image))
        if notify:
            self.hud.notification(self.sensors[index][2])
        self.index = index

    def next_sensor(self):
        """Get the next sensor"""
        self.set_sensor(self.index + 1)

    def toggle_recording(self):
        """Toggle recording on or off"""
        self.recording = not self.recording
        self.hud.notification('Recording %s' % ('On' if self.recording else 'Off'))

    def render(self, display):
        """Render method"""
        if self.surface is not None:
            display.blit(self.surface, (0, 0))

    @staticmethod
    def _parse_image(weak_self, image):
        self = weak_self()
        if not self:
            return
        if self.sensors[self.index][0].startswith('sensor.lidar'):
            points = np.frombuffer(image.raw_data, dtype=np.dtype('f4'))
            points = np.reshape(points, (int(points.shape[0] / 3), 3))
            lidar_data = np.array(points[:, :2])
            lidar_data *= min(self.hud.dim) / 100.0
            lidar_data += (0.5 * self.hud.dim[0], 0.5 * self.hud.dim[1])
            lidar_data = np.fabs(lidar_data)  # pylint: disable=assignment-from-no-return
            lidar_data = lidar_data.astype(np.int32)
            lidar_data = np.reshape(lidar_data, (-1, 2))
            lidar_img_size = (self.hud.dim[0], self.hud.dim[1], 3)
            lidar_img = np.zeros(lidar_img_size)
            lidar_img[tuple(lidar_data.T)] = (255, 255, 255)
            self.surface = pygame.surfarray.make_surface(lidar_img)
        else:
            image.convert(self.sensors[self.index][1])
            array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
            array = np.reshape(array, (image.height, image.width, 4))
            array = array[:, :, :3]
            array = array[:, :, ::-1]
            self.surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
        if self.recording:
            image.save_to_disk('_out/%08d' % image.frame)

# ==============================================================================
# -- Game Loop ---------------------------------------------------------
# ==============================================================================


def game_loop(args):
    setting.io_calls = 0
    parts = os.path.splitext(__name__)
    module_name = parts[len(parts) - 2]
    print(module_name)
    """ Main loop for agent"""

    pygame.init()
    pygame.font.init()
    world = None
    tot_target_reached = 0
    num_min_waypoints = 21
    timeout = 60 #99999999.0

    try:
        # import setting
        from agents.navigation.behavior_agent import BehaviorAgent  # pylint: disable=import-error
        from agents.navigation.roaming_agent import RoamingAgent  # pylint: disable=import-error
        from agents.navigation.basic_agent import BasicAgent  # pylint: disable=import-error
    except IndexError:
        pass

    try:
        client = carla.Client(args.host, args.port)
        client.set_timeout(timeout)

        display = pygame.display.set_mode(
            (args.width, args.height),
            pygame.HWSURFACE | pygame.DOUBLEBUF)

        hud = HUD(args.width, args.height)
        world = World(client.get_world(), hud, args)
        controller = KeyboardControl(world)

        if args.agent == "Roaming":
            agent = RoamingAgent(world.player)
        elif args.agent == "Basic":
            agent = BasicAgent(world.player)
            spawn_point = world.map.get_spawn_points()[0]
            agent.set_destination((spawn_point.location.x,
                                   spawn_point.location.y,
                                   spawn_point.location.z))
        else:
            agent = BehaviorAgent(world.player, behavior=args.behavior)

        spawn_points = world.map.get_spawn_points()
        random.shuffle(spawn_points)

        if spawn_points[0].location != agent.vehicle.get_location():
            destination = spawn_points[0].location
        else:
            destination = spawn_points[1].location

        agent.set_destination(agent.vehicle.get_location(), destination, clean=True)

        speed_factor = 1
        update_freq = 0.1 / speed_factor

        weather = Weather(world.world.get_weather())

        elapsed_time = 0.0
        clock = pygame.time.Clock()
        counter = 1
        threshold = int(hud.simulation_time) + 20
        #cov = None
        # sys.setprofile(trace)
        path = '{}/path_{}/round_{}/{}_coverage/.coverage'.format(args.base_path, args.pathId,
                                                                                   args.round,
                                                                                   args.scenario
                                                                                   )
        while True:

            cov = coverage.Coverage(
                data_file=path,
                data_suffix='{}'.format(counter), branch=False,
                include=['*agent*', '*behavior_agent*', '*controller*',
                         '*local_planner_behavior*']) #'*automatic_control*',
            # CANBusSensor.weak_self.cov = self.cov

            cov.start()
            # tracker = setting.TrackCalls()
            clock.tick_busy_loop(60)
            if controller.parse_events():
                #row_list = hud.log[:-1]
                #save_records(row_list, args.pathId, args.round, args.scenario)
                return
            #first_loc = world.player.get_location()----------------> error
            # As soon as the server is ready continue!
            if not world.world.wait_for_tick(10.0):
                continue

            #first_loc = world.player.get_location()
            if args.agent == "Roaming" or args.agent == "Basic":
                if controller.parse_events():
                    return
                # as soon as the server is ready continue!
                world.world.wait_for_tick(10.0)

                world.tick(clock)
                world.render(display)
                pygame.display.flip()
                control = agent.run_step()
                control.manual_gear_shift = False
                world.player.apply_control(control)
            else:

                agent.update_information(world)
                #first_loc = world.player.get_location()
                world.tick(clock)
                world.render(display)
                pygame.display.flip()
                #first_loc = world.player.get_location()
                # Set new destination when target has been reached
                if len(agent.get_local_planner().waypoints_queue) < num_min_waypoints and args.loop:
                    agent.reroute(spawn_points)
                    tot_target_reached += 1
                    world.hud.notification("The target has been reached " +
                                           str(tot_target_reached) + " times.", seconds=4.0)

                elif len(world.world.get_actors().filter('walker.*')) == 0 or  int(hud.simulation_time) >= threshold: #or
                    cov.stop()
                    cov.save()
                    # tracker.save_data()
                    save_ticks(args.base_path, hud.log, args.pathId, args.round, args.scenario)
                    save_records(args.base_path, args.pathId, args.round, args.scenario, current_frame)
                    break

                speed_limit = world.player.get_speed_limit()
                agent.get_local_planner().set_speed(speed_limit)

                current_frame = CANBusSensor.weak_self._frame + 1
                CANBusSensor.coverage_path = current_frame
                control = agent.run_step()
                world.player.apply_control(control)
                # tracker.save_data()
                cov.stop()
                cov.save()
                save_records(args.base_path, args.pathId, args.round, args.scenario, current_frame)
                # if not os.path.exists('{}.{}'.format(path, current_frame)):
                #     os.rename('{}.{}'.format(path, counter), '{}.{}'.format(path, current_frame))
                # else:
                #     i = 1
                #     while True:
                #         if not os.path.exists('{}.{}-{}'.format(path, current_frame, i)):
                #             os.rename('{}.{}'.format(path, counter), '{}.{}-{}'.format(path, current_frame, i))
                #             break
                #         i += 1

                counter += 1
                elapsed_time += 1e-3 * clock.get_time()
                if elapsed_time > update_freq:
                    weather.tick(speed_factor * elapsed_time)
                    world.world.set_weather(weather.weather)
                    elapsed_time = 0.0


    finally:
        if world is not None:
            world.destroy()

        sys.path.append('C:/CARLA/scenario_runner-0.9.8')
        from srunner.scenariomanager.carla_data_provider import CarlaDataProvider
        CarlaDataProvider.clear_buffer()
        pygame.quit()


def trace(frame, event, arg):
    # if event == "call":
    print('-----------------------', event)
    filename = frame.f_code.co_filename
    if any(map(filename.__contains__, setting.suts)):
        lineno = frame.f_lineno
        method_name = frame.f_code.co_name
        setting.call_functions.append([filename, method_name, lineno])
    return trace

def traceit(frame, event, arg):
    # print('-----------------------',event)
    if event == "call" or event == "c_call":
        lineno = frame.f_lineno
        filename = frame.f_code.co_filename #frame.f_globals["__file__"]
        if (filename.endswith(".pyc") or
            filename.endswith(".pyo")):
            filename = filename[:-1]
        name = frame.f_code.co_name #frame.f_globals["__name__"]
        line = linecache.getline(filename, lineno)
        # print "%s:%s: %s" % (name, lineno, line.rstrip())
        setting.call_functions.append([name, lineno, line.rstrip()])
    return traceit

# import hunter
# hunter.trace(module='controller', action=hunter.CodePrinter)

def save_records(base_path, pathId, round, scenario, tick_no):
    # global trace_map, trace_record

    if setting.trace_record is None:
        print("----------------------------> ERROR:(       tick {} ---> no trace!".format(tick_no))
        return
    # sys.settrace(None)  # Turn off
    setting.trace_record.insert(0, ['file', 'branch', 'distance_true', 'distance_false', 'loop', 'ol', 'counter'])

    with open("{}/path_{}/round_{}/{}_trace/tick_{}.csv".format(base_path, pathId, round, scenario, tick_no), 'w',
              newline='') as file:
        writer = csv.writer(file)
        writer.writerows(setting.trace_record)

    # setting.call_functions.insert(0, ['filename', 'method_name', 'lineno'])
    # with open("C:/CARLA/experiment/path_{}/round_{}/{}_trace/tick_{}_cal_fucntions.csv".format(pathId, round, scenario, tick_no), 'w',
    #           newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(setting.call_functions)

    # print(setting.call_functions)

    setting.trace_map = {}
    setting.trace_record = []
    setting.io_calls = 0
    setting.call_functions = []


def save_ticks(base_path, row_list, pathId, round, scenario):
    # Akram Kalaee
    #row_list.insert(0, ['frame', 'timestamp', 'Collision', 'obstacle', 'coverage_path', 'Speed', 'ped-Speed', 'Location', 'ped-Location', 'Distance', 'weather',  'can_bus_data', 'road_id', 'lane_id', 'curvature'])
    row_list.insert(0, ['frame',  'timestamp', 'collision', 'obstacle', 'coverage_path',
                 'cloudiness', 'precipitation', 'precipitation_deposits', 'wind_intensity', 'sun_azimuth_angle',
                 'sun_altitude_angle', 'fog_density', 'fog_distance',
                 'wetness', 'start_distance', 'other_actor_target_velocity', 'other_actor_yaw', 'tire_friction', 'ego_location_x',
                 'ego_location_y', 'ego_location_z', 'ego_location_yaw', 'ego_velocity', 'road_id', 'lane_id', 'curvature',
                        'other_actor_location_x',
                        'other_actor_location_y', 'other_actor_location_z', 'linear_acceleration', 'torque_curve',
                        'steering_curve', 'steer_angle', 'lateral_speed', 'full_data'
                        ])
    # list_of_files = glob.glob('{}/*.csv'.format(latest_folder))
    # csv_file = max(list_of_files, key=os.path.getctime)
    with open("{}/path_{}/round_{}/{}.csv".format(base_path, pathId, round, scenario), 'w',
              newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

    # if row_list:
    #     with open(r"E:\members\kalaee\simulators\working\experiment\path_0\round_1\test.txt", 'w') as file:
    #         file.write("hi")
    #         file.close()


# ==============================================================================
# -- main() --------------------------------------------------------------
# ==============================================================================

def main():

    argparser = argparse.ArgumentParser(
        description='CARLA Automatic Control Client')
    argparser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='debug',
        help='Print debug information')
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    argparser.add_argument(
        '--res',
        metavar='WIDTHxHEIGHT',
        default='1280x720',
        help='Window resolution (default: 1280x720)')
    argparser.add_argument(
        '--filter',
        metavar='PATTERN',
        default='vehicle.*',
        help='Actor filter (default: "vehicle.*")')
    argparser.add_argument(
        '--gamma',
        default=2.2,
        type=float,
        help='Gamma correction of the camera (default: 2.2)')
    argparser.add_argument(
        '-l', '--loop',
        action='store_true',
        dest='loop',
        help='Sets a new random destination upon reaching the previous one (default: False)')
    argparser.add_argument(
        '-b', '--behavior', type=str,
        choices=["cautious", "normal", "aggressive"],
        help='Choose one of the possible agent behaviors (default: normal) ',
        default='normal')
    argparser.add_argument("-a", "--agent", type=str,
                           choices=["Behavior", "Roaming", "Basic"],
                           help="select which agent to run",
                           default="Behavior")
    argparser.add_argument(
        '-s', '--seed',
        help='Set seed for repeating executions (default: None)',
        default=None,
        type=int)
    # Added by Akram Kalaee###################
    argparser.add_argument('--pathId', default="1",
                           help='Set the pathId for test scenario generation')
    argparser.add_argument('--round', default="1",
                           help='Set the round for test scenario generation')
    argparser.add_argument('--base_path', default="C:/CARLA/experiment",
                        help='Set the pathId for test scenario generation')
    #######################################
    argparser.add_argument(
        '--scenario',
        help='Name of the scenario to be executed. Use the preposition \'group:\' to run all scenarios of one class, e.g. ControlLoss or FollowLeadingVehicle')

    args = argparser.parse_args()

    args.width, args.height = [int(x) for x in args.res.split('x')]

    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)

    logging.info('listening to server %s:%s', args.host, args.port)

    print(__doc__)

    try:
        game_loop(args)

    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')

def automatic_controller_start(parameters):
    argparser = argparse.ArgumentParser(
        description='CARLA Automatic Control Client')
    argparser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='debug',
        help='Print debug information')
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    argparser.add_argument(
        '--res',
        metavar='WIDTHxHEIGHT',
        default='1280x720',
        help='Window resolution (default: 1280x720)')
    argparser.add_argument(
        '--filter',
        metavar='PATTERN',
        default='vehicle.*',
        help='Actor filter (default: "vehicle.*")')
    argparser.add_argument(
        '--gamma',
        default=2.2,
        type=float,
        help='Gamma correction of the camera (default: 2.2)')
    argparser.add_argument(
        '-l', '--loop',
        action='store_true',
        dest='loop',
        help='Sets a new random destination upon reaching the previous one (default: False)')
    argparser.add_argument(
        '-b', '--behavior', type=str,
        choices=["cautious", "normal", "aggressive"],
        help='Choose one of the possible agent behaviors (default: normal) ',
        default='normal')
    argparser.add_argument("-a", "--agent", type=str,
                           choices=["Behavior", "Roaming", "Basic"],
                           help="select which agent to run",
                           default="Behavior")
    argparser.add_argument(
        '-s', '--seed',
        help='Set seed for repeating executions (default: None)',
        default=None,
        type=int)
    # Added by Akram Kalaee###################
    argparser.add_argument('--pathId', default="1",
                           help='Set the pathId for test scenario generation')
    argparser.add_argument('--round', default="1",
                           help='Set the round for test scenario generation')
    #######################################
    argparser.add_argument(
        '--scenario',
        help='Name of the scenario to be executed. Use the preposition \'group:\' to run all scenarios of one class, e.g. ControlLoss or FollowLeadingVehicle')

    args = argparser.parse_args(parameters)

    args.width, args.height = [int(x) for x in args.res.split('x')]

    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)

    logging.info('listening to server %s:%s', args.host, args.port)

    print(__doc__)

    try:
        time.sleep(5)
        game_loop(args)

    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')

def get_curvature(host_waypoint, route_distance):
        previous_waypoint = host_waypoint.previous(route_distance)[0]
        next_waypoint = host_waypoint.next(route_distance)[0]
        _transform = next_waypoint.transform
        _location, _rotation  = _transform.location, _transform.rotation
        x1, y1 = _location.x, _location.y
        yaw1 = _rotation.yaw

        _transform = previous_waypoint.transform
        _location, _rotation  = _transform.location, _transform.rotation
        x2, y2 = _location.x, _location.y
        yaw2 = _rotation.yaw

        c = 2*math.sin(math.radians((yaw1-yaw2)/2)) / math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return c

def clamp(value, minimum=0.0, maximum=100.0):
    return max(minimum, min(value, maximum))


class Sun(object):
    def __init__(self, azimuth, altitude):
        self.azimuth = azimuth
        self.altitude = altitude
        self._t = 0.0

    def tick(self, delta_seconds):
        self._t += 0.008 * delta_seconds
        self._t %= 2.0 * math.pi
        self.azimuth += 0.25 * delta_seconds
        self.azimuth %= 360.0
        self.altitude = (70 * math.sin(self._t)) - 20

    def __str__(self):
        return 'Sun(alt: %.2f, azm: %.2f)' % (self.altitude, self.azimuth)


class Storm(object):
    def __init__(self, precipitation):
        self._t = precipitation if precipitation > 0.0 else -50.0
        self._increasing = True
        self.clouds = 0.0
        self.rain = 0.0
        self.wetness = 0.0
        self.puddles = 0.0
        self.wind = 0.0
        self.fog = 0.0

    def tick(self, delta_seconds):
        delta = (1.3 if self._increasing else -1.3) * delta_seconds
        self._t = clamp(delta + self._t, -250.0, 100.0)
        self.clouds = clamp(self._t + 40.0, 0.0, 90.0)
        self.rain = clamp(self._t, 0.0, 80.0)
        delay = -10.0 if self._increasing else 90.0
        self.puddles = clamp(self._t + delay, 0.0, 85.0)
        self.wetness = clamp(self._t * 5, 0.0, 100.0)
        self.wind = 5.0 if self.clouds <= 20 else 90 if self.clouds >= 70 else 40
        self.fog = clamp(self._t - 10, 0.0, 30.0)
        if self._t == -250.0:
            self._increasing = True
        if self._t == 100.0:
            self._increasing = False

    def __str__(self):
        return 'Storm(clouds=%d%%, rain=%d%%, wind=%d%%)' % (self.clouds, self.rain, self.wind)


class Weather(object):
    def __init__(self, weather):
        self.weather = weather
        self._sun = Sun(weather.sun_azimuth_angle, weather.sun_altitude_angle)
        self._storm = Storm(weather.precipitation)

    def tick(self, delta_seconds):
        self._sun.tick(delta_seconds)
        self._storm.tick(delta_seconds)
        self.weather.cloudiness = self._storm.clouds
        self.weather.precipitation = self._storm.rain
        self.weather.precipitation_deposits = self._storm.puddles
        self.weather.wind_intensity = self._storm.wind
        self.weather.fog_density = self._storm.fog
        self.weather.wetness = self._storm.wetness
        self.weather.sun_azimuth_angle = self._sun.azimuth
        self.weather.sun_altitude_angle = self._sun.altitude

    def __str__(self):
        return '%s %s' % (self._sun, self._storm)

# global trace_map , trace_record
# trace_map = {}
# trace_record = []
if __name__ == '__main__':

    main()