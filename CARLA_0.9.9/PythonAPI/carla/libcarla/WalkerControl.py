# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class WalkerControl(__Boost_Python.instance):
    # no doc
    def __eq__(self, WalkerControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (WalkerControl)arg1, (WalkerControl)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::rpc::WalkerControl {lvalue},class carla::rpc::WalkerControl)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (Vector3D)direction=<carla.libcarla.Vector3D object at 0x000001FE4669D810> [, (float)speed=0.0 [, (bool)jump=False]]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,class carla::geom::Vector3D=<carla.libcarla.Vector3D object at 0x000001FE4669D810> [,float=0.0 [,bool=False]]])
        """
        pass

    def __ne__(self, WalkerControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (WalkerControl)arg1, (WalkerControl)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::rpc::WalkerControl {lvalue},class carla::rpc::WalkerControl)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, WalkerControl, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (WalkerControl)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::rpc::WalkerControl {lvalue})
        """
        pass

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jump = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    speed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 40


