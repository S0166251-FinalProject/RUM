import abc
from abc import ABCMeta
from World.Weather.Weather import Weather

class AbstractWorld(object):

    __metaclass__ = ABCMeta

    def __init__(self):        
        self.roadNetwork = []
        self.roads = []        
        self.locations = []
        self.weather = Weather()
        
    @abc.abstractmethod         
    def addConnection(self, loc1, loc2, road):
        return
    
    @abc.abstractmethod              
    def addRoad(self, road):
        return
    
    @abc.abstractmethod          
    def addLocation(self, location):
        return
    
    @abc.abstractmethod          
    def findConnection(self, loc1, loc2):
        return
     
    @abc.abstractmethod          
    def driveVehicleTo(self, vehicle, destination, speed):       
        return 
    
    def getVehicleLocation(self, vehicle):
        for location in self.locations:
            if location.containsVehicle(vehicle):
                return location
        return None
