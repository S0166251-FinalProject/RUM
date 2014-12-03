import abc
from abc import ABCMeta

class AbstractVehicle():
        
    __metaclass__ = ABCMeta
    
    def __init__(self, name, propulsion, gearbox, fueltank, routePlanner, trunk, circumference):
        self.name = name
        self.propulsion = propulsion
        self.gearbox = gearbox
        self.fueltank = fueltank
        self.routePlanner = routePlanner
        self.trunk = trunk
        self.wheelCircumference = circumference
    
    def incThrottle(self, amount):
        self.propulsion.incThrottle(amount)
        
    def decThrottle(self, amount):
        self.propulsion.decThrottle(amount)
        
    def stop(self):
        self.propulsion.stop()
        
    def engineOn(self):
        self.propulsion.engineOn()
        
    def engineOff(self):
        self.propulsion.engineOff()
        
    def incGear(self):
        self.gearbox.incGear()
        
    def decGear(self):
        self.gearbox.decGear()  
        
    def refuel(self, amount):
        self.fueltank.refuel(amount)    
        
    def consumeFuel(self, amount):
        self.fueltank.consumeFuel(amount)
    
    def removePackage(self, package):
        self.trunk.removeCargo(package)
        
    def addPackage(self, package):        
        if self.trunk.canAddCargo(package):
            self.trunk.addCargo(package)
            
    def getLocation(self):
        return self.routePlanner.getCurrentLocation()
    
    @abc.abstractmethod     
    def driveTo(self, destination):
        return
    
    def getPropulsion(self):
        return self.propulsion
    
    def getGearbox(self):
        return self.gearbox
    
    def getFuelTank(self):
        return self.fueltank
    
    def getRoutePlanner(self):
        return self.routePlanner
    
    def getTrunk(self):
        return self.trunk
    
    def getCurrentLocation(self):
        return self.routePlanner.getCurrentLocation()
    
    def getWheelCircumference(self):
        return self.wheelCircumference    
    
    def containsPackage(self, package):
        return self.trunk.containsPackage(package)
    
    def setCurrentLocation(self, location):
        self.routePlanner.setCurrentLocation(location)
        
    def getWeightMod(self):
        return (100-self.trunk.getCargoWeight()/50)/100
    
        
        