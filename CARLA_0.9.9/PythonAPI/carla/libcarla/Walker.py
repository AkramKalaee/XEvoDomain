# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting

from .Actor import Actor

class Walker(Actor):
    # no doc
    @setting.io_calls
    def apply_control(self, Walker, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        apply_control( (Walker)arg1, (WalkerControl)control) -> None :
        
            C++ signature :
                void apply_control(class carla::client::Walker {lvalue},class carla::rpc::WalkerControl)
        """
        pass

    @setting.io_calls
    def get_control(self, Walker, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_control( (Walker)arg1) -> WalkerControl :
        
            C++ signature :
                class carla::rpc::WalkerControl get_control(class carla::client::Walker {lvalue})
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

    def __str__(self, Walker, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Walker)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::Walker {lvalue})
        """
        pass

    bounding_box = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



