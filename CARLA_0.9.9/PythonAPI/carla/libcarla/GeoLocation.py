# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class GeoLocation(__Boost_Python.instance):
    # no doc
    def __eq__(self, GeoLocation, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (GeoLocation)arg1, (GeoLocation)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::geom::GeoLocation {lvalue},class carla::geom::GeoLocation)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (float)latitude=0.0 [, (float)longitude=0.0 [, (float)altitude=0.0]]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,double=0.0 [,double=0.0 [,double=0.0]]])
        """
        pass

    def __ne__(self, GeoLocation, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (GeoLocation)arg1, (GeoLocation)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::geom::GeoLocation {lvalue},class carla::geom::GeoLocation)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, GeoLocation, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (GeoLocation)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::geom::GeoLocation {lvalue})
        """
        pass

    altitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 40


