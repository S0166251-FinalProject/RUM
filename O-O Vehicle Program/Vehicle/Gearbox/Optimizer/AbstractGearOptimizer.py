''' 
    Lines of Code: 10
    Max CC2: 1
    LCOM4: -
    TCC:
    CBO:
    CF:    
'''

import abc
from abc import ABCMeta

class AbstractGearOptimizer(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, gearbox): 
        self.gearbox = gearbox  
        
    @abc.abstractmethod        
    def incGear(self, vehicle):
        return
    
    @abc.abstractmethod        
    def decGear(self, vehicle):
        return 

        