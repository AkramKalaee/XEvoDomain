# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class ActorAttribute(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def as_bool(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        as_bool( (ActorAttribute)arg1) -> bool :
        
            C++ signature :
                bool as_bool(class carla::client::ActorAttribute {lvalue})
        """
        pass

    @setting.io_calls
    def as_color(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        as_color( (ActorAttribute)arg1) -> Color :
        
            C++ signature :
                struct carla::sensor::data::Color as_color(class carla::client::ActorAttribute {lvalue})
        """
        pass

    @setting.io_calls
    def as_float(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        as_float( (ActorAttribute)arg1) -> float :
        
            C++ signature :
                float as_float(class carla::client::ActorAttribute {lvalue})
        """
        pass

    @setting.io_calls
    def as_int(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        as_int( (ActorAttribute)arg1) -> int :
        
            C++ signature :
                int as_int(class carla::client::ActorAttribute {lvalue})
        """
        pass

    @setting.io_calls
    def as_str(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        as_str( (ActorAttribute)arg1) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > as_str(class carla::client::ActorAttribute {lvalue})
        """
        pass

    def __bool__(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __bool__( (ActorAttribute)arg1) -> bool :
        
            C++ signature :
                bool __bool__(class carla::client::ActorAttribute {lvalue})
        """
        pass

    def __eq__(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (ActorAttribute)arg1, (bool)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::client::ActorAttribute {lvalue},bool)
        
        __eq__( (ActorAttribute)arg1, (int)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::client::ActorAttribute {lvalue},int)
        
        __eq__( (ActorAttribute)arg1, (float)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::client::ActorAttribute {lvalue},float)
        
        __eq__( (ActorAttribute)arg1, (str)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::client::ActorAttribute {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        
        __eq__( (ActorAttribute)arg1, (Color)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::client::ActorAttribute {lvalue},struct carla::sensor::data::Color)
        
        __eq__( (ActorAttribute)arg1, (ActorAttribute)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::client::ActorAttribute {lvalue},class carla::client::ActorAttribute)
        """
        pass

    def __float__(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __float__( (ActorAttribute)arg1) -> float :
        
            C++ signature :
                float __float__(class carla::client::ActorAttribute {lvalue})
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
        pass

    def __int__(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __int__( (ActorAttribute)arg1) -> int :
        
            C++ signature :
                int __int__(class carla::client::ActorAttribute {lvalue})
        """
        pass

    def __ne__(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (ActorAttribute)arg1, (bool)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::client::ActorAttribute {lvalue},bool)
        
        __ne__( (ActorAttribute)arg1, (int)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::client::ActorAttribute {lvalue},int)
        
        __ne__( (ActorAttribute)arg1, (float)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::client::ActorAttribute {lvalue},float)
        
        __ne__( (ActorAttribute)arg1, (str)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::client::ActorAttribute {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        
        __ne__( (ActorAttribute)arg1, (Color)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::client::ActorAttribute {lvalue},struct carla::sensor::data::Color)
        
        __ne__( (ActorAttribute)arg1, (ActorAttribute)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::client::ActorAttribute {lvalue},class carla::client::ActorAttribute)
        """
        pass

    def __nonzero__(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __nonzero__( (ActorAttribute)arg1) -> bool :
        
            C++ signature :
                bool __nonzero__(class carla::client::ActorAttribute {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, ActorAttribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (ActorAttribute)arg1) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > __str__(class carla::client::ActorAttribute {lvalue})
        
        __str__( (ActorAttribute)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::ActorAttribute {lvalue})
        """
        pass

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_modifiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    recommended_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



