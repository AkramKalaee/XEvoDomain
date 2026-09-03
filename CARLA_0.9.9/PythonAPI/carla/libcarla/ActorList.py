# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class ActorList(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def filter(self, ActorList, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        filter( (ActorList)arg1, (str)wildcard_pattern) -> ActorList :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::ActorList> filter(class carla::client::ActorList {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def find(self, ActorList, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        find( (ActorList)arg1, (int)id) -> Actor :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Actor> find(class carla::client::ActorList {lvalue},unsigned int)
        """
        pass

    def __getitem__(self, ActorList, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (ActorList)arg1, (int)arg2) -> Actor :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Actor> __getitem__(class carla::client::ActorList {lvalue},unsigned __int64)
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
                struct boost::python::objects::iterator_range<struct boost::python::return_value_policy<struct boost::python::return_by_value,struct boost::python::default_call_policies>,class boost::iterators::transform_iterator<class <lambda_d0c368c6ff902ebf843f129147c0b2f2>,class std::_Vector_const_iterator<class std::_Vector_val<struct std::_Simple_types<class carla::client::detail::ActorVariant> > >,struct boost::iterators::use_default,struct boost::iterators::use_default> > __iter__(struct boost::python::back_reference<class carla::client::ActorList & __ptr64>)
        """
        pass

    def __len__(self, ActorList, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (ActorList)arg1) -> int :
        
            C++ signature :
                unsigned __int64 __len__(class carla::client::ActorList {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, ActorList, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (ActorList)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::ActorList {lvalue})
        """
        pass


