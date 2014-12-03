from Vehicle.Fueltank.AbstractFueltank import AbstractFueltank

class Fueltank(AbstractFueltank):
    
    def __init__(self, maxFuel):
        AbstractFueltank.__init__(self, maxFuel)
        
    def full(self):
        return self.fuelLevel==self.maxFuel

    def empty(self):
        return self.fuelLevel==0
    
    def refuel(self, amount):
        self.fuelLevel = min(self.fuelLevel+amount, self.maxFuel)
        
    def consumeFuel(self, amount):
        self.fuelLevel = self.fuelLevel-amount
        
    def canContainExtra(self):
        return self.maxFuel - self.fuelLevel