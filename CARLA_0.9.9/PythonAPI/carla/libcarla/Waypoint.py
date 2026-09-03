# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class Waypoint(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def get_left_lane(self, Waypoint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_left_lane( (Waypoint)arg1) -> Waypoint :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Waypoint> get_left_lane(class carla::client::Waypoint {lvalue})
        """
        pass

    @setting.io_calls
    def get_right_lane(self, Waypoint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_right_lane( (Waypoint)arg1) -> Waypoint :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Waypoint> get_right_lane(class carla::client::Waypoint {lvalue})
        """
        pass

    @setting.io_calls
    def next(self, Waypoint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        next( (Waypoint)arg1, (float)distance) -> list :
        
            C++ signature :
                class boost::python::list next(class carla::client::Waypoint,double)
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

    def __str__(self, Waypoint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Waypoint)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::Waypoint {lvalue})
        """
        pass

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_intersection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lane_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lane_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lane_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lane_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left_lane_marking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    right_lane_marking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    road_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    section_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



