#version: 13-1
#configurable parameters are including:

#param1-    Cloudiness: [0, 100]
#param2-    Precipitation: [0, 100]
#param3-    precipitation_deposits: [0, 100]
#param4-    wind_intensity: [0, 100]
#param5-    sun_azimuth_angle: [0, 360]
#param6-    sun_altitude_angle: [-90, 90]
#param7-    fog_density:[0,1]
#param8-    fog_distance: [0, 150]:
#param9-    wetness: [0, 10]

#param10-   start_distance:[5, 15]
#param11-_  other_actor_target_velocity:[1, 18]
#param12-_  walker_yaw:[270, 320]

#param13-   friction: [0.00001, 1]

import token
import tokenize
import collections
import concurrent
import csv
import socket
import math
import win32serviceutil
import seaborn as sns
from psutil import process_iter
from signal import SIGTERM  # or SIGKILL
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from scenario_runner import srunner_start
from pathlib import Path
import logging
import signal
from datetime import datetime, timedelta
import pickle
import glob
import os
from matplotlib import cm
import sys
import subprocess
import time
import re
import numpy as np
import coverage
import psutil
from IPython.core.display import display
from pandas.errors import EmptyDataError
from platypus.core import nondominated_sort
from sklearn.metrics import f1_score, roc_curve, precision_recall_curve
from sklearn.neighbors import NearestNeighbors
import sklearn
from platypus import GAOperator, SBX, PM, Archive, Generator, Solution, Variator, clip, random, EPSILON, copy, Mutation
from platypus.core import TerminationCondition, MaxTime
from platypus.problems import Problem
from platypus.algorithms import NSGAII
from platypus.types import Real, Integer
import xml.etree.ElementTree as ET
import vkbeautify as vkb
import pandas as pd
import itertools
import carla
from wrapt_timeout_decorator import *
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.exceptions import NotFittedError
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
import sklearn
from sklearn.tree import DecisionTreeClassifier
from skrules import SkopeRules
import coverage.coverage_to_vector
import scipy.spatial.distance as dist
from numpy.linalg import norm
import matplotlib.pyplot as plt
from sklearn.externals.six import StringIO
from IPython.display import Image
from pydot import graph_from_dot_data
from sklearn import tree
from contextlib import closing
import port_for
from subprocess import call, PIPE, check_output, STDOUT
from automatic_control import HUD, automatic_controller_start
from scenario_runner import ScenarioRunner
from ml_models.decision_tree import extract_rules
import coverage.coverage_compare as coverage_compare

############################### parameters ###############################
host = '127.0.0.1'
town = "Town05"
filter = "model3"
single_road = True
target_road = 1
_timeout = 100000.0
max_pop_size = 20
eps = 0.001
static_params = 14
io_var_id = 13
constraint_var_id = 18
scenario_name = "DynamicObjectCrossing"
scenario_config_file = "ObjectCrossing"
initial_roads = [
    (46, [-1, -2], -0.024660983495301714, -90.04034614562985, -99.981461, -53.625210, 1)
    ,
    (20, [-1], -0.007141292105148509, 123.79999542236325, 51.215088, 151.528366, 2),
    (19, [-1], -0.003531825385624573, 44.23333459719494, 44.770233, 151.504562, 3),
    (38, [2, 3, 4], 0.009881948697975276, 99.58999755978581, 58.372219, 197.033661, 4),
    (34, [2, 3, 4], 0.009901544057336559, 200.9606357496336, 69.634476, 196.740341, 5),
    (30, [-1, -2], 0.021958071182160147, 55.88784978376137, 41.828674, 106.616150, 6)
]
initial_domain = [(0, 1, 0), (0, -1, 100), (1, 1, 0), (1, -1, 100), (2, 1, 0), (2, -1, 100), (3, 1, 0), (3, -1, 100),
                  (4, 1, 0), (4, -1, 360), (5, 1, -90), (5, -1, 90), (6, 1, 0), (6, -1, 1),(7, 1, 0), (7, -1, 150),(8, 1, 0), (8, -1, 10),
                    (9, 1, 5), (9, -1, 15),(10, 1, 1), (10, -1, 18),(11, 1, 270), (11, -1, 320),(12, 1, 0.00001), (12, -1, 1),(13, 1, 0), (13, -1, 25),

                  ((14, 1, -99.98146057128906), (14, -1, -53.78223419189453), (15, 1, -138.61570739746094),
                   (15, -1, -102.61880493164062), (16, 1, 2.055450439453125), (16, -1, 2.055450439453125),
                   (17, 1, 0.44256171584129333), (17, -1, 85.32264709472656), (18, 1, 1), (18, -1, 1))
    ,
                  ((14, 1, 51.7147102355957), (14, -1, 151.5106964111328), (15, 1, 89.84903717041016),
                   (15, -1, 142.34896850585938), (16, 1, 2.038604736328125), (16, -1, 2.038604736328125),
                   (17, 1, -177.7715606689453), (17, -1, 182.14039611816406), (18, 1, 2), (18, -1, 2))
    ,
                  ((14, 1, 44.770233154296875), (14, -1, 151.5041046142578), (15, 1, -146.0388946533203),
                   (15, -1, -17.998546600341797), (16, 1, 2.038604736328125), (16, -1, 2.038604736328125),
                   (17, 1, -1.2122206687927246), (17, -1, 89.94741821289062), (18, 1, 3), (18, -1, 3))
    ,
                  ((14, 1, 58.37221908569336), (14, -1, 197.03366088867188), (15, 1, 13.69448184967041),
                   (15, -1, 195.0659942626953), (16, 1, 2.0), (16, -1, 2.0), (17, 1, 90.66463470458984),
                   (17, -1, 180.28781127929688), (18, 1, 4), (18, -1, 4))
    ,
                  ((14, 1, 70.10478973388672), (14, -1, 196.7344970703125), (15, 1, -193.8758544921875),
                   (15, -1, -11.026947975158691), (16, 1, 2.0), (16, -1, 2.0), (17, 1, -0.2217559814453125),
                   (17, -1, 359.757080078125), (18, 1, 5), (18, -1, 5))
    ,
                  ((14, 1, 41.82867431640625), (14, -1, 106.61614990234375), (15, 1, 12.991072654724121),
                   (15, -1, 95.55668640136719), (16, 1, 2.0), (16, -1, 2.0), (17, 1, -89.30083465576172),
                   (17, -1, -0.41618767380714417), (18, 1, 6), (18, -1, 6))
                  ]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.getLogger('matplotlib').setLevel(logging.WARNING)
output_file_handler = logging.FileHandler("E:\members\kalaee\experiment\path_0\log.log")
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(output_file_handler)
logger.addHandler(stdout_handler)


############################### carla functions ###############################
def get_spawnpoint(world, road_id, lane_id, start, end, distance=0.5):
    waypoints = world.get_map().generate_waypoints(distance=distance)
    filtered_waypoints = []
    for waypoint in waypoints:
        if waypoint.road_id == road_id and waypoint.lane_type == carla.LaneType.Driving and waypoint.lane_id in lane_id and waypoint.transform.location.x >= start and waypoint.transform.location.x <= end:  # :
            filtered_waypoints.append(waypoint)

    return filtered_waypoints

def spawn_hero(world, filter, spawn_point, road_id):
    for a in world.get_actors().filter("vehicle*"):
        if a.is_alive:
            a.destroy()

    lb = -1
    ub = -1
    lane_id = []
    for i in range(len(initial_roads)):
        if initial_roads[i][0] == road_id:
            lb = initial_roads[i][4]
            ub = initial_roads[i][5]
            lane_id = initial_roads[i][1]
            break
    if spawn_point.lane_type != carla.LaneType.Driving or spawn_point.road_id != road_id or spawn_point.lane_id not in lane_id or spawn_point.transform.location.x < lb or spawn_point.transform.location.x > ub:
         return None

    vehicle_blueprint = world.get_blueprint_library().filter('model3')[0]

    try:
        hero_actor = world.try_spawn_actor(vehicle_blueprint, spawn_point.transform)
    except:
        return None
    return hero_actor


