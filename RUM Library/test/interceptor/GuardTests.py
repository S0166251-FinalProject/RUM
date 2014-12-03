from test.BaseTest import BaseTest
from rum.RUM import RUM
from rum.statemachine.States import State
from rum.statemachine.Guards import *
from rum.statemachine.Operators import *


class InvokedServiceGuardTest(BaseTest):

    def __init__(self):
        BaseTest.__init__(self, "InvokedServiceGuardTest", "TrueFalseFalseFalse")
        self.comp = Component()
        self.other = Component()
        self.g1 = InvokedServiceGuard(self.comp, self.comp.setA)
    
    def execute(self):
        result = self.g1.evaluate([], [], self.comp, self.comp.setA).__repr__()
        result += self.g1.evaluate([], [], self.comp, self.comp.setB).__repr__()
        result += self.g1.evaluate([], [], self.comp, self.other.setA).__repr__()
        result += self.g1.evaluate([], [], self.other, self.other.setB).__repr__()
        BaseTest.execute(self, result)
        
class AndGuardTest(BaseTest):

    def __init__(self):
        BaseTest.__init__(self, "AndGuardTest", "TrueFalseFalseFalse")
        self.comp = Component()
        self.other = Component()
        g1 = InvokedServiceGuard(self.comp, self.comp.setA)
        g2 = Guard(EqualsOperator(), 1, 1)
        self.guard = AndGuard()
        self.guard.addGuard(g1)
        self.guard.addGuard(g2)
    
    def execute(self):
        result = self.guard.evaluate([], [], self.comp, self.comp.setA).__repr__()
        result += self.guard.evaluate([], [], self.comp, self.comp.setB).__repr__()
        result += self.guard.evaluate([], [], self.comp, self.other.setA).__repr__()
        result += self.guard.evaluate([], [], self.other, self.other.setB).__repr__()
        BaseTest.execute(self, result)
        
class OrGuardTest(BaseTest):

    def __init__(self):
        BaseTest.__init__(self, "InvokedServiceGuardTest", "TrueFalseFalseTrue")
        self.comp = Component()
        self.other = Component()
        g1 = InvokedServiceGuard(self.comp, self.comp.setA)
        g2 = InvokedServiceGuard(self.other, self.other.setB)
        self.guard = OrGuard()
        self.guard.addGuard(g1)
        self.guard.addGuard(g2)
    
    def execute(self):
        result = self.guard.evaluate([], [], self.comp, self.comp.setA).__repr__()
        result += self.guard.evaluate([], [], self.comp, self.comp.setB).__repr__()
        result += self.guard.evaluate([], [], self.comp, self.other.setA).__repr__()
        result += self.guard.evaluate([], [], self.other, self.other.setB).__repr__()
        BaseTest.execute(self, result)
        
class GuardTest(BaseTest):
    
    def __init__(self):
        BaseTest.__init__(self, "GuardTest", "FalseTrue")
        self.comp = Component()
        self.g1 = Guard(EqualsOperator(), 1, 5)
        self.g2 = Guard(EqualsOperator(), 1, 1)
    
    def execute(self):
        result = self.g1.evaluate([], [], self.comp, self.comp.setA).__repr__()
        result += self.g2.evaluate([], [], self.comp, self.comp.setB).__repr__()
        BaseTest.execute(self, result)

class Component(object):
        
    def __init__(self):
        self.x = 'A'
        
    def setA(self):
        self.x = 'A'
        
    def setB(self):
        self.x = 'B'
        
    def getX(self):
        return self.x
    
    def getY(self, bla):
        return bla
        