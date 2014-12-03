from rum.statemachine.Operands import AbstractOperand

class AbstractGuard(object):
    
    @staticmethod
    def getValue(operand, beforeVariables, afterVariables, component, method):            
        if isinstance(operand, Guard):
            return operand.evaluate(beforeVariables, afterVariables, component, method)
        elif isinstance(operand, AbstractOperand):
            return operand.getValue(beforeVariables, afterVariables, component, method)
        else:
            return operand 
        
    def evaluate(self, beforeVariables, afterVariables, component, invokedMethod):
        raise NotImplementedError('classes which inherit from AbstractGuard must implement evaluate(self, beforeVariables, afterVariables, component, invokedMethod)')

    @staticmethod
    def isGuard(node):
        return isinstance(node, AbstractGuard)

class Guard(AbstractGuard):
    
    def __init__(self, operator, leftOperand, rightOperand):
        AbstractGuard.__init__(self)
        self.operator = operator
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand   
        
    def evaluate(self, beforeVariables, afterVariables, component, method): 
        left = self.getValue(self.leftOperand, beforeVariables, afterVariables, component, method)
        right = self.getValue(self.rightOperand, beforeVariables, afterVariables, component, method)
        return self.operator.execute(left, right)             
    
    def getLeft(self):
        return self.leftOperand  
    
    def getRight(self):
        return self.rightOperand
    
    def getOperator(self):
        return self.operator
       
class TrueGuard(AbstractGuard):
    
    def __init__(self):
        AbstractGuard.__init__(self)
       
    def evaluate(self, beforeVariables, afterVariables, component, method):
        return True   
    
class InvokedServiceGuard(AbstractGuard):
    
    def __init__(self, component, service):
        AbstractGuard.__init__(self)
        self.component = component
        self.service = service
        
    def evaluate(self, beforeVariables, afterVariables, component, method):
        return self.service == method and self.component == component
    
    def getComponent(self):
        return self.component
    
    def getService(self):
        return self.service    

class CompositeGuard(AbstractGuard):
    
    def __init__(self):
        AbstractGuard.__init__(self)
        self.guards = []
        
    def getGuards(self):
        return self.guards
    
    def addGuard(self, guard):
        if not guard in self.guards:
            self.guards.append(guard)
    
class AndGuard(CompositeGuard):
    
    def __init__(self):
        CompositeGuard.__init__(self)
    
    def evaluate(self, beforeVariables, afterVariables, component, method):
        result = True
        for guard in self.guards:
            result &= guard.evaluate(beforeVariables, afterVariables, component, method)
        return result
    
class OrGuard(CompositeGuard):
    
    def __init__(self):
        CompositeGuard.__init__(self)    
            
    def evaluate(self, beforeVariables, afterVariables, component, method):        
        for guard in self.guards:
            if guard.evaluate(beforeVariables, afterVariables, component, method):
                return True
        return False
