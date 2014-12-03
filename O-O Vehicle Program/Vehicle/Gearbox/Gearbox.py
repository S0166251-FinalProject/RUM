from Vehicle.Gearbox.AbstractGearbox import AbstractGearbox

class Gearbox(AbstractGearbox): 

    def __init__(self, maxGears):
        AbstractGearbox.__init__(self, maxGears)
        self.differentialRatio = 3.42  
        self.ratio = {1 : 2.97,
                        2 : 2.07,
                        3 : 1.43,
                        4 : 1.0,
                        5 : 0.84,
                        6 : 0.56}
        
    def incGear(self):
        self.strategy.incGear()
        
    def decGear(self):
        self.strategy.decGear()
        
    def getRotation(self, RPM):
        return RPM/self.differentialRatio/self.ratio.get(self.gear)      
