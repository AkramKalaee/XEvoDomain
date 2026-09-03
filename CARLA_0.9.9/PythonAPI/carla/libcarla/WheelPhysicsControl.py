# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class WheelPhysicsControl(__Boost_Python.instance):
    # no doc
    def __eq__(self, WheelPhysicsControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (WheelPhysicsControl)arg1, (WheelPhysicsControl)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::rpc::WheelPhysicsControl {lvalue},class carla::rpc::WheelPhysicsControl)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (float)tire_friction=2.0 [, (float)damping_rate=0.25 [, (float)steer_angle=70.0 [, (bool)disable_steering=False]]]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,float=2.0 [,float=0.25 [,float=70.0 [,bool=False]]]])
        """
        pass

    def __ne__(self, WheelPhysicsControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (WheelPhysicsControl)arg1, (WheelPhysicsControl)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::rpc::WheelPhysicsControl {lvalue},class carla::rpc::WheelPhysicsControl)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, WheelPhysicsControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (WheelPhysicsControl)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::rpc::WheelPhysicsControl {lvalue})
        """
        pass

    damping_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disable_steering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    steer_angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tire_friction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 32


