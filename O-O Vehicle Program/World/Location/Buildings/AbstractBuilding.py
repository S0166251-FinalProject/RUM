import abc
from abc import ABCMeta

class AbstractBuilding(object):

    __metaclass__ = ABCMeta

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.packages = []        
    
    @abc.abstractmethod 
    def removePackage(self, index):
        return
    
    @abc.abstractmethod   
    def addPackage(self, package):
        return
    
    def getName(self):
        return self.name
    
    def containsPackage(self, package):
        return package in self.packages