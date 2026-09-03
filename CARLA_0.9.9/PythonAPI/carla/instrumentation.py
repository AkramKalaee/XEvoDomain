
__version__ = '2'
__author__ = 'Akram Kalaee'

import inspect
import sys
import numpy as np
import textwrap
import setting

def update_maps(condition_num, d_true, d_false, op, lhs, rhs):
    global distances_true, distances_false, conditions

    if condition_num in distances_true.keys():
        distances_true[condition_num] = min(
            distances_true[condition_num], d_true)
    else:
        distances_true[condition_num] = d_true

    if condition_num in distances_false.keys():
        distances_false[condition_num] = min(
            distances_false[condition_num], d_false)
    else:
        distances_false[condition_num] = d_false

    conditions.append([op, lhs, rhs])

def calculate_distance(op, lhs, rhs):
    #todo: update same as constraint handling methods

    distance_true = 0
    distance_false = 0
    K = 0.0001

    if isinstance(lhs, str):
        lhs = ord(lhs)
    if isinstance(rhs, str):
        rhs = ord(rhs)

    if op == "Eq":
        if lhs == rhs:
            distance_false = K
        else:
            distance_true = abs(lhs - rhs)

    elif op == "NotEq":
        if lhs != rhs:
            distance_false = abs(lhs - rhs)
        else:
            distance_true = K #violation

    elif op == "Lt":
        if lhs < rhs:
            distance_false = rhs - lhs
        else:
            distance_true = lhs - rhs + K #violation

    elif op == "LtE":
        if lhs <= rhs:
            distance_false = rhs - lhs + K
        else:
            distance_true = lhs - rhs #violation

    elif op == "Gt":
        if lhs > rhs:
            distance_false = lhs - rhs
        else:
            distance_true = rhs - lhs + K #violation

    elif op == "GtE":
        if lhs >= rhs:
            distance_false = lhs - rhs + K
        else:
            distance_true = rhs - lhs #violation

    elif op == "In":
        # minimum = sys.maxsize
        # for elem in rhs.keys():
        #     distance = abs(lhs - ord(elem))
        #     if distance < minimum:
        #         minimum = distance

        minimum = sys.maxsize
        for elem in rhs:
            distance = abs(lhs - elem)
            if distance < minimum:
                minimum = distance

        distance_true = minimum
        if distance_true == 0:
            distance_false = K
    elif op == "Pb" or op == "Nb":
        if lhs:
            distance_false = K
        else:
            distance_true = K
        # print('op: ', op, ' lsh: ', lhs, 'distance_true: ', distance_true, 'distance_false: ', distance_false)
    elif op == "IsNot":
        if lhs is not rhs:
            distance_false = K
        else:
            distance_true = K
        # print('op: ', op, ' lsh: ', lhs, 'distance_true: ', distance_true, 'distance_false: ', distance_false)
    elif op == "Is":
        if lhs is rhs:
            distance_false = K
        else:
            distance_true = K
        # print('op: ', op, ' lsh: ', lhs, 'distance_true: ', distance_true, 'distance_false: ', distance_false)

    return distance_true, distance_false

def run_predicate(op, lhs, rhs):
    if op == "Eq":
        if lhs == rhs:
            return True
        else:
            return False

    elif op == "NotEq":
        if lhs != rhs:
            return True
        else:
            return False
    elif op == "IsNot":
        if  lhs is not rhs:
            return True
        else:
            return False
    elif op == "Is":
        if lhs is rhs:
            return True
        else:
            return False
    else:
        print('----------------------------> ERROR:(       non_numeric_process', op)
        exit(0)

def evaluate_condition(file, branch_num, op, lhs, rhs, loop, ol):
    key = "{}_{}".format(file, branch_num)
    if key in setting.trace_map.keys():
        setting.trace_map[key] = setting.trace_map[key] + 1
    else:
        setting.trace_map[key] = 1

    if not isinstance(lhs, (int, float, complex)) and op not in ['Pb', 'Nb']:
        result = run_predicate(op, lhs, rhs)
        setting.trace_record.append([file, branch_num, None, None, loop, ol, setting.trace_map[key]])
        # if file in ['agent.py', 'behavior_agent.py']:
        #     print('file = ', file, ' branch_num = ', branch_num, ' result = ', result)
        return result

    distance_true, distance_false = calculate_distance(op, lhs, rhs)
    setting.trace_record.append([file, branch_num, distance_true, distance_false, loop, ol, setting.trace_map[key]])
    if distance_true == 0:
        result = True
    else:
        result = False
    # if file in ['agent.py', 'behavior_agent.py']:
    #     print('file = ', file, ' branch_num = ', branch_num, ' result = ', result)
    return result

def evaluate_condition_run(op, num, lhs, rhs):
    result = calculate_distance(op, lhs, rhs)
    distance_true = result[0]
    distance_false = result[1]
    update_maps(num, distance_true, distance_false, op, lhs, rhs)

    if distance_true == 0:
        return True
    else:
        return False

def save_as_instrumented_python(instrumented, name):
    with open("output/{}".format(name), "a") as ofh:
        ofh.write('\n')
        dedented = textwrap.indent(instrumented, '    ')
        ofh.write(dedented + '\n')

def normalize(x):
    return x / (1.0 + x)

