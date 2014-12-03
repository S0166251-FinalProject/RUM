from Vehicle.Optimizers.AbstractOptimizer import AbstractOptimizer

class FuelEfficiencyOptimizer(AbstractOptimizer):
    
    def __init__(self, vehicle, propulsion, gearbox):
        AbstractOptimizer.__init__(self, vehicle, propulsion, gearbox)

    def __determinePossibleCombinations__(self, road):
        minSpeed = road.getMinSpeed()
        maxSpeed = road.getMaxSpeed()
        combinations = []
        gearboxStates = self.RUM.getStatesList(self.gearbox.RUM)
        propulsionStates = self.RUM.getStatesDictionary(self.propulsion.RUM)
        for state in gearboxStates:
            self.gearbox.RUM.currentState = state
            self.propulsion.RUM.currentState = propulsionStates['DrivingNormally']
            self.__determinePossibleCombinationsHelper__(2, 50, minSpeed, maxSpeed, combinations)
            
            self.propulsion.RUM.currentState = propulsionStates['DrivingRapidly']
            self.__determinePossibleCombinationsHelper__(52, 101, minSpeed, maxSpeed, combinations) 
        return combinations
    
    def __determinePossibleCombinationsHelper__(self, start, end, minSpeed, maxSpeed, combinations):
        t = start
        bestEfficiency = 0
        combination = None
        while t <= end:         
            self.propulsion.throttle = t 
            speed = self.vehicle.RUM.getSpeed()
            consumption = self.propulsion.RUM.getConsumption()     
            efficiency = speed/consumption  
            if speed >= minSpeed and speed <= maxSpeed and efficiency > bestEfficiency:
                bestEfficiency = efficiency
                combination = (self.gearbox.RUM.currentState, self.propulsion.RUM.currentState, t-1)
                break
            t+=1
        if combination != None:
            combinations.append(combination)
        
    def __determineOptimalCombination__(self, combinations):
        desiredCombination = combinations[0]
        optimalEfficiency = 0
        optimalSpeed = 0
        for combination in combinations:
            self.gearbox.RUM.currentState = combination[0]
            self.propulsion.RUM.currentState = combination[1]
            self.propulsion.throttle = combination[2]
            consumption = self.propulsion.RUM.getConsumption()
            speed = self.vehicle.RUM.getSpeed()
            efficiency = speed/consumption
            if efficiency > optimalEfficiency:
                optimalEfficiency = efficiency
                optimalSpeed = speed
                desiredCombination = combination
            elif efficiency == optimalEfficiency and speed > optimalSpeed:
                optimalSpeed = speed
                desiredCombination = combination
        return desiredCombination
        
