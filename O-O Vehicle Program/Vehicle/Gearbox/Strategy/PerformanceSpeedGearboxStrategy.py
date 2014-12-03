from Vehicle.Gearbox.Strategy.AbstractGearboxStrategy import AbstractGearboxStrategy

class PerformanceSpeedGearboxStrategy(AbstractGearboxStrategy):

    def __init__(self, gearbox, propulsion, vehicle):
        AbstractGearboxStrategy.__init__(self, gearbox, propulsion, vehicle)
        
    def incGear(self):
        combination = self.__determineOptimalGearThrottleCombination__()
        desiredGear = combination[0]
        if desiredGear != self.gearbox.gear:
            self.gearbox.gear = desiredGear        
        
    def decGear(self):
        combination = self.__determineOptimalGearThrottleCombination__()
        desiredGear = combination[0]
        if desiredGear != self.gearbox.gear:
            self.gearbox.gear = desiredGear
        
    def __determineOptimalCombination__(self, road):
        minSpeed = road.getMinSpeed()
        maxSpeed = road.getMaxSpeed()
        i = 1
        combination = None
        while i <= self.gearbox.maximumGears:            
            self.gearbox.gear = i
            t = 1
            bestSpeed = 0
            bestEfficiency = 0
            while t <= 100:         
                self.propulsion.throttle = t 
                speed = self.vehicle.getSpeed()
                consumption = self.propulsion.getConsumption()         
                efficiency = speed/consumption  
                if speed >= minSpeed and speed <= maxSpeed:
                    if speed > bestSpeed or (speed == bestSpeed and efficiency > bestEfficiency):
                        bestSpeed = speed
                        bestEfficiency = efficiency
                        combination = (self.gearbox.gear, self.propulsion.throttle)   
                t+=1
            i+=1
        return combination    
        