# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class Client(__Boost_Python.instance):
    @setting.io_calls
    def apply_batch(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        apply_batch( (Client)arg1, (object)commands [, (bool)do_tick=False]) -> None :
        
            C++ signature :
                void apply_batch(class carla::client::Client,class boost::python::api::object [,bool=False])
        """
        pass

    @setting.io_calls
    def apply_batch_sync(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        apply_batch_sync( (Client)arg1, (object)commands [, (bool)do_tick=False]) -> list :
        
            C++ signature :
                class boost::python::list apply_batch_sync(class carla::client::Client,class boost::python::api::object [,bool=False])
        """
        pass

    @setting.io_calls
    def get_available_maps(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_available_maps( (Client)arg1) -> list :
        
            C++ signature :
                class boost::python::list get_available_maps(class carla::client::Client)
        """
        pass

    @setting.io_calls
    def get_client_version(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_client_version( (Client)arg1) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > get_client_version(class carla::client::Client {lvalue})
        """
        pass

    @setting.io_calls
    def get_server_version(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_server_version( (Client)arg1) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > get_server_version(class carla::client::Client)
        """
        pass

    @setting.io_calls
    def get_world(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_world( (Client)arg1) -> World :
        
            C++ signature :
                class carla::client::World get_world(class carla::client::Client {lvalue})
        """
        pass

    @setting.io_calls
    def load_world(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        load_world( (Client)arg1, (str)map_name) -> World :
        
            C++ signature :
                class carla::client::World load_world(class carla::client::Client,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def reload_world(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        reload_world( (Client)arg1) -> World :
        
            C++ signature :
                class carla::client::World reload_world(class carla::client::Client)
        """
        pass

    @setting.io_calls
    def replay_file(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        replay_file( (Client)arg1, (str)name, (float)time_start, (float)duration, (int)follow_id) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > replay_file(class carla::client::Client {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,float,float,int)
        """
        pass

    @setting.io_calls
    def set_timeout(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_timeout( (Client)arg1, (float)seconds) -> None :
        
            C++ signature :
                void set_timeout(class carla::client::Client {lvalue},double)
        """
        pass

    @setting.io_calls
    def show_recorder_actors_blocked(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        show_recorder_actors_blocked( (Client)arg1, (str)name, (float)min_time, (float)min_distance) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > show_recorder_actors_blocked(class carla::client::Client {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,float,float)
        """
        pass

    @setting.io_calls
    def show_recorder_collisions(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        show_recorder_collisions( (Client)arg1, (str)name, (str)type1, (str)type2) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > show_recorder_collisions(class carla::client::Client {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,char,char)
        """
        pass

    @setting.io_calls
    def show_recorder_file_info(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        show_recorder_file_info( (Client)arg1, (str)name) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > show_recorder_file_info(class carla::client::Client {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def start_recorder(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        start_recorder( (Client)arg1, (str)name) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > start_recorder(class carla::client::Client {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
        pass

    @setting.io_calls
    def stop_recorder(self, Client, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        stop_recorder( (Client)arg1) -> None :
        
            C++ signature :
                void stop_recorder(class carla::client::Client {lvalue})
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1, (str)host, (int)port [, (int)worker_threads=0]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,unsigned short [,unsigned __int64=0])
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __instance_size__ = 32


