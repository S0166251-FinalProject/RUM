from Vehicle.AbstractVehicle import AbstractVehicle

class DeliveryVehicle(AbstractVehicle):
    
    def __init__(self, name, propulsion, gearbox, fueltank, routePlanner, trunk, circumference):
        AbstractVehicle.__init__(self, name, propulsion, gearbox, fueltank, routePlanner, trunk, circumference)
        
    def getSpeed(self):
        if self.propulsion.getThrottle() == 0 or not self.propulsion.isOn():
            return 0
        cargoModifier = (100-self.trunk.getCargoWeight()/50)/100
        steepness = self.routePlanner.getNextRoadSteepness()
        return self.gearbox.getRotation(self.propulsion.getRPM(cargoModifier, steepness, self.routePlanner.getWorld().getWeather()))*self.wheelCircumference/1000.0*60
            
    def driveTo(self, destination):        
        world = self.getRoutePlanner().getWorld()
        connection = world.findConnection(self.routePlanner.getCurrentLocation(), destination)
        if connection != None: 
            time = world.driveVehicleTo(self, destination)
            if time >0:
                consumption = self.propulsion.getConsumption()
                self.consumeFuel(consumption*time/3600)
                self.routePlanner.setCurrentLocation(destination)