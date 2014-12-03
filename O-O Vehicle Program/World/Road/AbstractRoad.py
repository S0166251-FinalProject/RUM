import abc
from abc import ABCMeta

class AbstractRoad(object):

    __metaclass__ = ABCMeta

    def __init__(self, name, steepness, distance, minSpeed, maxSpeed):
        self.name = name
        self.steepness = steepness
        self.distance = distance
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
    
    @abc.abstractmethod          
    def getSteepness(self, reverted):
        return
   
    @abc.abstractmethod      
    def getDistance(self):
        return
    
    @abc.abstractmethod      
    def getMinSpeed(self):
        return
    
    @abc.abstractmethod      
    def getMaxSpeed(self):
        return
        
        