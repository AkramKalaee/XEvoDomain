# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python


class WorldSettings(__Boost_Python.instance):
    # no doc
    def __eq__(self, Timestamp, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __eq__( (Timestamp)arg1, (Timestamp)arg2) -> bool :
        
            C++ signature :
                bool __eq__(class carla::client::Timestamp {lvalue},class carla::client::Timestamp)
        """
        pass

    def __init__(self, p_object, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        
        __init__( (object)arg1 [, (bool)synchronous_mode=False [, (bool)no_rendering_mode=False]]) -> None :
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,bool=False [,bool=False]])
        """
        pass

    def __ne__(self, Timestamp, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __ne__( (Timestamp)arg1, (Timestamp)arg2) -> bool :
        
            C++ signature :
                bool __ne__(class carla::client::Timestamp {lvalue},class carla::client::Timestamp)
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, WorldSettings, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (WorldSettings)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::rpc::EpisodeSettings {lvalue})
        """
        pass

    no_rendering_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    synchronous_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __instance_size__ = 24


