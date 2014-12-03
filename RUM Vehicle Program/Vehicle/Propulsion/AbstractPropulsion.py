import abc
from abc import ABCMeta

class AbstractPropulsion():
    __metaclass__ = ABCMeta

    def __init__(self):
        self.on = False
        self.maxThrottle = 100
        self.minThrottle = 0        
        self.throttle = self.minThrottle

    @abc.abstractmethod   
    def incThrottle(self, amount):
        return
    
    @abc.abstractmethod          
    def decThrottle(self, amount):
        return
    
    @abc.abstractmethod      
    def stop(self):
        return
    
    @abc.abstractmethod      
    def getThrottle(self):
        return
        
    @abc.abstractmethod           
    def engineOn(self):
        return
    
    @abc.abstractmethod  
    def engineOff(self):
        return
    
    def isOn(self):
        return self.on