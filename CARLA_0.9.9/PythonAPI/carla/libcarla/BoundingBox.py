# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class BoundingBox(__Boost_Python.instance):
    # no doc
    def __eq__(self, BoundingBox, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (BoundingBox)arg1, (BoundingBox)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::geom::BoundingBox {lvalue},class carla::geom::BoundingBox)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (Location)location=<carla.libcarla.Location object at 0x000001FE4669D7B0> [, (Vector3D)extent=<carla.libcarla.Vector3D object at 0x000001FE4669D750>]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,class carla::geom::Location=<carla.libcarla.Location object at 0x000001FE4669D7B0> [,class carla::geom::Vector3D=<carla.libcarla.Vector3D object at 0x000001FE4669D750>]])
        """
        pass

    def __ne__(self, BoundingBox, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (BoundingBox)arg1, (BoundingBox)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::geom::BoundingBox {lvalue},class carla::geom::BoundingBox)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, BoundingBox, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (BoundingBox)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::geom::BoundingBox {lvalue})
        """
        pass

    extent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 40


