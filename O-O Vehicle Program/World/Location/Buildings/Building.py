from World.Location.Buildings.AbstractBuilding import AbstractBuilding

class Building(AbstractBuilding):

    def __init__(self, name, location):
        AbstractBuilding.__init__(self, name, location)        
        
    def removePackage(self, package):
        if package in self.packages:
            self.packages.remove(package)
        
    def addPackage(self, package):
        self.packages.append(package)
        
    def getLocation(self):
        return self.location