import abc
from abc import ABCMeta
from Vehicle.Propulsion.Strategy.ManualPropulsionStrategy import ManualPropulsionStrategy

class AbstractPropulsion(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.on = False
        self.maxThrottle = 100
        self.minThrottle = 0        
        self.throttle = self.minThrottle
        self.strategy = ManualPropulsionStrategy(self, None, None)
        
    def setStrategy(self, strategy):
        self.strategy = strategy

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
    
    @abc.abstractmethod        
    def getConsumption(self, intake):
        return
    
    @abc.abstractmethod      
    def getRPM(self, intake, weightMod, steepness, weather):
        return
    
    def isOn(self):
        return self.on