# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class BlueprintLibrary(__Boost_Python.instance):
    # no doc
    @setting.io_calls
    def filter(self, BlueprintLibrary, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        filter( (BlueprintLibrary)arg1, (str)wildcard_pattern) -> BlueprintLibrary :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::BlueprintLibrary> filter(class carla::client::BlueprintLibrary {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def find(self, BlueprintLibrary, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        find( (BlueprintLibrary)arg1, (str)id) -> ActorBlueprint :
        
            C++ signature :
                class carla::client::ActorBlueprint find(class carla::client::BlueprintLibrary,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    def __getitem__(self, BlueprintLibrary, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __getitem__( (BlueprintLibrary)arg1, (int)arg2) -> ActorBlueprint :
        
            C++ signature :
                class carla::client::ActorBlueprint __getitem__(class carla::client::BlueprintLibrary,unsigned __int64)
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
                struct boost::python::objects::iterator_range<struct boost::python::return_value_policy<struct boost::python::return_by_value,struct boost::python::default_call_policies>,class boost::iterators::transform_iterator<class <lambda_e3336f3429f720d46c7c1513874e757f>,class std::_List_const_iterator<class std::_List_val<struct std::_List_simple_types<struct std::pair<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > const ,class carla::client::ActorBlueprint> > > >,struct boost::iterators::use_default,struct boost::iterators::use_default> > __iter__(struct boost::python::back_reference<class carla::client::BlueprintLibrary & __ptr64>)
        """
        pass

    def __len__(self, BlueprintLibrary, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __len__( (BlueprintLibrary)arg1) -> int :
        
            C++ signature :
                unsigned __int64 __len__(class carla::client::BlueprintLibrary {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, BlueprintLibrary, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (BlueprintLibrary)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::BlueprintLibrary {lvalue})
        """
        pass


