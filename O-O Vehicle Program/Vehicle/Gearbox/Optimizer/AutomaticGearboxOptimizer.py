''' 
    Lines of Code: 34
    Max CC2: 5
    LCOM4: 1
    TCC:
    CBO: 2
    CF:    
'''

from threading import Thread
from Vehicle.Gearbox.Optimizer.GearOptimizer import GearOptimizer

class AutomaticGearboxOptimizer(Thread, GearOptimizer):
        
    def __init__(self, vehicle, gearbox):
        Thread.__init__(self, None, None, None, None, None)
        GearOptimizer.__init__(self, gearbox)
        self.gearbox = gearbox
        self.vehicle = vehicle
        self.switchThresholdsUp = {1 : 10,
                                          2 : 20,
                                          3 : 30,
                                          4 : 40,
                                          5 : 50}
        self.switchThresholdsDown = {2 : 9,
                                              3 : 19,
                                              4 : 29,
                                              5 : 39,
                                              6 : 49}
        self.daemon = True
        self.run()

    '''CC2: 5'''         
    def __incGear__(self):
        if(self.gearbox.gear<self.gearbox.maxGears):
            if(self.automatic):            
                if(self.vehicle.getSpeed()>self.switchThresholdsUp.get(self.gearbox.gear)):
                    self.gearbox.gear+=1
            else:
                if(self.vehicle.getSpeed()>self.switchThresholdsUp.get(self.gearbox.gear)):
                    self.gearbox.gear+=1
                    self.automatic = True

    '''CC2: 5'''     
    def __decGear__(self):
        if(self.gearbox.gear>1):
            if(self.automatic):            
                if(self.vehicle.getSpeed()<self.switchThresholdsDown.get(self.gearbox.gear)):
                    self.gearbox.gear-=1
            else:
                if(self.vehicle.getSpeed()<self.switchThresholdsDown.get(self.gearbox.gear)):
                    self.gearbox.gear-=1
                    self.automatic = True
                    
    def processManualSwitch(self):
        self.automatic = False
            
    def run(self):
        while(True) : 
            self.__incGear__()
            self.__decGear__() 
            
    