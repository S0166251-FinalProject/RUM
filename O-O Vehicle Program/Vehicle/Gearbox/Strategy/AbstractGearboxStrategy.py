
class AbstractGearboxStrategy(object):
    
    def __init__(self, gearbox, propulsion, vehicle):
        self.gearbox = gearbox
        self.propulsion = propulsion
        self.vehicle = vehicle

    def __determineOptimalGearThrottleCombination__(self):
        currentGear = self.gearbox.gear
        currentPropulsion = self.propulsion.getThrottle()
        road = self.vehicle.getRoutePlanner().getNextRoad()
        
        desiredCombination = self.__determineOptimalCombination__(road)
        self.gearbox.gear = currentGear
        self.propulsion.throttle = currentPropulsion
        
        return desiredCombination
        