# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class Transform(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def get_forward_vector(self, Transform, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_forward_vector( (Transform)arg1) -> Vector3D :
        
            C++ signature :
                class carla::geom::Vector3D get_forward_vector(class carla::geom::Transform {lvalue})
        """
        pass

    @setting.io_calls
    def transform(self, Transform, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        transform( (Transform)arg1, (list)arg2) -> None :
        
            C++ signature :
                void transform(class carla::geom::Transform,class boost::python::list {lvalue})
        
        transform( (Transform)arg1, (Vector3D)in_point) -> Vector3D :
        
            C++ signature :
                class carla::geom::Vector3D transform(class carla::geom::Transform,class carla::geom::Vector3D {lvalue})
        """
        pass

    def __eq__(self, Transform, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (Transform)arg1, (Transform)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::geom::Transform {lvalue},class carla::geom::Transform)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (Location)location=<carla.libcarla.Location object at 0x000001FE4669D6F0> [, (Rotation)rotation=<carla.libcarla.Rotation object at 0x000001FE4669D690>]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,class carla::geom::Location=<carla.libcarla.Location object at 0x000001FE4669D6F0> [,class carla::geom::Rotation=<carla.libcarla.Rotation object at 0x000001FE4669D690>]])
        """
        pass

    def __ne__(self, Transform, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (Transform)arg1, (Transform)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::geom::Transform {lvalue},class carla::geom::Transform)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, Transform, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Transform)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::geom::Transform {lvalue})
        """
        pass

    location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 40


