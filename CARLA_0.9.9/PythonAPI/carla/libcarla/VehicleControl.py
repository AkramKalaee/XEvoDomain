# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class VehicleControl(__Boost_Python.instance):
    # no doc
    def __eq__(self, VehicleControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (VehicleControl)arg1, (VehicleControl)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::rpc::VehicleControl {lvalue},class carla::rpc::VehicleControl)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (float)throttle=0.0 [, (float)steer=0.0 [, (float)brake=0.0 [, (bool)hand_brake=False [, (bool)reverse=False [, (bool)manual_gear_shift=False [, (int)gear=0]]]]]]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,float=0.0 [,float=0.0 [,float=0.0 [,bool=False [,bool=False [,bool=False [,int=0]]]]]]])
        """
        pass

    def __ne__(self, VehicleControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (VehicleControl)arg1, (VehicleControl)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::rpc::VehicleControl {lvalue},class carla::rpc::VehicleControl)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, VehicleControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (VehicleControl)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::rpc::VehicleControl {lvalue})
        """
        pass

    brake = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hand_brake = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    manual_gear_shift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    steer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    throttle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 40


