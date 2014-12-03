from World.Location.AbstractLocation import AbstractLocation

class Location(AbstractLocation):

    def __init__(self, name):        
        AbstractLocation.__init__(self, name)    
    
    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)
        
    def removeVehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)                   
       
    def containsBuilding(self, building):
        return building in self.buildings
                
    def addBuilding(self, building):
        self.buildings.append(building)              
        
    def getBuilding(self, name):
        for building in self.buildings:
            if building.isBuilding(name, self):
                return building
        return None
    
    def __repr__(self):
        return self.name
        