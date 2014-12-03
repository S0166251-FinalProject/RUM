from Vehicle.Propulsion.AbstractPropulsion import AbstractPropulsion

class Propulsion(AbstractPropulsion):

    def __init__(self):
        AbstractPropulsion.__init__(self)
        
    def engineOn(self):
        self.on = True

    def engineOff(self):
        self.on = False
        
    def incThrottle(self, amount):
        self.throttle = min(self.throttle+amount, 100)
        
    def decThrottle(self, amount):
        self.throttle = max(self.throttle-amount, 0)
        
    def stop(self):
        self.throttle = self.minThrottle
        self.engineOff()
        
    def getThrottle(self):
        return self.throttle