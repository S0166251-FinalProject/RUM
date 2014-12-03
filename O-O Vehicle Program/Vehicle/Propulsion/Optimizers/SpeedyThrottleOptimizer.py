''' 
    Lines of Code: 37
    Max CC2: 4
    LCOM4: 1
    TCC:
    CBO: 8
    CF:    
'''

from Vehicle.Propulsion.Optimizers.AbstractThrottleOptimizer import AbstractThrottleOptimizer

class SpeedyThrottleOptimizer(AbstractThrottleOptimizer):

    def __init__(self, throttle):
        AbstractThrottleOptimizer.__init__(self, throttle)
        
    def incThrottle(self, amount, vehicle):
        if vehicle.getSpeed() < vehicle.getRoutePlanner().getMaxAllowedSpeed():
            currentThrottle = self.throttle.getThrottle()
            desiredThrottle = self.determineDesiredThrottle(vehicle)
            self.throttle.incThrottle(desiredThrottle-currentThrottle)
        elif vehicle.getSpeed() > vehicle.getRoutePlanner().getMaxAllowedSpeed():
            self.decThrottle(amount, vehicle)
   
    def decThrottle(self, amount, vehicle): 
        if vehicle.getSpeed() < vehicle.getRoutePlanner().getMaxAllowedSpeed():
            self.incThrottle(amount, vehicle)
        elif vehicle.getSpeed() > vehicle.getRoutePlanner().getMaxAllowedSpeed():
            currentThrottle = self.throttle.getThrottle()
            desiredThrottle = self.determineDesiredThrottle(vehicle)
            if desiredThrottle < 0:
                desiredThrottle = 0
            self.throttle.decThrottle(currentThrottle-desiredThrottle)
            
    def determineDesiredThrottle(self, vehicle):
        cargoModifier = (100-vehicle.getTrunk().getCargoWeight()/50)/100
        routePlanner = vehicle.getRoutePlanner()
        world = routePlanner.getWorld()
        destination = routePlanner.getNextStop()
        resistance = 1
        maxSpeed = 0
        if destination != None:
            connection = world.findConnection(routePlanner.getCurrentLocation(), destination)
            resistance = world.determineResistanceForRoad(connection, routePlanner.getCurrentLocation())
            maxSpeed = connection[2].getMaxSpeed()
        desiredSpeed = maxSpeed * resistance
        gearboxRPM = desiredSpeed/60*1000.0/vehicle.getWheelCircumference()
        RPM = vehicle.getGearbox().GetRequiredRPMFor(gearboxRPM)
        desiredThrottle = vehicle.getEngine().getRequiredThrottleForRPM(RPM, cargoModifier, routePlanner.getNextRoadSteepness(), world.getWeather())
        return desiredThrottle 

    def stop(self, vehicle):
        self.throttle.stop()