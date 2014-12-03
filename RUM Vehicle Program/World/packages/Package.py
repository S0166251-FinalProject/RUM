from Vehicle.AbstractVehicle import AbstractVehicle

class Package(object):

    def __init__(self, startBuilding, destinationBuilding, weight, volume):
        self.startBuilding = startBuilding
        self.destinationBuilding = destinationBuilding
        self.currentlyContainedIn = startBuilding
        self.weight = weight
        self.volume = volume
        
    def delivered(self):
        return self.currentlyContainedIn == self.destinationBuilding
    
    def inTransit(self):
        return isinstance(self.currentlyContainedIn, AbstractVehicle)
    
    def containedIn(self):
        return self.currentlyContainedIn

    def getCurrentLocation(self): 
        return self.currentlyContainedIn.getLocation()  
    
    def setCurrentlyLocatedIn(self, location):
        self.currentlyContainedIn = location
        
    def getDestination(self):
        return self.destinationBuilding.getLocation()
    
    def getDestinationBuilding(self):
        return self.destinationBuilding
    
    def getWeight(self):
        return self.weight
    
    def getVolume(self):
        return self.volume