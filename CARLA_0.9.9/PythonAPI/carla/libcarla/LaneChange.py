# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class LaneChange(__Boost_Python.enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Both = 3
    Left = 2
    names = {
        'Both': 3,
        'Left': 2,
        'NONE': 0,
        'Right': 1,
    }
    NONE = 0
    Right = 1
    values = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }
    __slots__ = ()


