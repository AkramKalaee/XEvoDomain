# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting
from functools import wraps

class World(__Boost_Python.instance):
    # no doc
    @setting.counter
    def apply_settings(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        apply_settings( (World)arg1, (WorldSettings)arg2) -> None :
        
            C++ signature :
                void apply_settings(class carla::client::World {lvalue},class carla::rpc::EpisodeSettings)
        """
        pass

    @setting.counter
    def get_actors(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_actors( (World)arg1) -> ActorList :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::ActorList> get_actors(class carla::client::World)
        
        get_actors( (World)arg1, (list)actor_ids) -> ActorList :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::ActorList> get_actors(class carla::client::World {lvalue},class boost::python::list)
        """
        pass

    @setting.counter
    def get_blueprint_library(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_blueprint_library( (World)arg1) -> BlueprintLibrary :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::BlueprintLibrary> get_blueprint_library(class carla::client::World)
        """
        pass

    @setting.counter
    def get_map(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        if setting.trace_record:
            setting.io_calls += 1
        """
        get_map( (World)arg1) -> Map :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Map> get_map(class carla::client::World)
        """
        pass

    @setting.counter
    def get_settings(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_settings( (World)arg1) -> WorldSettings :
        
            C++ signature :
                class carla::rpc::EpisodeSettings get_settings(class carla::client::World)
        """
        pass

    @setting.counter
    def get_spectator(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_spectator( (World)arg1) -> Actor :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Actor> get_spectator(class carla::client::World)
        """
        pass

    @setting.counter
    def get_weather(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_weather( (World)arg1) -> WeatherParameters :
        
            C++ signature :
                class carla::rpc::WeatherParameters get_weather(class carla::client::World)
        """
        pass

    @setting.counter
    def on_tick(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        on_tick( (World)arg1, (object)callback) -> None :
        
            C++ signature :
                void on_tick(class carla::client::World {lvalue},class boost::python::api::object)
        """
        pass

    @setting.counter
    def set_weather(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_weather( (World)arg1, (WeatherParameters)arg2) -> None :
        
            C++ signature :
                void set_weather(class carla::client::World {lvalue},class carla::rpc::WeatherParameters)
        """
        pass

    @setting.counter
    def spawn_actor(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        spawn_actor( (World)arg1, (ActorBlueprint)blueprint, (Transform)transform [, (Actor)attach_to=None]) -> Actor :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Actor> spawn_actor(class carla::client::World {lvalue},class carla::client::ActorBlueprint,class carla::geom::Transform [,class carla::client::Actor * __ptr64=None])
        """
        pass

    @setting.counter
    def tick(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        tick( (World)arg1) -> None :
        
            C++ signature :
                void tick(class carla::client::World {lvalue})
        """
        pass

    @setting.counter
    def try_spawn_actor(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        try_spawn_actor( (World)arg1, (ActorBlueprint)blueprint, (Transform)transform [, (Actor)attach_to=None]) -> Actor :
        
            C++ signature :
                class boost::shared_ptr<class carla::client::Actor> try_spawn_actor(class carla::client::World {lvalue},class carla::client::ActorBlueprint,class carla::geom::Transform [,class carla::client::Actor * __ptr64=None])
        """
        pass

    @setting.counter
    def wait_for_tick(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        wait_for_tick( (World)arg1 [, (float)seconds=10.0]) -> Timestamp :
        
            C++ signature :
                class carla::client::Timestamp wait_for_tick(class carla::client::World [,double=10.0])
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

    def __str__(self, World, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (World)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::World {lvalue})
        """
        pass

    debug = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



