# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class DebugHelper(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def draw_arrow(self, DebugHelper, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        draw_arrow( (DebugHelper)arg1, (Location)begin, (Location)end [, (float)thickness=0.10000000149011612 [, (float)arrow_size=0.10000000149011612 [, (Color)color=<carla.libcarla.Color object at 0x000001FE46646580> [, (float)life_time=-1.0 [, (bool)persistent_lines=True]]]]]) -> None :
        
            C++ signature :
                void draw_arrow(class carla::client::DebugHelper {lvalue},class carla::geom::Location,class carla::geom::Location [,float=0.10000000149011612 [,float=0.10000000149011612 [,struct carla::sensor::data::Color=<carla.libcarla.Color object at 0x000001FE46646580> [,float=-1.0 [,bool=True]]]]])
        """
        pass

    @setting.io_calls
    def draw_box(self, DebugHelper, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        draw_box( (DebugHelper)arg1, (BoundingBox)box, (Rotation)rotation [, (float)thickness=0.10000000149011612 [, (Color)color=<carla.libcarla.Color object at 0x000001FE46646530> [, (float)life_time=-1.0 [, (bool)persistent_lines=True]]]]) -> None :
        
            C++ signature :
                void draw_box(class carla::client::DebugHelper {lvalue},class carla::geom::BoundingBox,class carla::geom::Rotation [,float=0.10000000149011612 [,struct carla::sensor::data::Color=<carla.libcarla.Color object at 0x000001FE46646530> [,float=-1.0 [,bool=True]]]])
        """
        pass

    @setting.io_calls
    def draw_line(self, DebugHelper, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        draw_line( (DebugHelper)arg1, (Location)begin, (Location)end [, (float)thickness=0.10000000149011612 [, (Color)color=<carla.libcarla.Color object at 0x000001FE466465D0> [, (float)life_time=-1.0 [, (bool)persistent_lines=True]]]]) -> None :
        
            C++ signature :
                void draw_line(class carla::client::DebugHelper {lvalue},class carla::geom::Location,class carla::geom::Location [,float=0.10000000149011612 [,struct carla::sensor::data::Color=<carla.libcarla.Color object at 0x000001FE466465D0> [,float=-1.0 [,bool=True]]]])
        """
        pass

    @setting.io_calls
    def draw_point(self, DebugHelper, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        draw_point( (DebugHelper)arg1, (Location)location [, (float)size=0.10000000149011612 [, (Color)color=<carla.libcarla.Color object at 0x000001FE46646620> [, (float)life_time=-1.0 [, (bool)persistent_lines=True]]]]) -> None :
        
            C++ signature :
                void draw_point(class carla::client::DebugHelper {lvalue},class carla::geom::Location [,float=0.10000000149011612 [,struct carla::sensor::data::Color=<carla.libcarla.Color object at 0x000001FE46646620> [,float=-1.0 [,bool=True]]]])
        """
        pass

    @setting.io_calls
    def draw_string(self, DebugHelper, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        draw_string( (DebugHelper)arg1, (Location)location, (str)text [, (bool)draw_shadow=False [, (Color)color=<carla.libcarla.Color object at 0x000001FE466464E0> [, (float)life_time=-1.0 [, (bool)persistent_lines=True]]]]) -> None :
        
            C++ signature :
                void draw_string(class carla::client::DebugHelper {lvalue},class carla::geom::Location,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False [,struct carla::sensor::data::Color=<carla.libcarla.Color object at 0x000001FE466464E0> [,float=-1.0 [,bool=True]]]])
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


