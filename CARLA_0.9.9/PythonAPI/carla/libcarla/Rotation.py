# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class Rotation(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def get_forward_vector(self, Rotation, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_forward_vector( (Rotation)arg1) -> Vector3D :
        
            C++ signature :
                class carla::geom::Vector3D get_forward_vector(class carla::geom::Rotation {lvalue})
        """
        pass

    def __eq__(self, Rotation, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (Rotation)arg1, (Rotation)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::geom::Rotation {lvalue},class carla::geom::Rotation)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (float)pitch=0.0 [, (float)yaw=0.0 [, (float)roll=0.0]]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,float=0.0 [,float=0.0 [,float=0.0]]])
        """
        pass

    def __ne__(self, Rotation, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (Rotation)arg1, (Rotation)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::geom::Rotation {lvalue},class carla::geom::Rotation)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, Rotation, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Rotation)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::geom::Rotation {lvalue})
        """
        pass

    pitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    roll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yaw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 32


