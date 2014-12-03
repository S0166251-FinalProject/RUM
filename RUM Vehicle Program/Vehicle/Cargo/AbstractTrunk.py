import abc
from abc import ABCMeta

class AbstractTrunk(object):
    __metaclass__ = ABCMeta

    '''CC2: 1'''  
    def __init__(self, maximumVolume):
        self.maxVolume = maximumVolume
        self.currentlyUsedVolume = 0
        self.cargo = []
        
    @abc.abstractmethod
    def remainingVolume(self):
        return
    
    @abc.abstractmethod
    def usedVolume(self):
        return
    
    @abc.abstractmethod
    def canAddCargo(self, package):
        return
    
    @abc.abstractmethod
    def addCargo(self, package):
        return
            
    @abc.abstractmethod        
    def removeCargo(self, package):
        return
    
    @abc.abstractmethod        
    def getCargoWeight(self):
        return
    
    @abc.abstractmethod
    def containsPackage(self, package):
        return