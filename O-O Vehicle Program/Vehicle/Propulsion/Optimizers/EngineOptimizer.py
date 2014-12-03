''' 
    Lines of Code: 10
    Max CC2: 2
    LCOM4: 1
    TCC:
    CBO: 3
    CF:    
'''

from Vehicle.Propulsion.Optimizers.AbstractEngineOptimizer import AbstractEngineOptimizer

class EngineOptimizer(AbstractEngineOptimizer):

    def __init__(self, engine):
        AbstractEngineOptimizer.__init__(self, engine)
        
    def engineOn(self, vehicle):
        if not vehicle.getFuelTank().empty():
            self.engine.engineOn()
   
    def engineOff(self, vehicle): 
        self.engine.engineOff()

    def stop(self, vehicle):
        self.engine.engineOff()