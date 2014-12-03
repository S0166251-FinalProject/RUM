import abc
from abc import ABCMeta

class AbstractFueltank(object):
    __metaclass__ = ABCMeta
            
    def __init__(self, maxFuel):
        self.maxFuel = maxFuel
        self.fuelLevel = maxFuel
    
    @abc.abstractmethod      
    def full(self):
        return

    @abc.abstractmethod
    def empty(self):
        return
    
    @abc.abstractmethod
    def refuel(self, amount):
        return
    
    @abc.abstractmethod        
    def consumeFuel(self, amount):
        return
    
    @abc.abstractmethod 
    def canContainExtra(self):
        return

        