import types 
from collections import namedtuple 

class Interceptor(object):
    
    wrappers = {}    
    Service = namedtuple("Service", ["Instance", "methodName"]) 
    
    def __init__(self, lightWeight = True):
        if lightWeight:
            self.__createWrapper__ = Interceptor.__createLightWeightWrapper__
        else:
            self.__createWrapper__ = Interceptor.__createWrapper__

    '''registers the current instance to the interception of the given service invocation.
    If no other instance is registered to this service invocation then a new wrapper is deployed.'''
    def registerToServiceInvocation(self, component, method):
        name = method.__name__
        service = Interceptor.Service(Instance = component, methodName = name)
        if service in Interceptor.wrappers:
            Interceptor.wrappers[service].append(self)
        else:
            wrapper = self.__createWrapper__(component, method)
            wrapper.__name__ = name
            setattr(component, name, types.MethodType(wrapper, self))        
            Interceptor.wrappers[service] = [self]
            
    @staticmethod
    def __createWrapper__(component, method):
        def wrapper(self, *args, **kwargs):
            old = {}
            for var in component.__dict__:
                old[var] = getattr(component, var)       
                
            result = method(*args, **kwargs)
            new = {}
            for var in component.__dict__:
                new[var] = getattr(component, var)
            Interceptor.interceptInvocation(old, new, component, method)
            return result
        return wrapper
    
    @staticmethod
    def __createLightWeightWrapper__(component, method):
        def wrapper(self, *args, **kwargs):
            result = method(*args, **kwargs)
            Interceptor.interceptInvocation({}, {}, component, method)
            return result
        return wrapper    
    
    
    @staticmethod                
    def interceptInvocation(old, new, component, method):
        name = method.__name__
        service = Interceptor.Service(Instance = component, methodName = name)
        if service in Interceptor.wrappers:
            listeningRUMs = Interceptor.wrappers[service]
            for rum in listeningRUMs:
                rum.checkForTransition(old, new, component, method) 
    
    