############################### problem: Automatic Braking System (ABS) #######
class ABS(Problem):
    def __init__(self, domains, roads, filter, pop_size, round, scenario_number, target_path, target_path_id, sample_path, io_lines, delta, base_path, class_name, init_pop=[]):
        super(ABS, self).__init__(19, 4, static_params, constraint_var_id)
        self.static_params = static_params
        self.constraint_var_id = constraint_var_id
        self.all_static_params = static_params * 2
        self.all_params = len(domains)
        self.dynamic_params = len(initial_roads)

        self.types[0] = Real(domains[0][2], domains[1][2])
        self.types[1] = Real(domains[2][2], domains[3][2])
        self.types[2] = Real(domains[4][2], domains[5][2])
        self.types[3] = Real(domains[6][2], domains[7][2])
        self.types[4] = Real(domains[8][2], domains[9][2])
        self.types[5] = Real(domains[10][2], domains[11][2])
        self.types[6] = Real(domains[12][2], domains[13][2])
        self.types[7] = Real(domains[14][2], domains[15][2])
        self.types[8] = Real(domains[16][2], domains[17][2])

        self.types[9] = Real(domains[18][2], domains[19][2])
        self.types[10] = Real(domains[20][2], domains[21][2])
        self.types[11] = Real(domains[22][2], domains[23][2])
        self.types[12] = Real(domains[24][2], domains[25][2])

        _int2 = Integer(-1, 1000)
        self.types[13] = _int2

        types_var14 = []
        types_var15 = []
        types_var16 = []
        types_var17 = []

        for i in range(len(roads)):
            types_var14.append(Real(domains[self.all_static_params + i][0][2], domains[self.all_static_params + i][1][2]))
            types_var15.append(Real(domains[self.all_static_params + i][2][2], domains[self.all_static_params + i][3][2]))
            types_var16.append(Real(domains[self.all_static_params + i][4][2], domains[self.all_static_params + i][5][2]))
            types_var17.append(Real(domains[self.all_static_params + i][6][2], domains[self.all_static_params + i][7][2]))

        self.types[14] = types_var14
        self.types[15] = types_var15
        self.types[16] = types_var16
        self.types[17] = types_var17

        _int1 = Integer(1, self.dynamic_params)
        self.types[18] = _int1

        self.domains = domains
        self.roads = roads
        self.roads_index = [road[len(road) - 1] for road in self.roads]
        self.filter = filter
        self.round = round
        self.scenario_number = scenario_number
        self.pop_size = pop_size
        self.target_path = target_path
        self.target_path_id = target_path_id
        self.directions[:] = [Problem.MINIMIZE, Problem.MINIMIZE, Problem.MINIMIZE, Problem.MAXIMIZE] #approach_level, branch_distance, min_distance, speed
        self.init_pop = init_pop
        self.target_coverage_file = target_path
        self.io_var_id = io_var_id
        self.sample_path = sample_path
        self.target_edge_list = self.get_edges(self.target_coverage_file)
        self.target_map = self.get_target_map(self.target_coverage_file)
        self.target_slices = self.get_target_slices(self.target_coverage_file)
        self.io_lines = io_lines
        self.delta = delta
        self.base_path = base_path
        self.class_name = class_name

    def find_IO_calls(self, coverage_report):
        dict = coverage_compare.convert_coverage_report_to_dict(coverage_report)
        result = {}
        calls_no = 0
        for fname in dict.keys():
            missing = dict[fname][1]
            interval_statements = re.compile("[\d]+-[\d]+").findall(",".join(missing))
            missing = ",".join(missing).strip().split(',')
            statements = [int(x) for x in missing if x.strip().isdigit()]

            io_lines = self.io_lines.get(fname)
            called_io = []

            for io in io_lines:
                is_missed = False
                if io not in statements:
                    for interval in interval_statements:
                        list_interval = interval.split("-")
                        start = int(list_interval[0])
                        end = int(list_interval[1])
                        if io >= start and io <= end:
                            is_missed = True
                            break
                else:
                    is_missed = True

                if not is_missed:
                    called_io.append(io)
                    calls_no += 1

            result[fname] = called_io
        return calls_no

    def get_edges(self, coverage):
        path = []
        target_trace_file = pd.read_csv(coverage)
        target_trace_file['ol'] = target_trace_file['ol'].apply(eval)

        file_name_1 = target_trace_file.iloc[:, 0]
        branch_no_1 = target_trace_file.iloc[:, 1]
        distance_true = target_trace_file.iloc[:, 2]
        distance_false = target_trace_file.iloc[:, 3]
        ol = target_trace_file.iloc[:, 5]

        target_path = list(zip(file_name_1, branch_no_1, distance_true, distance_false, ol))
        target_nrows = len(file_name_1)

        start = None
        for idx1 in range(target_nrows):
            start_node = target_path[idx1]
            start = (start_node[0], start_node[1])
            next = idx1 + 1
            if next < target_nrows:
                end_node = target_path[next]
                end = (end_node[0], end_node[1])
                path.append((start, end, start_node[2], start_node[3], start_node[4]))

        path.append((start, None, start_node[2], start_node[3], start_node[4]))
        return path

    def get_target_map(self, coverage):
        map = []
        target_trace_file = pd.read_csv(coverage)

        file_name_1 = target_trace_file.iloc[:, 0]
        branch_no_1 = target_trace_file.iloc[:, 1]
        distance_true = target_trace_file.iloc[:, 2]
        distance_false = target_trace_file.iloc[:, 3]

        target_path = list(zip(file_name_1, branch_no_1, distance_true, distance_false))
        target_nrows = len(file_name_1)

        for idx1 in range(target_nrows):
            start_node = target_path[idx1]
            start = (start_node[0], start_node[1])

            if start_node[2] == start_node[2]:
                if start_node[2] != 0:
                    branch = False
                elif start_node[3] != 0:
                    branch = True
                else:
                    raise Exception
            else:
                branch = None

            next = idx1 + 1
            if next < target_nrows:
                end_node = target_path[next]
                end = (end_node[0], end_node[1])
                map.append((start, end, branch))

        map.append((start, None, branch))
        return map

    def get_target_slices(self, coverage_file):
        trace_file = pd.read_csv(coverage_file)
        trace_file['ol'] = trace_file['ol'].apply(eval)
        nrows = trace_file.shape[0]
        start = 0
        end = 0
        slices = []
        for row_no in range(1, nrows):
            if trace_file.iloc[start, 0] == trace_file.iloc[row_no, 0]:
                if trace_file.iloc[start, 4] == trace_file.iloc[row_no, 4]:
                    if trace_file.iloc[start, 4] == 0:
                        end = row_no
                    else:
                        if trace_file.iloc[start, 6] == trace_file.iloc[row_no, 6]:
                            end = row_no
                        else:
                            rows = trace_file.iloc[start:end + 1, :].values
                            slices.append(rows)
                            start = row_no
                            end = start
                else:
                    rows = trace_file.iloc[start:end + 1, :].values
                    slices.append(rows)
                    start = row_no
                    end = start
            else:
                rows = trace_file.iloc[start:end + 1, :].values
                slices.append(rows)
                start = row_no
                end = start

        rows = trace_file.iloc[start:end + 1, :].values
        slices.append(rows)

        return slices

    def evaluate(self, individual):
        min_fitness = sys.float_info.max
        positive_delta_active_samples_no = 0
        evaluation_number = 0
        feasible_samples = []
        test_data = []
        label = -1
        risk = -1
        _class = -1
        IO_no = -1
        min_distance = 1000
        speed = -1
        approach_level = sys.maxsize
        branch_distance = sys.float_info.max

        domain_part1 = self.domains[0:2 * (self.io_var_id + 1)]
        for i in np.arange(len(domain_part1)):
            if individual.variables[i] > domain_part1[2 * i + 1][2]:
                individual.variables[i] = domain_part1[2 * i + 1][2]
            if individual.variables[i] < domain_part1[2 * i][2]:
                individual.variables[i] = domain_part1[2 * i][2]
            if 2 * i + 2 == len(domain_part1):
                break

        idx = 0
        domain_part2 = list(self.domains[2 * self.io_var_id + 2 + idx])
        for i in range(len(domain_part2)):
            if individual.variables[i] > domain_part2[2 * i + 1][2]:
                individual.variables[i] = domain_part2[2 * i + 1][2]
            if individual.variables[i] < domain_part2[2 * i][2]:
                individual.variables[i] = domain_part2[2 * i][2]
            if 2 * i + 1 == len(domain_part2) - 1:
                break


        variables = individual.variables[:]
        scenario_id = self.convert_to_xml(variables)
        individual.id = self.scenario_number
        logger.debug(".......................................................................")
        logger.debug("path_id: {}, scenario_id: {}".format(self.target_path_id, scenario_id))

        while True:
            try:
                free_port, client, world = self.load_carla()
                break
            except BaseException as e:
                "try agin for a new port..."
                print(e)
                "waite..."

        try:
            print("starting srunner ...")
            srunner_args = ["--port", str(free_port), "--scenario", str(scenario_id), "--round", str(self.round), "--pathId",str(self.target_path_id), "--timeout", str(_timeout), "--reloadWorld" , "--waitForEgo"] #, "--debug" ]
            srunner_start(srunner_args, client, world, self.base_path)
            print("srunner killed")

            self.kill_port(free_port)
        except:
            IO_no = IO_no
            individual.objectives[:] = [approach_level, branch_distance, min_distance, speed]
            individual.variables[self.io_var_id] = IO_no
            index = 0

            logger.debug("min_distance: {} , speed: {}, fitness: {}, io#: {}  in time step: {}".format(
                min_distance, speed, min_fitness, IO_no, index))

            self.scenario_number += 1

            return

        try:
            scenario_output_file = pd.read_csv(
                r'{}\path_{}\round_{}\{}.csv'.format(self.base_path,
                    self.target_path_id, self.round,
                    scenario_id))
        except EmptyDataError:
            scenario_output_file = pd.DataFrame()

        if scenario_output_file.empty or len(scenario_output_file.values) <10:  # frames data
            IO_no = IO_no
            individual.objectives[:] = [approach_level, branch_distance, min_distance, speed]
            individual.variables[self.io_var_id] = IO_no
            index = 0

            logger.debug("min_distance: {} , speed: {}, fitness: {}, io#: {}  in time step: {}".format(
                min_distance, speed, min_fitness, IO_no, index))

            self.scenario_number += 1

            return

        d = scenario_output_file.iloc[:, 14].values  # distance
        min_distance = min(d)
        if min_distance is np.nan:
            min_distance = 1000

        collisions = scenario_output_file.iloc[:, 2].values #collision
        walker_collisions = [(i, x) for i, x in enumerate(collisions) if
                             re.compile("Pedestrian").search(str(x)) != None]

        threshold_index = -1 #as a window for unsafe scenarios
        if len(walker_collisions) > 0:
            index = walker_collisions[0][
                0]
            speed = scenario_output_file.iloc[index, 22]  # The vehicle's speed at the time of the collision

            braking_distance = 4  # for normal behaviors
            dmin = braking_distance
            d = scenario_output_file.iloc[:index, 14].values  # distance
            v = scenario_output_file.iloc[:index, 22].values  # speed
            no = len(v)
            distance = [np.abs(d[i] - dmin) for i in range(no)]
            ttc = [distance[i] / v[i] if v[i] != 0 else distance[i] / eps for i in range(no)]
            ttc_v = [ttc[i] + v[i] for i in range(no)]
            danger = ttc_v[-1]
            for i in reversed(range(no-1)):
                if ttc_v[i] < 0.5 * danger:
                    break
                else:
                    threshold_index = i

            if threshold_index == -1:
                threshold_index = index
            risk = 1
        else:
            speed = -1
            min_index = np.where(d == min_distance)[0]
            if len(min_index) == 0:
                index = 0
            else:
                index = min_index[0]

        index = index + 1
        frames = (scenario_output_file.iloc[:, 4].values)[0:index]
        frames_id = [(i, int(id)) for i, id in enumerate(frames) if id == id]
        coverage_folder = "{}/path_{}/round_{}/".format(self.base_path, self.target_path_id, self.round)

        best = [min_fitness, -1, (-1, -1), -1, sys.maxsize, sys.float_info.max]
        row_lists = []

        curvature_id = variables[self.constraint_var_id]
        counter = 1
        _risk = risk
        for item in frames_id:
            row_no = item[0]
            frame_id = item[1]

            if _risk == 1 and row_no >= threshold_index:
                frame_risk = 1
            else:
                frame_risk = -1

            road_id = scenario_output_file.loc[:, "road_id"].values[row_no]
            lane_id = scenario_output_file.loc[:, "lane_id"].values[row_no]

            if not(road_id == self.roads[curvature_id-1][0] and lane_id in self.roads[curvature_id-1][1]):
                print('rejected frame-> road/lane:',road_id,"/", lane_id,"  curvature_id:", curvature_id)
                continue

            evaluation_number += 1
            try:
                pattern = "{}/{}_trace/tick_{}.csv".format(coverage_folder, scenario_id, frame_id)
                coverage_file = glob.glob(pattern)[0]
            except:
                pattern = "{}/{}_trace/tick_{}*.csv".format(coverage_folder, scenario_id, frame_id)
                print('warning for {}-> the file is rewriting'.format(pattern))
                coverage_file = glob.glob(pattern)[0]

            current_edge_list = self.get_edges(coverage_file)
            branch_distance, approach_level = self.calculate_fitness(self.target_map, self.target_slices,
                                                                     self.target_edge_list, current_edge_list)

            if approach_level == 0 and branch_distance <= 0:
                label = 1  # feasible config
            else:
                label = -1  # infeasible config

            h_branch_distance = math.fabs(branch_distance + self.delta) - self.delta

            call_pattern = "{}/{}_coverage/.coverage.{}".format(coverage_folder, scenario_id,counter)
            call_file = glob.glob(call_pattern)[0]
            cov = coverage.Coverage(data_file=call_file)
            cov.load()
            statement_coverage = "{}/{}_coverage/.coverage.{}.txt".format(coverage_folder, scenario_id, counter)
            try:
                with open(statement_coverage, "w") as f:
                    cov.report(show_missing=True, file=f)
            except:
                IO_no = -1
                individual.objectives[:] = [approach_level, branch_distance, min_distance, speed]
                individual.variables[self.io_var_id] = IO_no
                index = 0
                min_distance = 1000
                speed = -1

                logger.debug("min_distance: {} , speed: {}, fitness: {}, io#: {}  in time step: {}".format(
                    min_distance, speed, min_fitness, IO_no, index))

                self.scenario_number += 1
                evaluation_number = 1
                return

            IO_no = self.find_IO_calls(statement_coverage)
            counter += 1

            #update the coverage file name
            if label == 1 and h_branch_distance <= 0:  # negative delta active point
                updated_path = r"{}\path_{}\round_{}\{}_trace\tick_{}_io_{}_target.csv".format(self.base_path,
                    self.target_path_id, self.round, scenario_id, frame_id, IO_no)
                h_branch_distance = 0
            else:
                if approach_level == 0 and 0 < branch_distance <= 2* self.delta: # positive delta active point
                    positive_delta_active_samples_no += 1
                updated_path = r"{}\path_{}\round_{}\{}_trace\tick_{}_io_{}.csv".format(self.base_path,
                    self.target_path_id, self.round, scenario_id, frame_id, IO_no)

            os.rename(coverage_file, updated_path)

            normalized_branch_distance = math.tanh(h_branch_distance)
            fitness = approach_level + normalized_branch_distance

            #save feasible samples
            if label == 1:  # negative delta active point
                feasible_samples.append((fitness, frame_risk))

            c1= 'b' if h_branch_distance <= 0 or (approach_level == 0 and 0 < branch_distance <= 2* self.delta) else 'nb'
            c2= 'target' if label == 1 else 'non_target'
            c3= 'unsafe' if frame_risk == 1 else 'safe'
            _class = list.index(self.class_name, '{}_{}_{}'.format(c1, c2, c3))

            boundary_variables = scenario_output_file.iloc[row_no, :-1].values
            row_list = []
            row_list.extend(boundary_variables)
            distance = row_list[14]
            v = row_list[22]
            danger = distance / v if v != 0 else distance / eps

            logger.debug(
                'frame_id: {}  danger: {}   branch_distance: {}    h_branch_distance: {}    approach_level: {}    fitness: {}   Io#: {}'.format(
                    frame_id, danger, branch_distance, h_branch_distance, approach_level, fitness, IO_no))
            row_list.extend([curvature_id, fitness, label, frame_risk, branch_distance, normalized_branch_distance, approach_level, IO_no, h_branch_distance, _class,  scenario_id, danger])
            row_lists.append(row_list)

            #update best
            if min_fitness > fitness:
                min_fitness = fitness
                best = [fitness, IO_no, item, label, approach_level, branch_distance]

        # update solution
        boundary_distance = best[0]
        IO_no = best[1]
        row_no = best[2][0]
        frame_id = best[2][1]
        label = best[3]
        approach_level = best[4]
        branch_distance = best[5]
        if len(row_lists) > 0:
            test_data = scenario_output_file.iloc[row_no, 5:22].values
            with open(self.sample_path, 'a', newline='') as file: #append to sample_file
                writer = csv.writer(file)
                writer.writerows(row_lists)

            file.close()
            print('Archive the sample set done!')

        individual.objectives[:] = [approach_level, branch_distance, min_distance, speed]
        individual.variables[self.io_var_id] = IO_no

        #update best frame
        if IO_no != -1:
            traversed_path = r"{}\path_{}\round_{}\{}_trace\tick_{}_io_{}.csv".format(self.base_path,
                self.target_path_id, self.round, scenario_id, frame_id, IO_no)
            updated_path = r"{}\path_{}\round_{}\{}_trace\tick_{}_io_{}_best.csv".format(self.base_path,
                self.target_path_id, self.round, scenario_id, frame_id, IO_no)
            try:
                os.rename(traversed_path, updated_path)
            except:
                pass
        else:
            print('io = -1')

        #update io number of the xml file
        xml_file_path = "C:/CARLA/scenario_runner-0.9.8/srunner/examples/{}.xml".format(
            scenario_config_file)

        root = ET.parse(xml_file_path).getroot()
        last_match = root.findall('scenario[@name="{}"]'.format(scenario_id))[-1]
        path_elem = last_match.find('path')
        path_elem.set('io_no', str(IO_no))

        data = ET.tostring(root, encoding="unicode")

        with open(xml_file_path, 'w') as f:
            f.write(data)

        #log the results
        logger.debug(
            "min_distance: {} , speed: {}, fitness: {}, io#: {}  in time step: {}".format(min_distance, speed,
                                                                                                  boundary_distance,
                                                                                                  IO_no, frame_id))
        self.scenario_number += 1


    def calculate_fitness(self, target_map, target_slices, target_edge_list, current_edge_list):
        fitness = 0
        approach_level = 0
        n = len(current_edge_list)
        index2 = 0
        counter = 0
        distance = []


        for slice in target_slices:
            index1 = index2
            index2 = index1 + len(slice)
            slice_edge_list = list(zip(target_edge_list[index1: index2], target_map[index1: index2]))
            rows = []
            target_map_rows = []

            for edge1, target_map_edge1 in slice_edge_list:
                if counter < n:
                    edge2 = current_edge_list[counter]
                    last_edge2 = edge2

                    while (edge1[0] != edge2[0] or edge1[1] != edge2[1]) and counter < n - 1:
                        counter += 1
                        edge2 = current_edge_list[counter]
                        last_edge2 = edge2

                    if edge1[0] != last_edge2[0] or edge1[1] != last_edge2[1]:
                        approach_level += 1
                    else:
                        rows.append(last_edge2)
                        target_map_rows.append(target_map_edge1)
                else:
                    break

            if rows and target_map_rows:
                distance.append(self.constraint_violation(0, rows, target_map_rows))

            if counter == n:
                break

        lst = np.array(distance, dtype=np.float64)
        if lst.size != 0:
            branch_distance = np.nanmax(lst)
        else:
            branch_distance = sys.float_info.max

        return branch_distance, approach_level

    def constraint_violation(self, idx1, rows, target_map):
        row = rows[idx1]
        target = target_map[idx1]
        ol = row[4]
        idx2 = idx1 + 1

        if idx2 >= len(rows):
            next_row = None
        else:
            next_row = rows[idx2]

        if target[2] != None:
            if target[2]:
                if row[3] != 0:  # false_distance column
                    value1 = -row[3]
                elif row[2] != 0:
                    value1 = row[2]  # true_distance column
                else:
                    value1 = 0

            else:
                if row[2] != 0:  # true_distance column
                    value1 = -row[2]
                elif row[3] != 0:
                    value1 = row[3]  # false_distance column
                else:
                    value1 = 0
        else:
            value1 = None

        if next_row is None:
            return value1
        else:
            if len(ol) == 1 and ol[0] == '#':
                value2 = self.constraint_violation(idx2, rows, target_map)
                lst = np.array([value1, value2], dtype=np.float64)
                return np.nanmax(lst)
            else:
                nol = len(ol)
                for idx in range(1, nol):
                    list1 = [x.strip() for x in ol[idx].split(',')]
                    op = list1[0]
                    list1 = list(map(int, list1[1:]))
                    if next_row[1] in list1:
                        value2 = self.constraint_violation(idx2, rows, target_map)
                        lst = np.array([value1, value2], dtype=np.float64)
                        if op == 'and':
                            return np.nanmax(lst)
                        else:
                            return np.nanmin(lst)

                value2 = self.constraint_violation(idx2, rows, target_map)
                lst = np.array([value1, value2], dtype=np.float64)
                return np.nanmax(lst)

    def kill_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.shutdown(2)
            s.close()

            find_port = 'netstat -aon | findstr %s' % port
            # Execute cmd command to return object
            result = os.popen(find_port)
            # Read the returned result
            text = result.read()
            text = [i.split(' ') for i in text.split('\n') if i]
            pids = []
            for i in text:
                pid = [u for u in i if u]
                if str(port) in pid[1]:
                    pids.append(pid[-1])
            # print(pids)
            pids = list(set(pids))
            # Kill the pid occupying the port
            for pid in pids:
                find_kill = 'taskkill -f -pid %s' % pid
                result = os.popen(find_kill)
                # print(result.read())

            time.sleep(5)
        except Exception as e:
            print('{} port is not enabled!'.format(port))
            print(e)

    def load_carla(self):

        free_port = self.find_free_port()

        command0 = "start  C:\CARLA\carla_0.9.9\CarlaUE4.exe --no-rendering -quality-level=Low -windowed -windowed -ResX=500 -ResY=500-carla-server -carla-world-port={} --town05".format(
            free_port)
        server_process = subprocess.Popen(command0, shell=True)
        server_process.communicate()
        time.sleep(10)
        print("--> a new carla started!")

        client = carla.Client(host, free_port, worker_threads=1)
        client.set_timeout(30.0)
        world = client.load_world(town)
        return free_port, client, world

    def find_free_port(self):
        command = "bash openport.sh"
        result = os.popen(command)
        new_port = int(result.read())
        print("free port is: {}".format(new_port))
        return new_port

    def convert_to_xml(self, x):
        xml_file_path = "C:/CARLA/scenario_runner-0.9.8/srunner/examples/{}.xml".format(
            scenario_config_file)
        scenario_id = "{}_{}".format(scenario_name, self.scenario_number)

        scenario = ET.Element('scenario')
        scenario.set("town", town)
        scenario.set("name", scenario_id)
        scenario.set("type", scenario_name)

        weather_elm = ET.Element("weather")
        weather_elm.set("cloudiness", str(x[0]))
        weather_elm.set("precipitation", str(x[1]))
        weather_elm.set("precipitation_deposits", str(x[2]))
        weather_elm.set("wind_intensity", str(x[3]))
        weather_elm.set("sun_azimuth_angle", str(x[4]))
        weather_elm.set("sun_altitude_angle", str(x[5]))
        weather_elm.set("fog_density", str(x[6]))
        weather_elm.set("fog_distance", str(x[7]))
        weather_elm.set("wetness", str(x[8]))
        scenario.append(weather_elm)

        pedstrian_elm = ET.Element("pedestrian")
        pedstrian_elm.set("start_distance", str(x[9]))
        pedstrian_elm.set("target_velocity", str(x[10]))
        pedstrian_elm.set("yaw", str(x[11]))

        scenario.append(pedstrian_elm)

        friction_elm = ET.Element("friction")
        friction_elm.set("mu", str(x[12]))
        scenario.append(friction_elm)

        friction_elm = ET.Element("path")
        friction_elm.set("io_no", str(x[13]))
        scenario.append(friction_elm)

        ego_vehicle_elm = ET.Element('ego_vehicle')
        ego_vehicle_elm.set("x", str(x[14]))
        ego_vehicle_elm.set("y", str(x[15]))
        ego_vehicle_elm.set("z", str(x[16]))
        ego_vehicle_elm.set("yaw", str(x[17]))
        ego_vehicle_elm.set("curvature", str(x[18]))
        ego_vehicle_elm.set("model", "vehicle.lincoln.mkz2017")
        scenario.append(ego_vehicle_elm)

        if self.scenario_number == 1:
            scenarios = ET.Element('scenarios')
        else:
            scenarios = ET.parse(xml_file_path).getroot()

        scenarios.append(scenario)
        data = ET.tostring(scenarios, encoding="unicode")

        with open(xml_file_path, 'w') as f:
            f.write(data)

        return scenario_id

