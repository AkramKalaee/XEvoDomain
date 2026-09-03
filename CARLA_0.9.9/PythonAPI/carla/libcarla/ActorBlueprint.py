# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class ActorBlueprint(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def get_attribute(self, ActorBlueprint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_attribute( (ActorBlueprint)arg1, (str)arg2) -> ActorAttribute :
        
            C++ signature :
                class carla::client::ActorAttribute get_attribute(class carla::client::ActorBlueprint,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def has_attribute(self, ActorBlueprint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        has_attribute( (ActorBlueprint)arg1, (str)arg2) -> bool :
        
            C++ signature :
                bool has_attribute(class carla::client::ActorBlueprint {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def has_tag(self, ActorBlueprint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        has_tag( (ActorBlueprint)arg1, (str)arg2) -> bool :
        
            C++ signature :
                bool has_tag(class carla::client::ActorBlueprint {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def match_tags(self, ActorBlueprint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        match_tags( (ActorBlueprint)arg1, (str)arg2) -> bool :
        
            C++ signature :
                bool match_tags(class carla::client::ActorBlueprint {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def set_attribute(self, ActorBlueprint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_attribute( (ActorBlueprint)arg1, (str)arg2, (str)arg3) -> None :
        
            C++ signature :
                void set_attribute(class carla::client::ActorBlueprint {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
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
                struct boost::python::objects::iterator_range<struct boost::python::return_value_policy<struct boost::python::return_by_value,struct boost::python::default_call_policies>,class boost::iterators::transform_iterator<class <lambda_58a50b3bebf57cae1213e2a702382867>,class std::_List_const_iterator<class std::_List_val<struct std::_List_simple_types<struct std::pair<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const ,class carla::client::ActorAttribute> > > >,struct boost::iterators::use_default,struct boost::iterators::use_default> > __iter__(struct boost::python::back_reference<class carla::client::ActorBlueprint & __ptr64>)
        """
        pass

    def __len__(self, ActorBlueprint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (ActorBlueprint)arg1) -> int :
        
            C++ signature :
                unsigned __int64 __len__(class carla::client::ActorBlueprint {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, ActorBlueprint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (ActorBlueprint)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::ActorBlueprint {lvalue})
        """
        pass

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



