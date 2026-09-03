import os
import datetime
from functools import wraps
import traceback
suts = ['behavior_agent', 'misc', 'local_planner_behavior', 'controller'] #'automatic_control',
trace_map = {}
trace_record = []
call_functions = []
simple_instrumentation = True #the variable sets korel distance on or off
global io_calls

# def traceit(frame, event, arg):
#     if event == "call":
#         # global coverage
#         global io_calls_
#         function_name = frame.f_code.co_name
#         print('function_name: ', function_name)
#         if function_name in ['get_map', 'get_actors', 'set_sensor', 'get_world', 'get_velocity',  'get_transform']:
#             # lineno = frame.f_lineno
#             # coverage.append(lineno)
#             io_calls_ += 1
#
#     return traceit

def counter(func):
    global io_calls
    @wraps(func)
    def tmp(*args, **kwargs):
        global io_calls
        #tmp.count += 1
        io_calls += 1
        print('counter: ', func)

        return func(*args, **kwargs)
    #tmp.count = 0
    return tmp

def func_logger(func):

    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        logger.info(f'Call func {func.__name__} with {args, kwargs} returns {ret}')
        return ret

    return inner

def method_logger(method):

    def inner(self, *args, **kwargs):
        ret = method(self, *args, **kwargs)
        logger.info(f'Call method {method.__name__} of {self} with {args, kwargs} returns {ret}')
        return ret

    return inner

import sys, inspect
class TrackCalls:
    def __init__(self):
        self._traceCalls = set()
        sys.settrace(self._trace_calls)

    def _get_func_name(self, frame):
        module = inspect.getmodule(frame)
        if module is not None:
            module_name = module.__name__
        func_name = frame.f_code.co_name
        arginfo = inspect.getargvalues(frame)
        if len(arginfo.args) > 0:
            if arginfo.args[0] == "self":
                func_name = "%s.%s" % (arginfo.locals["self"].__class__.__name__, func_name)
        return func_name

    def _filter_callee(self, func_filename): ###
        #if 'yourmodule.py' in func_filename:
        return True

    def _trace_calls(self, frame, event, arg):
        if event != 'call':
            return

        func_name = self._get_func_name(frame)
        if func_name == 'write':
            # Ignore write() calls from print statements
            return

        func_line_no = frame.f_lineno
        func_filename = frame.f_code.co_filename
        if not self._filter_callee(func_filename):
            return

        caller = frame.f_back
        caller_funcname = self._get_func_name(caller) #.f_code.co_name
        caller_line_no = caller.f_lineno
        caller_filename = caller.f_code.co_filename

        self._traceCalls.add((caller_filename, caller_funcname, func_filename, func_name))
        # self._traceCalls.add((arg_info, caller_arginfo))
        # date_time = datetime.datetime.now().strftime('_date_%Y-%m-%d_%H-%M-%S')


    def _simplify_trace_filename(self, lineItems, modules):
        line = list(lineItems)
        for modName in modules:
            if modName in line[0]:
                line[0] = os.path.basename(line[0])
            if modName in line[2]:
                line[2] = os.path.basename(line[2])
        return tuple(line)

    def _filter_line(self, lineItems): ###
        return True

    def save_data(self):
        sys.settrace(None)
        sys.stdout = sys.__stdout__
        date_time = datetime.datetime.now().strftime('_date_%Y-%m-%d_%H-%M-%S')
        traceOut = open("trace_{}.txt".format(date_time), 'w')
        # traceback.print_stack()
        # traceback.print_stack(file=traceOut)
        # with open("trace_{}.txt".format(date_time), 'w') as traceOut:
        #     for item in inspect.stack():
        #         traceOut.write("%s\n" % item)
        self._traceCalls = list(self._traceCalls)
        self._traceCalls.sort()
        for line in self._traceCalls:
            if self._filter_line(line):
                simpleLine = self._simplify_trace_filename(line, ['instrumentation.py','agent.py', 'setting.py', 'automatic_control.py', 'behavior_agent.py', 'misc.py', 'local_planner_behavior.py', 'controller.py'])
                traceOut.write('%10s %-40s %10s %-40s\n' % simpleLine)
            # traceOut.write('%s\n' % line)
        traceOut.close()

        info = ''

        # for thread_id, frame in sys._current_frames().items():
        #     print('Stack for thread {}'.format(thread_id))
        #     traceback.print_stack(frame)
        #     print('')

        traceOut = open("trace_temp.txt", 'a')
        # traceOut.write('{}\n'.format(info))
        # traceOut.close()

        for thread_id, frame in sys._current_frames().items():
            print('\n--- Stack for thread {t} ---'.format(t=thread_id))
            traceback.print_stack(frame, file=traceOut)

        # for item in reversed(inspect.stack()[2:]):
        #     info += ' File "{1}", line {2}, in {3}\n'.format(*item)
        # for line in item[4]:
        #     info += ' ' + line.lstrip()
        # for item in inspect.trace():
        #     info += ' File "{1}", line {2}, in {3}\n'.format(*item)
        # for line in item[4]:
        #     info += '' + line.lstrip()

        # tb = sys.exc_info()[2]
        # while 1:
        #     if not tb.tb_next:
        #         break
        #     tb = tb.tb_next
        # stack = []
        # f = tb.tb_frame
        # while f:
        #     stack.append(f)
        #     f = f.f_back
        # stack.reverse()
        # traceback.print_exc()
        # info += "Locals by frame, innermost last"
        # for frame in stack:
        #     info += "Frame %s in %s at line %s" % (frame.f_code.co_name,
        #                                    frame.f_code.co_filename,
        #                                    frame.f_lineno)
        #     for key, value in frame.f_locals.items():
        #         info += "\t%20s = " % key
        #         # We have to be VERY careful not to cause a new error in our error
        #         # printer! Calling str(  ) on an unknown object could cause an
        #         # error we don't want, so we must use try/except to catch it --
        #         # we can't stop it from happening, but we can and should
        #         # stop it from propagating if it does happen!
        #         try:
        #             info += value
        #         except:
        #             info += "<ERROR WHILE PRINTING VALUE>"