############################### nsgaii operators ##############################
class LoggingArchive(Archive):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.log = []

    def add(self, solution):
        super().add(copy.deepcopy(solution))
        self.log.append([copy.deepcopy(solution)])

class RandomGenerator(Generator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

    def generate(self, problem):
        solution = None
        if len(problem.init_pop) > 0:
            solution = copy.deepcopy(problem.init_pop[0])
            solution.problem = problem
            del problem.init_pop[0]
            print('seeding solution done!')

        if not solution:
            solution = Solution(problem)

            _cloudiness = Real(problem.domains[0][2], problem.domains[1][2]).rand()
            _precipitation = Real(problem.domains[2][2], problem.domains[3][2]).rand()
            _precipitation_deposits = Real(problem.domains[4][2], problem.domains[5][2]).rand()
            _wind_intensity = Real(problem.domains[6][2], problem.domains[7][2]).rand()
            _sun_azimuth_angle = Real(problem.domains[8][2], problem.domains[9][2]).rand()
            _sun_altitude_angle = Real(problem.domains[10][2], problem.domains[11][2]).rand()
            _fog_density = Real(problem.domains[12][2], problem.domains[13][2]).rand()
            _fog_distance = Real(problem.domains[14][2], problem.domains[15][2]).rand()
            _wetness = Real(problem.domains[16][2], problem.domains[17][2]).rand()

            _start_distance = Real(problem.domains[18][2], problem.domains[19][2]).rand()
            _other_actor_target_velocity = Real(problem.domains[20][2], problem.domains[21][2]).rand()
            _other_actor_yaw = Real(problem.domains[22][2], problem.domains[23][2]).rand()
            _friction = Real(problem.domains[24][2], problem.domains[25][2]).rand()

            if single_road:
                idx = target_road
            else:
                idx = random.randint(1, problem.dynamic_params)

            _curvature_id = problem.types[constraint_var_id].encode(idx)
            _IO_number = problem.types[io_var_id].encode(-1)
            idx = idx - 1
            road = problem.roads[idx]
            road_id = road[0]
            lane_id = road[1]
            start = road[4]
            end = road[5]

            while True:
                try:
                    free_port, client, world = problem.load_carla()
                    break
                except BaseException  as e:
                    "try agin for a new port..."
                    print(e)
                    "waite..."

            filtered_waypoints = get_spawnpoint(world, road_id, lane_id, start, end)
            vehicle_blueprint = world.get_blueprint_library().filter('model3')[0]
            player = None
            while player is None:
                spawn_point = filtered_waypoints[random.randrange(len(filtered_waypoints))].transform
                spawn_point.location.z += 2
                player = world.try_spawn_actor(vehicle_blueprint, spawn_point)

            player = None
            vehicle_blueprint = None

            logger.debug("road id: {}=> {}".format(road_id, spawn_point))

            solution.variables = [_cloudiness, _precipitation, _precipitation_deposits, _wind_intensity, _sun_azimuth_angle,
                                  _sun_altitude_angle, _fog_density, _fog_distance, _wetness, _start_distance,
                                  _other_actor_target_velocity, _other_actor_yaw, _friction, _IO_number,
                                  spawn_point.location.x, spawn_point.location.y,
                                  spawn_point.location.z, spawn_point.rotation.yaw, _curvature_id]

            world = None
            client = None
            filtered_waypoints = None

            problem.kill_port(free_port)

        return solution

class SBX(Variator):
    def __init__(self, probability=1.0, distribution_index=15.0):
        super(SBX, self).__init__(2)
        self.probability = probability
        self.distribution_index = distribution_index
        self.filter = filter

    def evolve(self, parents):
        child1 = copy.deepcopy(parents[0])
        child2 = copy.deepcopy(parents[1])

        problem = child1.problem
        nvars = problem.nvars
        while True:
            try:
                free_port, client, world = problem.load_carla()
                break
            except BaseException as e:
                "try agin for a new port..."
                print(e)
                "waite..."

        map = world.get_map()

        _curvature_id1 = child1.variables[constraint_var_id]
        idx1 = problem.roads_index.index(Integer(1, problem.dynamic_params).decode(_curvature_id1))

        _curvature_id2 = child2.variables[constraint_var_id]
        idx2 = problem.roads_index.index(Integer(1, problem.dynamic_params).decode(_curvature_id2))


        if random.uniform(0.0, 1.0) <= self.probability and idx1 == idx2:
            for i in range(nvars):
                if isinstance(problem.types[i], Real) or (not isinstance(problem.types[i], Integer) and type(problem.types[i]) == list):
                    if random.uniform(0.0, 1.0) <= 0.5:
                        x1 = float(child1.variables[i])
                        x2 = float(child2.variables[i])
                        #todo: how prepare these type ranges?
                        if i < static_params:
                            lb = problem.types[i].min_value
                            ub = problem.types[i].max_value
                        else:
                            lb = problem.types[i][idx1].min_value
                            ub = problem.types[i][idx1].max_value

                        x1, x2 = self.sbx_crossover(x1, x2, lb, ub)
                        child1.variables[i] = x1
                        child2.variables[i] = x2
                        child1.evaluated = False
                        child2.evaluated = False

            x_id = static_params
            y_id = static_params + 1
            z_id = static_params + 2
            yaw_id = static_params + 3

            x = child1.variables[x_id]
            y = child1.variables[y_id]
            z = child1.variables[z_id]

            spawn_point1 = map.get_waypoint(carla.Location(x, y, z))
            spawn_point1.transform.location.z += 2.0

            x = child2.variables[x_id]
            y = child2.variables[y_id]
            z = child2.variables[z_id]

            spawn_point2 = map.get_waypoint(carla.Location(x, y, z))
            spawn_point2.transform.location.z += 2.0

            road1 = problem.roads[idx1]
            road1_id = road1[0]
            road1_lane_id = road1[1]
            road1_domain = problem.domains[problem.all_static_params + idx1]
            road1_start = road1_domain[0][2]
            road1_end = road1_domain[1][2]

            road2 = problem.roads[idx2]
            road2_id = road2[0]
            road2_lane_id = road2[1]
            road2_domain = problem.domains[problem.all_static_params + idx2]
            road2_start = road2_domain[0][2]
            road2_end = road2_domain[1][2]

            player1 = spawn_hero(world, self.filter, spawn_point1, road1_id)

            player2 = spawn_hero(world, self.filter, spawn_point2, road2_id)

            filtered_waypoints = []
            if player1 is None:
                filtered_waypoints = get_spawnpoint(world, road1_id, road1_lane_id, road1_start, road1_end)

            for a in world.get_actors().filter("vehicle*"):
                if a.is_alive:
                    a.destroy()

            vehicle_blueprint = world.get_blueprint_library().filter('model3')[0]
            while player1 is None:
                spawn_point1 = filtered_waypoints[random.randrange(len(filtered_waypoints))].transform
                spawn_point1.location.z += 2
                player1 = world.try_spawn_actor(vehicle_blueprint, spawn_point1)


            child1.variables[x_id] = spawn_point1.location.x
            child1.variables[y_id] = spawn_point1.location.y
            child1.variables[z_id] = spawn_point1.location.z
            child1.variables[yaw_id] = spawn_point1.rotation.yaw

            if player2 is None:
                filtered_waypoints = get_spawnpoint(world, road2_id, road2_lane_id, road2_start, road2_end)

            for a in world.get_actors().filter("vehicle*"):
                if a.is_alive:
                    a.destroy()

            vehicle_blueprint = world.get_blueprint_library().filter('model3')[0]
            while player2 is None:
                spawn_point2 = filtered_waypoints[random.randrange(len(filtered_waypoints))].transform
                spawn_point2.location.z += 2
                player2 = world.try_spawn_actor(vehicle_blueprint, spawn_point2)


            child2.variables[x_id] = spawn_point2.location.x
            child2.variables[y_id] = spawn_point2.location.y
            child2.variables[z_id] = spawn_point2.location.z
            child2.variables[yaw_id] = spawn_point2.rotation.yaw

        filtered_waypoints = None
        world = None
        client = None

        problem.kill_port(free_port)
        return [child1, child2]

    def sbx_crossover(self, x1, x2, lb, ub):
        dx = x2 - x1

        if dx > EPSILON:
            if x2 > x1:
                y2 = x2
                y1 = x1
            else:
                y2 = x1
                y1 = x2

            beta = 1.0 / (1.0 + (2.0 * (y1 - lb) / (y2 - y1)))
            alpha = 2.0 - np.float_power(beta, self.distribution_index + 1.0)
            rand = random.uniform(0.0, 1.0)

            if rand <= 1.0 / alpha:
                alpha = alpha * rand
                betaq = np.float_power(alpha, 1.0 / (self.distribution_index + 1.0))
            else:
                alpha = alpha * rand;
                alpha = 1.0 / (2.0 - alpha)
                betaq = np.float_power(alpha, 1.0 / (self.distribution_index + 1.0))

            x1 = 0.5 * ((y1 + y2) - betaq * (y2 - y1))
            beta = 1.0 / (1.0 + (2.0 * (ub - y2) / (y2 - y1)));
            alpha = 2.0 - np.float_power(beta, self.distribution_index + 1.0);

            if rand <= 1.0 / alpha:
                alpha = alpha * rand;
                betaq = np.float_power(alpha, 1.0 / (self.distribution_index + 1.0));
            else:
                alpha = alpha * rand;
                alpha = 1.0 / (2.0 - alpha);
                betaq = np.float_power(alpha, 1.0 / (self.distribution_index + 1.0));

            x2 = 0.5 * ((y1 + y2) + betaq * (y2 - y1));

            # randomly swap the values
            if bool(random.getrandbits(1)):
                x1, x2 = x2, x1

            x1 = clip(x1, lb, ub)
            x2 = clip(x2, lb, ub)

        return x1, x2

class PM(Mutation):

    def __init__(self, probability=1, distribution_index=20.0):
        super(PM, self).__init__()
        self.probability = probability
        self.distribution_index = distribution_index

    def mutate(self, parent):
        child = copy.deepcopy(parent)
        problem = child.problem
        probability = self.probability

        if isinstance(probability, int):
            probability /= float(len([t for t in problem.types if isinstance(t, Real) or (not isinstance(t, Integer) and type(t) == list)]))

        for i in range(len(child.variables)):
            if (isinstance(problem.types[i], Real) and problem.types[i].min_value != problem.types[i].max_value) or (not isinstance(problem.types[i], Integer) and type(problem.types[i]) == list):
                if random.uniform(0.0, 1.0) <= probability:
                    if i < static_params:
                        child.variables[i] = self.pm_mutation(float(child.variables[i]),
                                                              problem.types[i].min_value,
                                                              problem.types[i].max_value)
                    else:
                        idx = problem.roads_index.index(problem.types[constraint_var_id].decode(child.variables[constraint_var_id]))
                        if problem.types[i][idx].min_value != problem.types[i][idx].max_value:
                            child.variables[i] = self.pm_mutation(float(child.variables[i]),
                                                                  problem.types[i][idx].min_value,
                                                                  problem.types[i][idx].max_value)

                    child.evaluated = False

        return child

    def pm_mutation(self, x, lb, ub):
        u = random.uniform(0, 1)
        dx = ub - lb

        if u < 0.5:
            bl = (x - lb) / dx
            b = 2.0 * u + (1.0 - 2.0 * u) * np.float_power(1.0 - bl, self.distribution_index + 1.0)
            delta = np.float_power(b, 1.0 / (self.distribution_index + 1.0)) - 1.0
        else:
            bu = (ub - x) / dx
            b = 2.0 * (1.0 - u) + 2.0 * (u - 0.5) * np.float_power(1.0 - bu, self.distribution_index + 1.0)
            delta = 1.0 - np.float_power(b, 1.0 / (self.distribution_index + 1.0))

        x = x + delta * dx
        x = clip(x, lb, ub)

        return x

############################### utils #########################################
def load_dump(path):
    with open(path, "rb") as input_file:
        content = pickle.load(input_file)

    return content

def update_leaf_domain(domain, roads, rules):
    all_static_params = static_params * 2
    all_params = len(domain)
    dynamic_params = all_params - all_static_params

    excloude_roads = []
    for rule in rules:
        if rule[1] == 1:
            idx = rule[0] * 2
            if idx < all_static_params:
                domain[idx] = rule
            else:
                idx = all_static_params
                for i in range(dynamic_params):
                    if i in excloude_roads:
                        continue
                    if domain[idx + i][(rule[0] % static_params) * 2][2] < rule[2] and \
                            domain[idx + i][(rule[0] % static_params) * 2 + 1][2] >= rule[2]:
                        temp = list(domain[idx + i])
                        temp[(rule[0] % static_params) * 2] = rule
                        domain[idx + i] = temp
                    else:
                        excloude_roads.append(i)
        else:
            idx = rule[0] * 2 + 1
            if idx < all_static_params:
                domain[idx] = rule
            else:
                idx = all_static_params
                for i in range(dynamic_params):
                    if i in excloude_roads:
                        continue
                    if domain[idx + i][(rule[0] % static_params) * 2 + 1][2] > rule[2] and \
                            domain[idx + i][(rule[0] % static_params) * 2][2] <= rule[2]:
                        temp = list(domain[idx + i])
                        temp[(rule[0] % static_params) * 2 + 1] = rule
                        domain[idx + i] = temp
                    else:
                        excloude_roads.append(i)

    temp_domain = []
    temp_roads = []

    rule_accepted = False
    if excloude_roads and len(excloude_roads) < len(roads):
        rule_accepted = True
        for i in excloude_roads:
            temp_domain.append(domain[all_static_params + i])
            temp_roads.append(roads[i])

        for i in range(len(excloude_roads)):
            domain.remove(temp_domain[i])
            roads.remove(temp_roads[i])

    return rule_accepted ,domain, roads

def get_leaf_population_by_samples(P, Ri, problem):
    dict = {}
    for row in P:
        solution = Solution(problem)
        for i in range(problem.nvars):
            if i < static_params or i == constraint_var_id:
                solution.variables[i] = problem.types[i].encode(row[i])
            else:
                idx = problem.roads_index.index(row[constraint_var_id])
                solution.variables[i] = problem.types[i][idx].encode(row[i])

        solution.objectives = row[-5:-1]
        target = row[-1]
        thisnode = True

        for i, rule in enumerate(Ri):
            if type(rule[0]) == tuple:
                result = get_leaf_population_by_samples([row], list(rule), problem)
                if result:
                    thisnode = True
                    break
                else:
                    thisnode = False
                    continue
            elif type(solution.variables[rule[0]]) == list:
                value = copy.deepcopy(solution.variables[rule[0]])
                if rule[0] == constraint_var_id:
                    value = Integer(1, len(initial_roads)).decode(value)
                else:
                    value = solution.problem.types[io_var_id].decode(value)
            else:
                value = solution.variables[rule[0]]

            if rule[1] == 1:
                thisnode = np.logical_and(thisnode, value >= rule[2])
            else:
                thisnode = np.logical_and(thisnode, value <= rule[2])

            if not thisnode:
                break

        if thisnode:
            if target not in dict:
                dict[target] = [copy.deepcopy(solution)]
            else:
                dict[target].append(copy.deepcopy(solution))

    result = []
    dictionary_items = dict.items()
    sorted_items = sorted(dictionary_items)
    for item in sorted_items:
        v = item[1]
        legall_size = max_pop_size - len(result)
        if len(v) <= legall_size:
            result = result + v
        else:
            result = result + random.sample(v, legall_size)

        if len(result) >= max_pop_size:
            break;

    return result

def get_leaf_population_by_population(P, Ri, classes, delta, problem):
    dict = {}
    for _solution in P:
        thisnode = True
        solution = Solution(problem)
        solution.variables = copy.deepcopy(_solution.variables)
        solution.objectives = copy.deepcopy(_solution.objectives)

        speed = solution.objectives[3]
        if speed > -1:
            statues = 'unsafe'
        else:
            statues = 'safe'

        approach_level = solution.objectives[0]
        branch_distance = solution.objectives[1]

        if approach_level == 0 and branch_distance <= 0:
            label = 1  # feasible config
        else:
            label = -1  # infeasible config

        if label == 1:
            h_branch_distance = math.fabs(branch_distance + delta) - delta
            if h_branch_distance <= 0:
                path_class = 'b_target' #boundary target
            else:
                path_class = 'nb_target' #non boundary target
        elif approach_level == 0 and 0 < branch_distance <= 2* delta:
            path_class = 'b_non_target'
        else:
            path_class = 'nb_non_target'

        target = list.index(classes,'{}_{}'.format(path_class, statues))


        for i, rule in enumerate(Ri):
            if type(rule[0]) == tuple:
                result = get_leaf_population_by_population([solution], list(rule), classes, delta, problem)
                if result:
                    thisnode = True
                    break
                else:
                    thisnode = False
                    continue
            elif type(solution.variables[rule[0]]) == list:
                value = copy.deepcopy(solution.variables[rule[0]])
                if rule[0] == constraint_var_id:
                    value = Integer(1, len(initial_roads)).decode(value)
                else:
                    value = solution.problem.types[io_var_id].decode(value)
            else:
                value = solution.variables[rule[0]]

            if rule[1] == 1:
                thisnode = np.logical_and(thisnode, value >= rule[2])
            else:
                thisnode = np.logical_and(thisnode, value <= rule[2])

            if not thisnode:
                break

        if thisnode:
            if target not in dict:
                dict[target] = [copy.deepcopy(solution)]
            else:
                dict[target].append(copy.deepcopy(solution))

    result = []
    dictionary_items = dict.items()
    sorted_items = sorted(dictionary_items)
    for item in sorted_items:
        v = item[1]
        legall_size = max_pop_size - len(result)
        if len(v) <= legall_size:
            result = result + v
        else:
            result = result + random.sample(v, legall_size)

        if len(result) >= max_pop_size:
            break;

    return result

############################### extraction of i/o functions #####################
def get_io_lines():
    io_functions = [
        #actor
        'add_impulse', 'get_acceleration', 'get_angular_velocity', 'get_location', 'get_transform', 'get_velocity',
        'get_world', 'set_angular_velocity', 'set_location', 'set_simulate_physics', 'set_transform', 'set_velocity',
        #client
        'reload_world', 'load_world', 'get_available_maps', 'apply_batch', 'apply_batch_sync',
        #LIdarMeasurement
        'get_point_count', 'save_to_disk',
        #world
        'apply_settings', 'get_actors', 'get_map', 'get_settings', 'get_spectator', 'get_weather', 'set_weather', 'spawn_actor',
        'try_spawn_actor',
        #waypoint
        'get_left_lane', 'get_right_lane', 'next',
        #vehicle
        'apply_control', 'apply_physics_control', 'get_control', 'get_physics_control', 'get_speed_limit', 'get_traffic_light',
        'get_traffic_light_state', 'is_at_traffic_light', 'set_autopilot',
        #TrafficLight
        'freeze', 'get_elapsed_time', 'get_green_time', 'get_group_traffic_lights', 'get_pole_index', 'get_red_time', 'get_state',
        'get_yellow_time', 'is_frozen', 'set_green_time', 'set_red_time', 'set_state', 'set_yellow_time',
        #sensor
        'listen', #'stop',
        #map
        'generate_waypoints', 'get_spawn_points', 'get_topology', 'get_waypoint',
        #location
        'distance',
        #automatic_control
        'get_collision_frame_history', 'get_collision_history', '_on_collision', '_on_invasion', '_on_obstacle', '_get_forward_speed',
        '_get_rotation_matrix', '_get_linear_velocity', '_get_linear_acceleration', '_get_angular_velocity', '_get_simple_velocity',
        '_get_walker_info', '_get_road_info', '_on_can_bus_event', '_on_gnss_event', 'set_sensor', 'next_sensor',
        '_parse_image'
                    ]
    io_lines = {
        r"C:\CARLA\carla_0.9.9\PythonAPI\carla\agents\navigation\agent.py": [],
        r"C:\CARLA\carla_0.9.9\PythonAPI\carla\agents\navigation\behavior_agent.py": [],
        r"C:\CARLA\carla_0.9.9\PythonAPI\carla\agents\navigation\controller.py": [],
        r"C:\CARLA\carla_0.9.9\PythonAPI\carla\agents\navigation\local_planner_behavior.py": [],
        r"C:\CARLA\carla_0.9.9\PythonAPI\carla\agents\tools\misc.py": [],
        r"C:\CARLA\carla_0.9.9\PythonAPI\automatic_control.py": []
    }
    for item in io_lines.keys():
        fname = remove_comments(item)
        for io_call in io_functions:
            lines = check_if_string_in_file(fname, io_call+'(')
            if lines:
                io_lines[item].extend(lines)
    print(io_lines)
    return io_lines

def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only
    result = []
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for i, line in enumerate(read_obj, 1):
            # For each line, check if line contains the string
            _line = ''.join(line.split())
            if '.'+string_to_search in _line or '='+string_to_search in _line or _line.startswith(string_to_search): # string_to_search in line:
                # print(line, '----------->', string_to_search)
                result.append(i)
    return result

def remove_comments(fname):
    source = open(fname)
    new_fname = fname + ".strip"
    mod = open(new_fname, "w")

    prev_toktype = token.INDENT
    first_line = None
    last_lineno = -1
    last_col = 0
    last_text = ''

    tokgen = tokenize.generate_tokens(source.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if 0:
            print("%10s %-14s %-20r %r" % (
                tokenize.tok_name.get(toktype, toktype),
                "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                ttext, ltext
            ))
        if slineno > last_lineno:
            #check multiline statements
            if last_text.endswith('\\\n'):
                mod.write('\\\n')
            last_col = 0
        if scol > last_col:
            mod.write(" " * (scol - last_col))
        if toktype == token.STRING and prev_toktype == token.INDENT:
            index = len(ttext.split('\n'))
            indent = len(re.findall("^ *", ltext)[0])
            # Docstring
            for i in range(index):
                mod.write("#–")
                if i != index - 1:
                    mod.write("\n")
                mod.write(" " * indent)

        elif toktype == tokenize.COMMENT:
            # Comment
            mod.write("##")
        else:
            mod.write(ttext)
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno
        last_text = ltext
    return new_fname

############################### explaination and plotting #####################

def rule_transformation(rule, features):
    conditions = rule.split('and')
    result = []
    for condition in conditions:
        ops = condition.strip().split(' ')
        feature = ops[0]
        operator = ops[1]
        threshold = float(ops[2])

        feature_id = list.index(features, feature)
        if operator == '<=':
            op_id = -1
        else:
            op_id = 1

        result.append((feature_id, op_id, threshold))
    return result

def explain_model(data, target, save_path, save_fig, _min_samples, round, class_names, fea):
    lines = []
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop([target], axis=1), data[target], test_size=0.25, random_state=42, stratify=data[target])
    feature_names = X_train.columns

    # Train a gradient boosting classifier for benchmark
    gradient_boost_clf = GradientBoostingClassifier(random_state=42, n_estimators=30,  min_samples_leaf = _min_samples)
    gradient_boost_clf.fit(X_train, y_train)

    # Train a random forest classifier for benchmark
    random_forest_clf = RandomForestClassifier(random_state=42, n_estimators=30, min_samples_leaf = _min_samples)
    random_forest_clf.fit(X_train, y_train)

    # Train a decision tree classifier for benchmark
    decision_tree_clf = DecisionTreeClassifier(random_state=42,min_samples_leaf = _min_samples)
    decision_tree_clf.fit(X_train, y_train)

    cn = decision_tree_clf.classes_

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=300)
    tree.plot_tree(decision_tree_clf,
                   feature_names=fea,
                   class_names=class_names,
                   filled=True)
    date_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    fname = 'decision_tree_{}_{}'.format(round, date_time)
    fig.savefig('{}/{}.png'.format(save_fig, fname))  # (i + 1) * g

    # Train a skope-rules-boosting classifier
    skope_rules_clf = SkopeRules(max_depth_duplication=2,
                     n_estimators=30,
                     precision_min=0.7,
                     recall_min=0.7,
                     feature_names=feature_names)

    skope_rules_clf.fit(X_train, y_train)
    rules = skope_rules_clf.rules_

    for i in range(len(rules)):
        print('Rule ' + str(i + 1) + ':')
        lines.append(rules[i])
        print(rules[i])
        performances = compute_train_test_query_performances(X_train, y_train,
                                                      X_test, y_test,
                                                      skope_rules_clf.rules_[i][0])
        lines.append(performances)
        display(performances)

    # Compute prediction scores
    gradient_boost_scoring = gradient_boost_clf.predict_proba(X_test)[:, 1]
    random_forest_scoring = random_forest_clf.predict_proba(X_test)[:, 1]
    decision_tree_scoring = decision_tree_clf.predict_proba(X_test)[:, 1]
    skope_rules_scoring = skope_rules_clf.score_top_rules(X_test)

    if len(lines) > 0:
        date_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
        fname = '{}\skope_rules_round_{}_{}'.format(save_path, round ,date_time)

        with open('{}.txt'.format(fname), 'w+') as f:
            for line in lines:
                f.write(arrtostr(line) + '\n')

        fname = 'skope_rules_round_{}_{}'.format(round, date_time)
        plot_scores(fname, y_test, save_fig,
                    scores_with_line=[gradient_boost_scoring, random_forest_scoring, decision_tree_scoring],
                    scores_with_points=[skope_rules_scoring]
                    )

    return rules

