# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting

from .TrafficSign import TrafficSign

class TrafficLight(TrafficSign):
    # no doc
    @setting.io_calls
    def freeze(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        freeze( (TrafficLight)arg1, (bool)freeze) -> None :
        
            C++ signature :
                void freeze(class carla::client::TrafficLight {lvalue},bool)
        """
        pass

    @setting.io_calls
    def get_elapsed_time(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_elapsed_time( (TrafficLight)arg1) -> float :
        
            C++ signature :
                float get_elapsed_time(class carla::client::TrafficLight {lvalue})
        """
        pass

    @setting.io_calls
    def get_green_time(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_green_time( (TrafficLight)arg1) -> float :
        
            C++ signature :
                float get_green_time(class carla::client::TrafficLight {lvalue})
        """
        pass

    @setting.io_calls
    def get_group_traffic_lights(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_group_traffic_lights( (TrafficLight)arg1) -> list :
        
            C++ signature :
                class boost::python::list get_group_traffic_lights(class carla::client::TrafficLight {lvalue})
        """
        pass

    @setting.io_calls
    def get_pole_index(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_pole_index( (TrafficLight)arg1) -> int :
        
            C++ signature :
                unsigned int get_pole_index(class carla::client::TrafficLight {lvalue})
        """
        pass

    @setting.io_calls
    def get_red_time(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_red_time( (TrafficLight)arg1) -> float :
        
            C++ signature :
                float get_red_time(class carla::client::TrafficLight {lvalue})
        """
        pass

    @setting.io_calls
    def get_state(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_state( (TrafficLight)arg1) -> TrafficLightState :
        
            C++ signature :
                enum carla::rpc::TrafficLightState get_state(class carla::client::TrafficLight {lvalue})
        """
        pass

    @setting.io_calls
    def get_yellow_time(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_yellow_time( (TrafficLight)arg1) -> float :
        
            C++ signature :
                float get_yellow_time(class carla::client::TrafficLight {lvalue})
        """
        pass

    @setting.io_calls
    def is_frozen(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        is_frozen( (TrafficLight)arg1) -> bool :
        
            C++ signature :
                bool is_frozen(class carla::client::TrafficLight {lvalue})
        """
        pass

    @setting.io_calls
    def set_green_time(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_green_time( (TrafficLight)arg1, (float)green_time) -> None :
        
            C++ signature :
                void set_green_time(class carla::client::TrafficLight {lvalue},float)
        """
        pass

    @setting.io_calls
    def set_red_time(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_red_time( (TrafficLight)arg1, (float)red_time) -> None :
        
            C++ signature :
                void set_red_time(class carla::client::TrafficLight {lvalue},float)
        """
        pass

    @setting.io_calls
    def set_state(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_state( (TrafficLight)arg1, (TrafficLightState)state) -> None :
        
            C++ signature :
                void set_state(class carla::client::TrafficLight {lvalue},enum carla::rpc::TrafficLightState)
        """
        pass

    @setting.io_calls
    def set_yellow_time(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_yellow_time( (TrafficLight)arg1, (float)yellow_time) -> None :
        
            C++ signature :
                void set_yellow_time(class carla::client::TrafficLight {lvalue},float)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, TrafficLight, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (TrafficLight)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::TrafficLight {lvalue})
        """
        pass

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



