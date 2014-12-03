from Vehicle.Propulsion.Strategy.AbstractPropulsionStrategy import AbstractPropulsionStrategy

class EfficiencyPropulsionStrategy(AbstractPropulsionStrategy):

    def __init__(self, propulsion, gearbox, vehicle):
        AbstractPropulsionStrategy.__init__(self, propulsion, gearbox, vehicle)
     
    def incThrottle(self, amount):
        combination = self.__determineOptimalGearThrottleCombination__()
        if combination != None:
            desiredThrottle = combination[1]
            if desiredThrottle != self.propulsion.throttle:
                self.propulsion.throttle = desiredThrottle
        
    def decThrottle(self, amount):
        combination = self.__determineOptimalGearThrottleCombination__()
        if combination != None:
            desiredThrottle = combination[1]
            if desiredThrottle != self.propulsion.throttle:
                self.propulsion.throttle = desiredThrottle
        
    def stop(self):
        self.propulsion.throttle = self.propulsion.minThrottle
        self.propulsion.engineOff()

    def __determineOptimalCombination__(self, road):
        minSpeed = road.getMinSpeed()
        maxSpeed = road.getMaxSpeed()
        i = 1
        combination = None
        while i <= self.gearbox.maximumGear:
            self.gearbox.gear = i
            t = 1
            bestEfficiency = 0
            while t <= 100:         
                self.propulsion.throttle = t 
                speed = self.vehicle.getSpeed()
                consumption = self.propulsion.getConsumption()         
                efficiency = speed/consumption  
                if speed >= minSpeed and speed <= maxSpeed and efficiency > bestEfficiency:
                    bestEfficiency = efficiency
                    combination = (self.gearbox.gear, self.propulsion.throttle)                    
                t+=1
            i+=1
        return combination          