def arrtostr(item):
    strr=''
    if isinstance(item, pd.DataFrame):
        strr = item.to_string(header=True, index=False)
    else:
        for b in item:
            strr+=str(b)+'   '
    return strr

def compute_y_pred_from_query(X, rule):
    score = np.zeros(X.shape[0])
    X = X.reset_index(drop=True)
    score[list(X.query(rule).index)] = 1
    return (score)

def compute_train_test_query_performances(X_train, y_train, X_test, y_test, rule):
    y_train_pred = compute_y_pred_from_query(X_train, rule)
    y_test_pred = compute_y_pred_from_query(X_test, rule)

    performances = None
    performances = pd.concat([
        performances,
        compute_performances_from_y_pred(y_train, y_train_pred, 'train_set')],
        axis=0)
    performances = pd.concat([
        performances,
        compute_performances_from_y_pred(y_test, y_test_pred, 'test_set')],
        axis=0)

    return (performances)

def compute_performances_from_y_pred(y_true, y_pred, index_name='default_index'):
    df = pd.DataFrame(data=
    {
        'precision': [0 if sum(y_pred) == 0 else sum(y_true * y_pred) / sum(y_pred)],
        'recall': [0 if sum(y_true) == 0 else sum(y_true * y_pred) / sum(y_true)]
    },
        index=[index_name],
        columns=['precision', 'recall']
    )
    return (df)

