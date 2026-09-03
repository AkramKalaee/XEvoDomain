# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class TrafficLightState(__Boost_Python.enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Green = 2
    names = {
        'Green': 2,
        'Off': 3,
        'Red': 0,
        'Unknown': 4,
        'Yellow': 1,
    }
    Off = 3
    Red = 0
    Unknown = 4
    values = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    Yellow = 1
    __slots__ = ()


