from World.Road.AbstractRoad import AbstractRoad

class Road(AbstractRoad):

    def __init__(self, name, steepness, distance, minSpeed, maxSpeed):
        AbstractRoad.__init__(self, name, steepness, distance, minSpeed, maxSpeed)    
    
    def getSteepness(self, reverted):
        if reverted:
            return self.steepness*-1
        else:
            return self.steepness
      
    def getDistance(self):
        return self.distance
        
    def getMinSpeed(self):
        return self.minSpeed
        
    def getMaxSpeed(self):
        return self.maxSpeed
    
    def __repr__(self):
        return self.name
        