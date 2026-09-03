# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting

from .Actor import Actor

class Vehicle(Actor):
    # no doc
    @setting.counter
    def apply_control(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        apply_control( (Vehicle)arg1, (VehicleControl)control) -> None :
        
            C++ signature :
                void apply_control(class carla::client::Vehicle {lvalue},class carla::rpc::VehicleControl)
        """
        pass

    @setting.counter
    def apply_physics_control(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        apply_physics_control( (Vehicle)arg1, (VehiclePhysicsControl)physics_control) -> None :
        
            C++ signature :
                void apply_physics_control(class carla::client::Vehicle {lvalue},class carla::rpc::VehiclePhysicsControl)
        """
        pass

    @setting.counter
    def get_control(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_control( (Vehicle)arg1) -> VehicleControl :
        
            C++ signature :
                class carla::rpc::VehicleControl get_control(class carla::client::Vehicle {lvalue})
        """
        pass

    @setting.counter
    def get_physics_control(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_physics_control( (Vehicle)arg1) -> VehiclePhysicsControl :
        
            C++ signature :
                class carla::rpc::VehiclePhysicsControl get_physics_control(class carla::client::Vehicle)
        """
        pass

    @setting.counter
    def get_speed_limit(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_speed_limit( (Vehicle)arg1) -> float :
        
            C++ signature :
                float get_speed_limit(class carla::client::Vehicle {lvalue})
        """
        pass

    @setting.counter
    def get_traffic_light(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_traffic_light( (Vehicle)arg1) -> TrafficLight :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::TrafficLight> get_traffic_light(class carla::client::Vehicle {lvalue})
        """
        pass

    @setting.counter
    def get_traffic_light_state(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_traffic_light_state( (Vehicle)arg1) -> TrafficLightState :
        
            C++ signature :
                enum carla::rpc::TrafficLightState get_traffic_light_state(class carla::client::Vehicle {lvalue})
        """
        pass

    @setting.io_calls
    def is_at_traffic_light(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        is_at_traffic_light( (Vehicle)arg1) -> bool :
        
            C++ signature :
                bool is_at_traffic_light(class carla::client::Vehicle {lvalue})
        """
        pass

    @setting.counter
    def set_autopilot(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_autopilot( (Vehicle)arg1 [, (bool)enabled=True]) -> None :
        
            C++ signature :
                void set_autopilot(class carla::client::Vehicle {lvalue} [,bool=True])
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

    def __str__(self, Vehicle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Vehicle)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::Vehicle {lvalue})
        """
        pass

    bounding_box = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



