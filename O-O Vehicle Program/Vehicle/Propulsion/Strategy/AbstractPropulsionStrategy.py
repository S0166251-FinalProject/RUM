
class AbstractPropulsionStrategy(object):

    def __init__(self, propulsion, gearbox, vehicle):        
        self.propulsion = propulsion
        self.gearbox = gearbox
        self.vehicle = vehicle

    def __determineOptimalGearThrottleCombination__(self):
        currentGear = self.gearbox.gear
        currentPropulsion = self.propulsion.getThrottle()
        road = self.vehicle.getRoutePlanner().getNextRoad()
        
        desiredCombination = self.__determineOptimalCombination__(road)
        self.gearbox.gear = currentGear
        self.propulsion.throttle = currentPropulsion
        
        return desiredCombination
        