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

class AbstractThrottleOptimizer(object):

    __metaclass__ = ABCMeta

    def __init__(self, throttle):
        self.throttle = throttle
        
    @abc.abstractmethod   
    def incThrottle(self, vehicle, amount):
        return

    @abc.abstractmethod   
    def decThrottle(self, vehicle, amount):
        return

    @abc.abstractmethod   
    def stop(self, vehicle):
        return
