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

class Sensor(Actor):
    # no doc
    @setting.counter
    def listen(self, Sensor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        listen( (Sensor)arg1, (object)callback) -> None :
        
            C++ signature :
                void listen(class carla::client::Sensor {lvalue},class boost::python::api::object)
        """
        pass

    @setting.io_calls
    def stop(self, Sensor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        stop( (Sensor)arg1) -> None :
        
            C++ signature :
                void stop(class carla::client::Sensor {lvalue})
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

    def __str__(self, Sensor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Sensor)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::Sensor {lvalue})
        """
        pass

    is_listening = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



