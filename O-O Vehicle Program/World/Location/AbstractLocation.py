import abc
from abc import ABCMeta
from World.Location.Buildings.FuelStation import FuelStation

class AbstractLocation(object):

    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name        
        self.vehicles = []        
        self.buildings = []
        
    @abc.abstractmethod     
    def addVehicle(self, vehicle):
        return
    
    @abc.abstractmethod         
    def removeVehicle(self, vehicle):
        return 
    
    @abc.abstractmethod       
    def getBuilding(self, name):
        return
    
    @abc.abstractmethod         
    def addBuilding(self, building):
        return
    
    def getBuildings(self):
        return self.buildings    
        
    def containsFuelStation(self):
        for building in self.buildings:
            if type(building) is FuelStation:
                return True
        return False
    
    def getFuelStation(self):
        for building in self.buildings:
            if type(building) is FuelStation:
                return building
        return None     
    
    def containsVehicle(self, vehicle):
        return vehicle in self.vehicles
    
        
        