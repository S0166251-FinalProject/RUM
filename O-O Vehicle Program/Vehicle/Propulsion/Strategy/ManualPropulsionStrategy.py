from Vehicle.Propulsion.Strategy.AbstractPropulsionStrategy import AbstractPropulsionStrategy

class ManualPropulsionStrategy(AbstractPropulsionStrategy):

    def __init__(self, propulsion, gearbox, vehicle):
        AbstractPropulsionStrategy.__init__(self, propulsion, gearbox, vehicle)
      
    def incThrottle(self, amount):
        self.propulsion.throttle = min(self.propulsion.throttle+amount, 100)
        
    def decThrottle(self, amount):
        self.propulsion.throttle = max(self.propulsion.throttle-amount, 0)
        
    def stop(self):
        self.propulsion.throttle = self.propulsion.minThrottle
        self.propulsion.engineOff()
        