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

class Image(SensorData):
    # no doc
    @setting.io_calls
    def convert(self, Image, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        convert( (Image)arg1, (ColorConverter)color_converter) -> None :
        
            C++ signature :
                void convert(class carla::sensor::data::ImageTmpl<struct carla::sensor::data::Color> {lvalue},enum EColorConverter)
        """
        pass

    @setting.io_calls
    def save_to_disk(self, Image, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        save_to_disk( (Image)arg1, (str)path [, (ColorConverter)color_converter=carla.libcarla.ColorConverter.Raw]) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > save_to_disk(class carla::sensor::data::ImageTmpl<struct carla::sensor::data::Color> {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,enum EColorConverter=carla.libcarla.ColorConverter.Raw])
        """
        pass

    def __getitem__(self, Image, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (Image)arg1, (int)arg2) -> Color :
        
            C++ signature :
                struct carla::sensor::data::Color __getitem__(class carla::sensor::data::ImageTmpl<struct carla::sensor::data::Color>,unsigned __int64)
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
                struct boost::python::objects::iterator_range<struct boost::python::return_value_policy<struct boost::python::return_by_value,struct boost::python::default_call_policies>,struct carla::sensor::data::Color * __ptr64> __iter__(struct boost::python::back_reference<class carla::sensor::data::ImageTmpl<struct carla::sensor::data::Color> & __ptr64>)
        """
        pass

    def __len__(self, Image, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (Image)arg1) -> int :
        
            C++ signature :
                unsigned __int64 __len__(class carla::sensor::data::ImageTmpl<struct carla::sensor::data::Color> {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, Image, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __setitem__( (Image)arg1, (int)arg2, (Color)arg3) -> None :
        
            C++ signature :
                void __setitem__(class carla::sensor::data::ImageTmpl<struct carla::sensor::data::Color> {lvalue},unsigned __int64,struct carla::sensor::data::Color)
        """
        pass

    def __str__(self, Image, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Image)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::sensor::data::ImageTmpl<struct carla::sensor::data::Color> {lvalue})
        """
        pass

    fov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