def plot_scores(fname, y_true, save_path, scores_with_line=[], scores_with_points=[],
                        labels_with_line=['Gradient Boosting', 'Random Forest', 'Decision Tree'],
                        labels_with_points=['skope-rules']):
    gradient = np.linspace(0, 1, 10)
    color_list = [cm.tab10(x) for x in gradient ]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5),
                         sharex=True, sharey=True)
    ax = axes[0]
    n_line = 0
    for i_score, score in enumerate(scores_with_line):
        n_line = n_line + 1
        fpr, tpr, thresholds = roc_curve(y_true, score)
        ax.plot(fpr, tpr, linestyle='-.', c=color_list[i_score], lw=1, label=labels_with_line[i_score])
    for i_score, score in enumerate(scores_with_points):
        fpr, tpr, thresholds = roc_curve(y_true, score)
        # calculate the g-mean for each threshold
        gmeans = np.sqrt(tpr * (1 - fpr))
        # locate the index of the largest g-mean
        ix = np.argmax(gmeans)
        print('Best Threshold (number of rules)=%f, G-Mean=%.3f' % (thresholds[ix], gmeans[ix]))
        ax.scatter(fpr[:-1], tpr[:-1], c=color_list[n_line + i_score], s=10, label=labels_with_points[i_score])
    ax.set_title("ROC", fontsize=20)
    ax.set_xlabel('False Positive Rate', fontsize=18)
    ax.set_ylabel('True Positive Rate (Recall)', fontsize=18)
    ax.legend(loc='lower center', fontsize=8)

    ax = axes[1]
    n_line = 0
    for i_score, score in enumerate(scores_with_line):
        n_line = n_line + 1
        precision, recall, _ = precision_recall_curve(y_true, score)
        ax.step(recall, precision, linestyle='-.', c=color_list[i_score], lw=1, where='post', label=labels_with_line[i_score])
    for i_score, score in enumerate(scores_with_points):
        precision, recall, _ = precision_recall_curve(y_true, score)
        ax.scatter(recall, precision, c=color_list[n_line + i_score], s=10, label=labels_with_points[i_score])
    ax.set_title("Precision-Recall", fontsize=20)
    ax.set_xlabel('Recall (True Positive Rate)', fontsize=18)
    ax.set_ylabel('Precision', fontsize=18)
    ax.legend(loc='lower center', fontsize=8)
    plt.savefig('{}/{}.png'.format(save_path, fname))
    plt.show()


