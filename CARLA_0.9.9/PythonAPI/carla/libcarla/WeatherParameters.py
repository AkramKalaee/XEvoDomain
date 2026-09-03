# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class WeatherParameters(__Boost_Python.instance):
    # no doc
    def __eq__(self, WeatherParameters, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (WeatherParameters)arg1, (WeatherParameters)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::rpc::WeatherParameters {lvalue},class carla::rpc::WeatherParameters)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (float)cloudyness=0.0 [, (float)precipitation=0.0 [, (float)precipitation_deposits=0.0 [, (float)wind_intensity=0.0 [, (float)sun_azimuth_angle=0.0 [, (float)sun_altitude_angle=0.0]]]]]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,float=0.0 [,float=0.0 [,float=0.0 [,float=0.0 [,float=0.0 [,float=0.0]]]]]])
        """
        pass

    def __ne__(self, WeatherParameters, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (WeatherParameters)arg1, (WeatherParameters)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::rpc::WeatherParameters {lvalue},class carla::rpc::WeatherParameters)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, WeatherParameters, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (WeatherParameters)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::rpc::WeatherParameters {lvalue})
        """
        pass

    cloudyness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    precipitation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    precipitation_deposits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sun_altitude_angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sun_azimuth_angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wind_intensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ClearNoon = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DA50>'
    ClearSunset = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DCF0>'
    CloudyNoon = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DAB0>'
    CloudySunset = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DD50>'
    HardRainNoon = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DC30>'
    HardRainSunset = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DED0>'
    MidRainSunset = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DE70>'
    MidRainyNoon = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DBD0>'
    SoftRainNoon = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DC90>'
    SoftRainSunset = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DF30>'
    WetCloudyNoon = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DB70>'
    WetCloudySunset = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DE10>'
    WetNoon = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DB10>'
    WetSunset = None # (!) real value is '<carla.libcarla.WeatherParameters object at 0x000001FE4669DDB0>'
    __instance_size__ = 40


