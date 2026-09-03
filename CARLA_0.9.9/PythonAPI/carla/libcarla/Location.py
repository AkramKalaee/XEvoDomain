# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting

from .Vector3D import Vector3D

class Location(Vector3D):
    # no doc
    @setting.io_calls
    def distance(self, Location, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        distance( (Location)arg1, (Location)location) -> float :
        
            C++ signature :
                double distance(class carla::geom::Location {lvalue},class carla::geom::Location)
        """
        pass

    def __eq__(self, Location, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (Location)arg1, (Location)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::geom::Location {lvalue},class carla::geom::Location)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (float)x=0.0 [, (float)y=0.0 [, (float)z=0.0]]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,float=0.0 [,float=0.0 [,float=0.0]]])
        
        __init__( (object)arg1, (Vector3D)rhs) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64,class carla::geom::Vector3D)
        """
        pass

    def __ne__(self, Location, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (Location)arg1, (Location)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::geom::Location {lvalue},class carla::geom::Location)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, Location, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Location)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::geom::Location {lvalue})
        """
        pass

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 32


