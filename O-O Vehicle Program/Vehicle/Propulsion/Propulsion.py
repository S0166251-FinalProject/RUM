from Vehicle.Propulsion.AbstractPropulsion import AbstractPropulsion

class Propulsion(AbstractPropulsion):

    def __init__(self):
        AbstractPropulsion.__init__(self)
        
    def engineOn(self):
        self.on = True

    def engineOff(self):
        self.on = False
        
    def incThrottle(self, amount):
        self.strategy.incThrottle(amount)
        
    def decThrottle(self, amount):
        self.strategy.decThrottle(amount)
        
    def stop(self):
        self.strategy.stop()
        
    def getThrottle(self):
        return self.throttle
      
    def getConsumption(self):
        if(self.on):
            if self.throttle <=50:
                return (self.throttle/(100.0/19.0)+1)
            else:
                return self.throttle/(100/19)+(self.throttle-50)/(100/30)+1
        else:
            return 0            

    def getRPM(self, weightMod, steepness, weather):
        if self.on:
            resistance = weather.getResistance()+steepness
            resistance = 1+resistance/100        
            return (self.throttle/(100/3100)+900*weightMod)/resistance
        else:
            return 0        