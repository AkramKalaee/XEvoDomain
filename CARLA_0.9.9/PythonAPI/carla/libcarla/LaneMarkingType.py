# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class LaneMarkingType(__Boost_Python.enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BottsDots = 7
    Broken = 1
    BrokenBroken = 6
    BrokenSolid = 5
    Curb = 9
    Grass = 8
    names = {
        'BottsDots': 7,
        'Broken': 1,
        'BrokenBroken': 6,
        'BrokenSolid': 5,
        'Curb': 9,
        'Grass': 8,
        'NONE': 10,
        'Other': 0,
        'Solid': 2,
        'SolidBroken': 4,
        'SolidSolid': 3,
    }
    NONE = 10
    Other = 0
    Solid = 2
    SolidBroken = 4
    SolidSolid = 3
    values = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
    }
    __slots__ = ()


