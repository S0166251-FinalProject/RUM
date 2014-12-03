import abc
from abc import ABCMeta
from Vehicle.Gearbox.Strategy.ManualGearboxStrategy import ManualGearboxStrategy

class AbstractGearbox(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, maxGears):        
        self.maximumGear = min(maxGears, 6)
        self.gear = 1  
        self.strategy = ManualGearboxStrategy(self, None, None)
        
    @abc.abstractmethod
    def incGear(self):
        return
    
    @abc.abstractmethod
    def decGear(self):
        return
    
    @abc.abstractmethod
    def getRotation(self, RPM):
        return    
    
    @abc.abstractmethod   
    def GetRequiredRPMFor(self, GRPM):
        return
        
    def getMaxGears(self):
        return self.maximumGear
    
    def getCurrentGear(self):
        return self.gear
    
    def setStrategy(self, strategy):
        self.strategy = strategy