############################### main ######################################################
def main(seeded=False, _round=1, _population_path=None,
             _pareto_path=None, _dataset_path=None):
    ##################################### initial configurations #####################################
    default_budget = 20 #in hour
    if seeded:
        default_budget = default_budget - (_round * 2)

    test_budget = default_budget * 60 * 60   # in second
    generations = 20
    initial_population_size = max_pop_size
    delta = 0.1
    max_time = 2*60 *60 # in second
    base_path = r"E:\members\kalaee\experiment\{}"
    decision_tree_addr = base_path.format('path_{}\dtree_round_{}_time_{}.{}')
    dataset_addr = base_path.format('path_{}\dataset_round_{}_time_{}.{}')
    labels_addr = base_path.format('path_{}\labels_round_{}_time_{}.{}')
    pareto_front_addr = base_path.format('path_{}\pareto_front_round_{}_time_{}.pickle')
    explicit_sub_domains_addr = base_path.format('path_{}\explicit_sub_domains_round_{}_time_{}.pickle')
    implicit_sub_domains_addr = base_path.format('path_{}\implicit_sub_domains_round_{}_time_{}.pickle')
    critical_path_addr = base_path.format('critical_paths\critical_path{}.csv')
    population_addr = base_path.format('path_{}\population_round_{}_time_{}.pickle')

    path_id = 0
    dir_name = "E:\members\kalaee\experiment"
    base_path = r"{}".format(dir_name) + '\{}'
    report_path = base_path.format(r"path_{}".format(path_id))
    target_path = base_path.format('critical_paths\critical_path{}.csv'.format(path_id))
    sample_path = r"{}/sample_set.csv".format(report_path)
    known_sample_path = r"{}/known_sample_set.csv".format(report_path)
    boundary_pair_samples_path = r"{}/boundary_pair_samples.csv".format(report_path)
    figs_path = r"{}/figs".format(report_path)
    generation_analysis_path = r"{}/generation_analysis.csv".format(report_path)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    if not os.path.exists(report_path):
        os.makedirs(report_path)

    if not os.path.exists(figs_path):
        os.makedirs(figs_path)

    columns = ["cloudiness",
               "precipitation",
               "precipitation_deposits",
               "wind_intensity",
               "sun_azimuth_angle",
               "sun_altitude_angle",
               "fog_density",
               "fog_distance",
               "wetness",
               "start_distance",
               "other_actor_target_velocity",
               "other_actor_yaw",
               "friction",
               "x",
               "y",
               "z",
               "yaw,"
               "target"
               ]

    row_list = ["round",
                "partition_no",
                "elapsed_time(min)",
                "nfe",
                "start_row_idx",
                "end_row_idx"
                ]
    if not seeded:
        with open(generation_analysis_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row_list)

    row_list = ['frame', 'timestamp', 'collision', 'obstacle', 'coverage_path',
                'cloudiness', 'precipitation', 'precipitation_deposits', 'wind_intensity', 'sun_azimuth_angle',
                'sun_altitude_angle', 'fog_density', 'fog_distance',
                'wetness', 'start_distance', 'other_actor_target_velocity', 'other_actor_yaw', 'tire_friction',
                'ego_location_x',
                'ego_location_y', 'ego_location_z', 'ego_location_yaw', 'ego_velocity', 'road_id', 'lane_id',
                'curvature', 'other_actor_location_x', 'other_actor_location_y', 'other_actor_location_z',
                'linear_acceleration', 'torque_curve',
                'steering_curve', 'steer_angle', 'lateral_speed', 'curvature_id', 'fitness', 'label', 'risk',
                'branch_distance', 'normalized_branch_distance',
                'approach_level', 'io_no', 'h_branch_distance','target', 'scenario_id','danger']
    if not seeded:
        with open(sample_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row_list)

    row_list = ["cloudiness",
                "precipitation",
                "precipitation_deposits",
                "wind_intensity",
                "sun_azimuth_angle",
                "sun_altitude_angle",
                "fog_density",
                "fog_distance",
                "wetness",
                "start_distance",
                "other_actor_target_velocity",
                "other_actor_yaw",
                "friction",
                "io_no",
                "x",
                "y",
                "z",
                "yaw",
                "curvature_id"]
    if not seeded:
        with open(known_sample_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row_list)

        with open(boundary_pair_samples_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)

    io_lines = get_io_lines()

    fn = ['cloudiness', 'precipitation', 'precipitation_deposits', 'wind_intensity', 'sun_azimuth_angle',
          'sun_altitude_angle', 'fog_density', 'fog_distance', 'wetness', 'start_distance',
          'other_actor_target_velocity', 'walker_yaw', 'friction', 'io_no', 'x', 'y', 'z', 'yaw', 'curvature_id', 'target']

    class_name = [ "b_target_unsafe","nb_target_unsafe", "b_target_safe", "nb_target_safe", "b_non_target_unsafe", "b_non_target_safe", "nb_non_target_unsafe", "nb_non_target_safe"]
    ##################################### end of initial configurations #####################################

    ##################################### Main #####################################
    try:
        target_path = critical_path_addr.format(path_id)
        max_k = 1  # number of subdomains
        min_k = 0
        do_random_pop = True
        rule_list = []
        P = []
        Best = []
        Q = []
        R = [initial_domain]
        RD = [initial_roads]
        round = 1

        ##################################### seeding #####################################
        if seeded:
            round = _round
            P = load_dump(_population_path)
            scenario_number = len(P) + 1
            logger.debug(
                "critical path -> {}    round{} will start by scenario_number -> {}".format(path_id, round+1,
                                                                                                    scenario_number))
            Best = load_dump(_pareto_path)
            if _dataset_path == "":
                dataset = []
                labels = []
                visited = []
                for solution in P:
                    if solution not in visited:
                        visited.append(copy.deepcopy(solution))

                for solution in visited:
                    problem = solution.problem
                    solution.variables[constraint_var_id] = problem.types[constraint_var_id].decode(
                        solution.variables[constraint_var_id])
                    solution.variables[io_var_id] = problem.types[io_var_id].decode(solution.variables[io_var_id])

                    speed = solution.objectives[3]
                    #
                    if speed > -1:
                        criticality_class = 'unsafe'
                    else:
                        criticality_class = 'safe'

                    approach_level = solution.objectives[0]
                    branch_distance = solution.objectives[1]

                    if approach_level == 0 and branch_distance <= 0:
                        lable = 1  # feasible config
                    else:
                        lable = 0  # infeasible config

                    labels.append(lable)

                    record = []
                    record = solution.variables
                    record.append(lable)
                    dataset.append(record)

                dataset = pd.DataFrame(data=dataset, columns=fn)
                date_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
                with open(dataset_addr.format(path_id, round, date_time, 'pickle'), 'wb') as f:
                    pickle.dump(dataset, f)
                logger.debug("dataset saved")
                exit(0)
            else:
                dataset = load_dump(_dataset_path)

            ##################################### explaination #####################################
            min_k = 0
            max_k = 1
            do_random_pop = True
            _min_samples = int(0.05 * len(dataset))
            if _min_samples >= 1:
                logger.debug("creating dt from nsgaii solutions...")

                ds = dataset.loc[(dataset['io_no'] != -1)]
                df = pd.DataFrame(data=ds, columns=fn)

                try:
                    filterd_df = df.iloc[:, np.r_[0:13, 14:20]]
                    logger.debug('explaining model...')
                    rules = explain_model(filterd_df, 'target', report_path, figs_path, _min_samples, round, ['non-target', 'target'], filterd_df.columns)
                except Exception as e:  # work on python 3.x
                    logger.debug('explain_model function Failed to run: ' + str(e))
                    rules = []

                if len(rules) >= 1:
                    partition_no = 0
                    R = []
                    RD = []
                    for rule in rules:
                        region = copy.deepcopy(initial_domain)
                        roads = copy.deepcopy(initial_roads)
                        transformed_rule = rule_transformation(rule[0], fn)
                        rule_accepted, update_rule, update_roads = update_leaf_domain(region, roads, transformed_rule)
                        if rule_accepted:
                            partition_no += 1
                            R.append(update_rule)
                            RD.append(update_roads)

                    if partition_no > 0:
                        max_k = partition_no
                        do_random_pop = False

            round += 1
            ##################################### end of explaination #####################################

        ##################################### end of seeding #####################################

        start_time = time.time()
        indexer = 0
        flag = True
        while flag:
            date_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
            logger.debug("round: {} time: {}  --> number of subdomains: {}".format(round, date_time, max_k))

            for j in range(min_k, max_k):
                # call NSGAII for scpecific domain: Rj
                logger.debug("critical path=> {}... round=> {}... sub-domain=> {}".format(path_id, round, j))
                logger.debug("***********************************************************")
                log_archive = LoggingArchive()
                random_generator = RandomGenerator()
                population_size = initial_population_size
                scenario_number = len(P) + 1
                logger.debug("critical path -> {}       round -> {}        current scenario_number -> {}".format(path_id, round, scenario_number))
                Q = []
                if do_random_pop:
                    logger.debug("random initialization...")
                    region = initial_domain
                    roads = initial_roads
                    problem = ABS(region, roads, filter, population_size, round, scenario_number, target_path, path_id,
                                  sample_path, io_lines, delta, dir_name, class_name)
                    init_pop = []
                else:
                    region = R[j]
                    roads = RD[j]
                    samples = pd.read_csv(sample_path)

                    print('current round to seed: {}'.format(round))
                    problem = ABS(region, roads, filter, population_size, round, scenario_number, target_path, path_id,
                                  sample_path, io_lines, delta, dir_name, class_name)
                    init_pop = get_leaf_population_by_population(P, region, class_name, delta, problem)
                    problem.init_pop = init_pop


                    logger.debug("#P: {}, #Q (i.e., population size): {}".format(len(P), len(init_pop)))


                sbx = SBX(0.6, 20.0)
                pm = PM(0.11, 25.0)

                algorithm = NSGAII(problem, population_size=population_size, variator=GAOperator(sbx, pm), log_frequency=1,
                archive = log_archive, generator = random_generator, population= Q)

                g = population_size * generations

                max_time_object = MaxTime(max_time = max_time)
                algorithm.run(condition = max_time_object)

                #log the search informations
                nfe = algorithm.nfe

                elapsed_time = timedelta(seconds=time.time() - start_time)
                with open(sample_path) as fp:
                    count = 0
                    for _ in fp:
                        count += 1
                row_num = count - indexer - 2
                generation_row_list = [round,
                            j,
                            elapsed_time,
                            nfe,
                            indexer,
                            row_num
                            ]
                indexer = count

                with open(generation_analysis_path, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(generation_row_list)
                    logger.debug('evaluation results was saved')

                #plot the objectives values
                plt.scatter([s.objectives[0] for s in algorithm.result],
                            [s.objectives[1] for s in algorithm.result])
                plt.xlabel("approach_level")
                plt.ylabel("branch_distance")

                date_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
                fname = 'objectives_round_{}_{}'.format(round, date_time)
                plt.savefig('{}/{}.png'.format(figs_path, fname))
                plt.show()

                # save the nsgaii outputs
                Q_prim = list(itertools.chain(*log_archive.log))
                P.extend(copy.deepcopy(Q_prim))
                #the last population is the pareto front
                B = algorithm.result._contents
                Best.extend(copy.deepcopy(B))

                logger.debug("#P: {}, #Best: {}, #Q: {} , #Q': {}".format(len(P), len(Best), len(Q), len(Q_prim)))

                #save best scenarios, i.e., pareto front
                nondominated_sort(Best)
                pareto_front = [x for x in Best if x.rank == 0]

                date_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
                with open(pareto_front_addr.format(path_id, round, date_time), 'wb') as f:
                    pickle.dump(pareto_front, f)
                logger.debug("pareto front saved-> k: {}".format(j))

                date_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
                with open(population_addr.format(path_id, round, date_time, 'pickle'), 'wb') as f:
                    pickle.dump(P, f)
                logger.debug("population saved-> k: {}".format(j))

                #check termination condition
                if time.time() - start_time >= test_budget:
                    flag = False
                    break

            dataset = []
            labels = []
            # compute labels
            visited = []
            for solution in P:
                if solution not in visited:
                    visited.append(copy.deepcopy(solution))

            for solution in visited:
                problem = solution.problem
                solution.variables[constraint_var_id] = problem.types[constraint_var_id].decode(solution.variables[constraint_var_id])
                solution.variables[io_var_id] = problem.types[io_var_id].decode(solution.variables[io_var_id])

                speed = solution.objectives[3]
                if speed > -1:
                    criticality_class = 'unsafe'
                else:
                    criticality_class = 'safe'

                approach_level = solution.objectives[0]
                branch_distance = solution.objectives[1]

                if approach_level == 0 and branch_distance <= 0:
                    lable = 1  # feasible config
                else:
                    lable = 0  # infeasible config

                labels.append(lable)

                record = []
                record = solution.variables
                record.append(lable)
                dataset.append(record)

            min_k = 0
            max_k = 1
            do_random_pop = True
            _min_samples = int(0.05 * len(dataset))
            if _min_samples >= 1:
                logger.debug("creating dt from nsgaii solutions...")

                ds = [data for data in dataset if data[io_var_id] != -1]
                df = pd.DataFrame(data=ds, columns=fn)

                try:
                    print('explain model...')
                    filterd_df = df.iloc[:, np.r_[0:13, 14:20]]
                    rules = explain_model(filterd_df, 'target', report_path, figs_path, _min_samples, round, ['non-target', 'target'], filterd_df.columns)
                except Exception as e:  # work on python 3.x
                    logger.debug('explain_model function Failed to run: ' + str(e))
                    rules = []

                df = pd.DataFrame(data=dataset, columns=fn)
                date_time = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

                with open(dataset_addr.format(path_id, round, date_time, 'pickle'), 'wb') as f:
                    pickle.dump(df, f)
                logger.debug("dataset saved")

                if len(rules) >= 1:
                    partition_no = 0
                    R = []
                    RD = []
                    for rule in rules:
                        region = copy.deepcopy(initial_domain)
                        roads = copy.deepcopy(initial_roads)
                        transformed_rule = rule_transformation(rule[0], fn)
                        rule_accepted, update_rule, update_roads = update_leaf_domain(region, roads, transformed_rule)
                        if rule_accepted:
                            partition_no += 1
                            R.append(update_rule)
                            RD.append(update_roads)

                    if partition_no > 0:
                        max_k = partition_no
                        do_random_pop = False

            round += 1

        #save scenario file
        src = r"C:\CARLA\scenario_runner-0.9.8\srunner\examples\{}.xml".format(
            scenario_config_file)
        dst = r"{}\scenarios.xml".format(report_path)
        from shutil import copyfile
        copyfile(src, dst)
        logger.debug("all test scenarios saved")

    except Exception as e: # work on python 3.x
        logger.debug('Failed to run: '+ str(e))


if __name__ == "__main__":
    base_path = r"E:\members\kalaee\experiment\ieee2-target_io-14-path_0"
    dataset_path = "".format(base_path)
    pareto_path = "{}\pareto_front_round_10_time_2021-09-20-11-16-08.pickle".format(base_path)
    population_path = "{}\population_round_10_time_2021-09-20-11-16-08.pickle".format(base_path)

    # main(seeded=True, _round=10, _population_path=population_path, _pareto_path=pareto_path, _dataset_path=dataset_path)
    main()

