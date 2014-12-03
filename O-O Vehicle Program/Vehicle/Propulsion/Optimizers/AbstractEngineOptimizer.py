''' 
    Lines of Code: 13
    Max CC2: 1
    LCOM4: -
    TCC:
    CBO: 1
    CF:    
'''

import abc
from abc import ABCMeta

class AbstractEngineOptimizer(object):

    __metaclass__ = ABCMeta

    def __init__(self, engine):
        self.engine = engine
        
    @abc.abstractmethod   
    def engineOn(self, vehicle):
        return

    @abc.abstractmethod   
    def engineOff(self, vehicle):
        return

    @abc.abstractmethod   
    def stop(self, vehicle):
        return
