# encoding: utf-8
# module carla.libcarla
# from C:\Users\RELab\Anaconda3\envs\carla\lib\site-packages\carla-0.9.5-py3.7-win-amd64.egg\carla\libcarla.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import libcarla.command as command # <module 'libcarla.command'>
import Boost.Python as __Boost_Python
import setting


class Actor(__Boost_Python.instance):
    # no doc
    @setting.counter
    def add_impulse(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        add_impulse( (Actor)arg1, (Vector3D)vector) -> None :
        
            C++ signature :
                void add_impulse(class carla::client::Actor {lvalue},class carla::geom::Vector3D)
        """
        pass

    @setting.counter
    def destroy(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        destroy( (Actor)arg1) -> bool :
        
            C++ signature :
                bool destroy(class carla::client::Actor {lvalue})
        """
        pass

    @setting.counter
    def get_acceleration(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_acceleration( (Actor)arg1) -> Vector3D :
        
            C++ signature :
                class carla::geom::Vector3D get_acceleration(class carla::client::Actor {lvalue})
        """
        pass

    @setting.counter
    def get_angular_velocity(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_angular_velocity( (Actor)arg1) -> Vector3D :
        
            C++ signature :
                class carla::geom::Vector3D get_angular_velocity(class carla::client::Actor {lvalue})
        """
        pass

    @setting.counter
    def get_location(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_location( (Actor)arg1) -> Location :
        
            C++ signature :
                class carla::geom::Location get_location(class carla::client::Actor {lvalue})
        """
        pass

    @setting.counter
    def get_transform_(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
        """
        get_transform( (Actor)arg1) -> Transform :
        
            C++ signature :
                class carla::geom::Transform get_transform(class carla::client::Actor {lvalue})
        """
        pass

    @setting.counter
    def get_velocity(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_velocity( (Actor)arg1) -> Vector3D :
        
            C++ signature :
                class carla::geom::Vector3D get_velocity(class carla::client::Actor {lvalue})
        """
        pass

    @setting.counter
    def get_world(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_world( (Actor)arg1) -> World :
        
            C++ signature :
                class carla::client::World get_world(class carla::client::Actor)
        """
        pass

    @setting.counter
    def set_angular_velocity(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_angular_velocity( (Actor)arg1, (Vector3D)vector) -> None :
        
            C++ signature :
                void set_angular_velocity(class carla::client::Actor {lvalue},class carla::geom::Vector3D)
        """
        pass

    @setting.counter
    def set_location(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_location( (Actor)arg1, (Location)location) -> None :
        
            C++ signature :
                void set_location(class carla::client::Actor {lvalue},class carla::geom::Location)
        """
        pass

    @setting.counter
    def set_simulate_physics(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_simulate_physics( (Actor)arg1 [, (bool)enabled=True]) -> None :
        
            C++ signature :
                void set_simulate_physics(class carla::client::Actor {lvalue} [,bool=True])
        """
        pass

    @setting.counter
    def set_transform(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_transform( (Actor)arg1, (Transform)transform) -> None :
        
            C++ signature :
                void set_transform(class carla::client::Actor {lvalue},class carla::geom::Transform)
        """
        pass

    @setting.counter
    def set_velocity(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_velocity( (Actor)arg1, (Vector3D)vector) -> None :
        
            C++ signature :
                void set_velocity(class carla::client::Actor {lvalue},class carla::geom::Vector3D)
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

    def __str__(self, Actor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __str__( (Actor)arg1) -> object :
        
            C++ signature :
                struct _object * __ptr64 __str__(class carla::client::Actor {lvalue})
        """
        pass

    attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_alive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    semantic_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



