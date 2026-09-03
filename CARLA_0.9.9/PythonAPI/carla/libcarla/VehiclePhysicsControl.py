# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class VehiclePhysicsControl(__Boost_Python.instance):
    # no doc
    def __eq__(self, VehiclePhysicsControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (VehiclePhysicsControl)arg1, (VehiclePhysicsControl)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::rpc::VehiclePhysicsControl {lvalue},class carla::rpc::VehiclePhysicsControl)
        """
        pass

    def __init__(self, tuple_args, dict_kwds): # real signature unknown; restored from __doc__
        """
        object __init__(tuple args, dict kwds) :
            raw ctor
        
            C++ signature :
                object __init__(tuple args, dict kwds)
        
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
        pass

    def __ne__(self, VehiclePhysicsControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (VehiclePhysicsControl)arg1, (VehiclePhysicsControl)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::rpc::VehiclePhysicsControl {lvalue},class carla::rpc::VehiclePhysicsControl)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, VehiclePhysicsControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (VehiclePhysicsControl)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::rpc::VehiclePhysicsControl {lvalue})
        """
        pass

    center_of_mass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clutch_strength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    damping_rate_full_throttle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    damping_rate_zero_throttle_clutch_disengaged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    damping_rate_zero_throttle_clutch_engaged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_coefficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gear_switch_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_rpm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    moi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    steering_curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    torque_curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_gear_autobox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wheels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



