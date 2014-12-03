from Vehicle.Gearbox.Strategy.AbstractGearboxStrategy import AbstractGearboxStrategy

class ManualGearboxStrategy(AbstractGearboxStrategy):

    def __init__(self, gearbox, propulsion, vehicle):
        AbstractGearboxStrategy.__init__(self, gearbox, propulsion, vehicle)
        
    def incGear(self):
        self.gearbox.gear = min(self.gearbox.gear+1, self.gearbox.maximumGear)
        
    def decGear(self):
        self.gearbox.gear = max(self.gearbox.gear-1, 1)
        
        