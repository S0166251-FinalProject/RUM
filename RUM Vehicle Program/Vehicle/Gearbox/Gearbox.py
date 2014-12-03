from Vehicle.Gearbox.AbstractGearbox import AbstractGearbox

class Gearbox(AbstractGearbox): 

    def __init__(self, maxGears):
        AbstractGearbox.__init__(self, maxGears)
        
    def incGear(self):
        self.gear = min(self.gear+1, self.maximumGear)
        
    def decGear(self):
        self.gear = max(self.gear-1, 1)
