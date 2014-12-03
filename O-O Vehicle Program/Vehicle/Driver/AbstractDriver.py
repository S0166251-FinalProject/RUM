''' 
    Lines of Code: 7
    Max CC2: 1
    LCOM4: -
    TCC:
    CBO: 2
    CF:    
'''

import abc
from abc import ABCMeta

class AbstractDriver(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        return
    
    @abc.abstractmethod    
    def driveTo(self, destination, vehicle):
        return
        
        