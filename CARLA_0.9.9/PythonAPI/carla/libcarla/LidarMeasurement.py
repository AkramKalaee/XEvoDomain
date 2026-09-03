# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting

from .SensorData import SensorData

class LidarMeasurement(SensorData):
    # no doc
    @setting.io_calls
    def get_point_count(self, LidarMeasurement, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_point_count( (LidarMeasurement)arg1, (int)channel) -> int :
        
            C++ signature :
                unsigned int get_point_count(class carla::sensor::data::LidarMeasurement {lvalue},unsigned __int64)
        """
        pass

    @setting.io_calls
    def save_to_disk(self, LidarMeasurement, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        save_to_disk( (LidarMeasurement)arg1, (str)path) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > save_to_disk(class carla::sensor::data::LidarMeasurement {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    def __getitem__(self, LidarMeasurement, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (LidarMeasurement)arg1, (int)arg2) -> Location :
        
            C++ signature :
                class carla::geom::Location __getitem__(class carla::sensor::data::LidarMeasurement,unsigned __int64)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
        pass

    def __iter__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                struct boost::python::objects::iterator_range<struct boost::python::return_value_policy<struct boost::python::return_by_value,struct boost::python::default_call_policies>,class carla::geom::Location * __ptr64> __iter__(struct boost::python::back_reference<class carla::sensor::data::LidarMeasurement & __ptr64>)
        """
        pass

    def __len__(self, LidarMeasurement, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (LidarMeasurement)arg1) -> int :
        
            C++ signature :
                unsigned __int64 __len__(class carla::sensor::data::LidarMeasurement {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, LidarMeasurement, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (LidarMeasurement)arg1, (int)arg2, (Location)arg3) -> None :
        
            C++ signature :
                void __setitem__(class carla::sensor::data::LidarMeasurement {lvalue},unsigned __int64,class carla::geom::Location)
        """
        pass

    def __str__(self, LidarMeasurement, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (LidarMeasurement)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::sensor::data::LidarMeasurement {lvalue})
        """
        pass

    channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    horizontal_angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



