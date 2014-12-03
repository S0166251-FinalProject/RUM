''' 
    Lines of Code: 13
    Max CC2: 3
    LCOM4: 1
    TCC:
    CBO: 2
    CF:    
'''
from Vehicle.Gearbox.Optimizer.AbstractGearOptimizer import AbstractGearOptimizer

class GearOptimizer(AbstractGearOptimizer):

    def __init__(self, gearbox): 
        AbstractGearOptimizer.__init__(self, gearbox)     
        self.switchThresholdsUp = {1 : 10,
                        2 : 15,
                        3 : 30,
                        4 : 40,
                        5 : 60}
        self.switchThresholdsDown = {2 : 9,
                                     3 : 14,
                                     4 : 29,
                                     5 : 39,
                                     6 : 59}
    '''CC2: 3'''        
    def incGear(self, vehicle):
        if self.gearbox.getCurrentGear() < self.gearbox.getMaxGears():
            if self.switchThresholdsUp.get(self.gearbox.getCurrentGear()) < vehicle.getSpeed():
                self.gearbox.incGear()

    '''CC2: 3'''         
    def decGear(self, vehicle):
        if self.gearbox.getCurrentGear() > 1:
            if self.switchThresholdsDown.get(self.gearbox.getCurrentGear()) > vehicle.getSpeed():
                self.gearbox.decGear()     

        