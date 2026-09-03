# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class LaneMarkingColor(__Boost_Python.enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Blue = 1
    Green = 2
    names = {
        'Blue': 1,
        'Green': 2,
        'Other': 5,
        'Red': 3,
        'Standard': 0,
        'White': 0,
        'Yellow': 4,
    }
    Other = 5
    Red = 3
    Standard = 0
    values = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
    }
    White = 0
    Yellow = 4
    __slots__ = ()