def get_fitness(testfunc_instrumented, args, branch_num):
    global distances_true, distances_false, conditions
    op_list = ['GtE', 'Lt', 'Eq', 'LtE', 'Gt', 'NotEq', 'Pb', 'Nb']
    distances_true = {}
    distances_false = {}
    conditions = []

    testfunc_instrumented(*args)

    fitness_list = []
    total_fitness = 0.0
    counter = 0
    branch_operator_list = get_branch_operator_list(testfunc_instrumented)

    print('{} -> {}'.format(args, distances_true))

    for branch in list(range(1, branch_num+1)):
        branch_idx = branch_operator_list.index(branch)
        if branch_idx != 0:
            last_item_idx = branch_idx - 1
        else:
            last_item_idx = -1

        if branch_idx < len(branch_operator_list)-1:
             next_item_idx = branch_idx + 1
        else:
            next_item_idx = -1

        if branch in distances_true:
            branch_fitness = normalize(distances_true[branch])
            if last_item_idx != -1:
                if branch_operator_list[last_item_idx] == 'or':
                    #the before operator is 'or' or 'or not'
                    if branch_fitness == 0:
                        total_fitness = 0
                    else:
                        total_fitness = np.min([total_fitness, branch_fitness])
                elif branch_operator_list[last_item_idx] == 'and not':
                    if branch_fitness != 0:
                        total_fitness += 0
                    else:
                        #change operator
                        cond_args =conditions[counter]
                        op = op_list.index(cond_args[0])
                        left = cond_args[1]
                        right = cond_args[2]
                        new_op = reverse_operator(op)
                        #calculate predicate distance
                        calculate_distance(new_op, left, right)

                        #update fitness
                        total_fitness += branch_fitness
                elif branch_operator_list[last_item_idx] == 'or not':
                    if branch_fitness != 0:
                        total_fitness = 0
                    else:
                        # change operator
                        cond_args = conditions[counter]
                        op = op_list.index(cond_args[0])
                        left = cond_args[1]
                        right = cond_args[2]
                        new_op = reverse_operator(op)
                        # calculate predicate distance
                        calculate_distance(new_op, left, right)

                        # update fitness
                        total_fitness = np.min([total_fitness, branch_fitness])
                else:
                    total_fitness += branch_fitness
            else:
                #the first predicate
                total_fitness += branch_fitness
            counter += 1
        elif branch_operator_list[last_item_idx] == 'and' or branch_operator_list[last_item_idx] == 'and not':
            #the prdicate had not called
            total_fitness += 1.0

        #the end of the current predicate
        if branch_operator_list[next_item_idx] == ')':
            fitness_list.append(total_fitness)
            total_fitness = 0.0
            if next_item_idx < len(branch_operator_list)-2:
                if branch_operator_list[next_item_idx + 2] == '(':
                    external_op = branch_operator_list[next_item_idx + 1]
                    fitness_list.append(external_op)
            if len(fitness_list) == 3:
                if fitness_list[1] == 'or':
                    value = np.min([fitness_list[0], fitness_list[2]])
                elif fitness_list[1] == 'or not':
                    value = 0
                else:
                    value = fitness_list[0] + fitness_list[2]
                fitness_list = [value]
        elif next_item_idx == -1:
            # the last predicate
            fitness_list = [total_fitness]


    return fitness_list[0]

def reverse_operator(op):
    switcher = {
        0: 'Lt',  # 'GtE'
        1: 'GtE',  # 'Lt'
        2: 'NotEq',  # 'Eq'
        3: 'Gt',  # 'LtE'
        4: 'LtE',  # 'Gt'
        5: 'Eq',  # 'NotEq'
        6: 'IsNot',
        7: 'Is',
        8: 'NotIn',
        9: 'In'
    }
    return switcher.get(op, "nothing")

def get_branch_operator_list(testfunc_instrumented):
    branch_operator_list = []

    source = inspect.getsource(testfunc_instrumented)
    cond_list = source.split('evaluate_condition')
    cond_list = cond_list[1:]

    for cond in cond_list:
        branch = int(cond.lstrip('(').split(',')[0])
        cond = cond.rstrip('(').rstrip()
        if cond.endswith('and'):
            op = 'and'
        elif cond.endswith('or'):
            op = 'or'
        elif cond.endswith('or not'):
            op = 'or not'
        elif cond.endswith('and not'):
            op = 'and not'
        else:
            op = ''
        branch_operator_list.append(branch)
        if op != '':
            branch_operator_list.append(op)

    # handle parentheses
    cond_list = [cond.strip() for cond in cond_list]
    cond_list = ''.join(cond_list).split('((')
    cond_list = [cond.strip() for cond in cond_list]

    for cond in cond_list:
        cond_items = []
        cond_items = (cond.replace('or', 'and').replace('and not','and')).split('and')
        cond_items = [cond_item.strip('(') for cond_item in cond_items if cond_item]
        paratenses_idx = [int(cond_item.split(',')[0]) for cond_item in cond_items]

        _start = branch_operator_list.index(paratenses_idx[0])
        branch_operator_list.insert(_start, '(')

        _end = branch_operator_list.index(paratenses_idx[-1])+1
        branch_operator_list.insert(_end, ')')

    return branch_operator_list
