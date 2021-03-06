from test.BaseTest import BaseTest
from rum.RUM import RUM
from rum.statemachine.States import State
from rum.statemachine.Guards import *
from rum.statemachine.Operators import *
from rum.statemachine.Operands import *

class FieldVariableOperandTest(BaseTest):
   
    def __init__(self):
        BaseTest.__init__(self, "FieldVariableOperandTest", "ABAA")
        self.component = Component()   
        self.otherComp = Component()
        self.operand = FieldVariableOperand(self.component, 'x')
        
    def execute(self):        
        old = {}
        for var in self.component.__dict__:
            old[var] = getattr(self.component, var)    
        self.component.setA()
        new = {}
        for var in self.component.__dict__:
            new[var] = getattr(self.component, var)    
        result = self.operand.getValue(old, new, self.component, 'x')
        self.component.setB()
        result += self.operand.getValue([], [], self.component, 'x')
        self.component.setA()
        result += self.operand.getValue([], [], self.component, 'x')        
        old = {}
        for var in self.otherComp.__dict__:
            old[var] = getattr(self.otherComp, var)    
        self.otherComp.setA()
        new = {}
        for var in self.otherComp.__dict__:
            new[var] = getattr(self.otherComp, var)   
        result += self.operand.getValue(old, new, self.component, 'x')        
        BaseTest.execute(self, result)     

class FunctionValueOperandTest(BaseTest):
   
    def __init__(self):
        BaseTest.__init__(self, "FunctionValueOperandTest", "ABAZ")
        self.component = Component()   
        self.otherComp = Component()
        self.operand = FunctionValueOperand(self.component, 'getX') 
        self.otherOperand = FunctionValueOperand(self.component, 'getY')
        
    def execute(self):
        self.component.setA()
        result = self.operand.getCurrentValue()
        self.component.setB()
        result += self.operand.getCurrentValue()
        self.component.setA()
        result += self.operand.getCurrentValue()        
        result += self.otherOperand.getCurrentValue('Z')
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