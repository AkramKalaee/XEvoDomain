# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


from .SensorData import SensorData

class GnssEvent(SensorData):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, GnssEvent, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (GnssEvent)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::sensor::data::GnssEvent {lvalue})
        """
        pass

    altitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



