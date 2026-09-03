# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class Map(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def generate_waypoints(self, Map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        generate_waypoints( (Map)arg1, (float)distance) -> list :
        
            C++ signature :
                class boost::python::list generate_waypoints(class carla::client::Map,double)
        """
        pass

    @setting.counter
    def get_spawn_points(self, Map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_spawn_points( (Map)arg1) -> list :
        
            C++ signature :
                class boost::python::list get_spawn_points(class carla::client::Map)
        """
        pass

    @setting.io_calls
    def get_topology(self, Map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_topology( (Map)arg1) -> list :
        
            C++ signature :
                class boost::python::list get_topology(class carla::client::Map)
        """
        pass

    @setting.counter
    def get_waypoint(self, Map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_waypoint( (Map)arg1, (Location)location [, (bool)project_to_road=True [, (int)lane_type=carla.libcarla.LaneType.Driving]]) -> Waypoint :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Waypoint> get_waypoint(class carla::client::Map {lvalue},class carla::geom::Location [,bool=True [,unsigned int=carla.libcarla.LaneType.Driving]])
        """
        pass

    @setting.io_calls
    def save_to_disk(self, Map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        save_to_disk( (Map)arg1 [, (str)path='']) -> None :
        
            C++ signature :
                void save_to_disk(class carla::client::Map [,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >=''])
        """
        pass

    @setting.io_calls
    def to_opendrive(self, Map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        to_opendrive( (Map)arg1) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > to_opendrive(class carla::client::Map)
        """
        pass

    @setting.io_calls
    def transform_to_geolocation(self, Map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        transform_to_geolocation( (Map)arg1, (Location)location) -> GeoLocation :
        
            C++ signature :
                class carla::geom::GeoLocation transform_to_geolocation(class carla::client::Map,class carla::geom::Location)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)name, (str)xodr_content) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, Map, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Map)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::Map {lvalue})
        """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



