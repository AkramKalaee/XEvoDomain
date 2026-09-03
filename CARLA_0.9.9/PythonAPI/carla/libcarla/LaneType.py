# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class LaneType(__Boost_Python.enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Any = -1
    Bidirectional = 512
    Biking = 16
    Border = 64
    Driving = 2
    Entry = 131072
    Exit = 262144
    Median = 1024
    names = {
        'Any': -1,
        'Bidirectional': 512,
        'Biking': 16,
        'Border': 64,
        'Driving': 2,
        'Entry': 131072,
        'Exit': 262144,
        'Median': 1024,
        'NONE': 1,
        'OffRamp': 524288,
        'OnRamp': 1048576,
        'Parking': 256,
        'Rail': 65536,
        'Restricted': 128,
        'RoadWorks': 16384,
        'Shoulder': 8,
        'Sidewalk': 32,
        'Special1': 2048,
        'Special2': 4096,
        'Special3': 8192,
        'Stop': 4,
        'Tram': 32768,
    }
    NONE = 1
    OffRamp = 524288
    OnRamp = 1048576
    Parking = 256
    Rail = 65536
    Restricted = 128
    RoadWorks = 16384
    Shoulder = 8
    Sidewalk = 32
    Special1 = 2048
    Special2 = 4096
    Special3 = 8192
    Stop = 4
    Tram = 32768
    values = {
        -1: -1,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
        128: 128,
        256: 256,
        512: 512,
        1024: 1024,
        2048: 2048,
        4096: 4096,
        8192: 8192,
        16384: 16384,
        32768: 32768,
        65536: 65536,
        131072: 131072,
        262144: 262144,
        524288: 524288,
        1048576: 1048576,
    }
    __slots__ = ()


