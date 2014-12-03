from rum.RUM import RUM
from rum.statemachine.States import State
from rum.statemachine.Guards import *
from rum.statemachine.Operators import *
from rum.statemachine.Operands import *

class GearboxRUM(RUM):

    def __init__(self, gearbox):
        self.gearbox = gearbox
        RUM.__init__(self)
        self.registerToServiceInvocation(gearbox, gearbox.incGear)
        self.registerToServiceInvocation(gearbox, gearbox.decGear) 
        
    def __setupStates__(self):
        self.addState(GearboxFirstGearState('First gear', self.gearbox))
        self.addState(GearboxSecondGearState('Second gear', self.gearbox))
        self.addState(GearboxThirdGearState('Third gear', self.gearbox))
        self.addState(GearboxFourthGearState('Fourth gear', self.gearbox))
        self.addState(GearboxFifthGearState('Fifth gear', self.gearbox))
        self.addState(GearboxSixthGearState('Sixth gear', self.gearbox))
        self.setInitialState('First gear')
        
    def getRotation(self, RPM):
        return self.currentState.getRotation(RPM)
          
class AbstractGearboxGearState(State):
    
    def __init__(self, name, ratio):
        State.__init__(self, name)
        self.differentialRatio = 3.42
        self.ratio = ratio
        
    def getRotation(self, RPM):
        'first translate the engine RPM produced into rotation per minute of the transmission'
        TRPM = RPM/self.ratio           
        'then translate the TRPM into rotations of the wheel per minute'
        rotation = TRPM/self.differentialRatio
        return rotation   
        
class GearboxFirstGearState(AbstractGearboxGearState):
  
    def __init__(self, name, gearbox):
        AbstractGearboxGearState.__init__(self, name, 2.97)
        self.gearbox = gearbox
    
    def __setupStateTransitions__(self, states):
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 2   
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )          
        self.addStateTransition(states['Second gear'], guard)
        
class GearboxSecondGearState(AbstractGearboxGearState):
  
    def __init__(self, name, gearbox):
        AbstractGearboxGearState.__init__(self, name, 2.07)
        self.gearbox = gearbox
    
    def __setupStateTransitions__(self, states):
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 1
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )
        self.addStateTransition(states['First gear'], guard)
        
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 3  
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )        
        self.addStateTransition(states['Third gear'], guard)
        
class GearboxThirdGearState(AbstractGearboxGearState):
  
    def __init__(self, name, gearbox):
        AbstractGearboxGearState.__init__(self, name, 1.43)
        self.gearbox = gearbox
    
    def __setupStateTransitions__(self, states):
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 2
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )
        self.addStateTransition(states['Second gear'], guard)
        
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 4
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )        
        self.addStateTransition(states['Fourth gear'], guard)
        
class GearboxFourthGearState(AbstractGearboxGearState):
  
    def __init__(self, name, gearbox):
        AbstractGearboxGearState.__init__(self, name, 1.00)
        self.gearbox = gearbox
    
    def __setupStateTransitions__(self, states):
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 3
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )
        self.addStateTransition(states['Third gear'], guard)
        
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')        
        rightOperand = 5
        guard = Guard(EqualsOperator(), leftOperand, rightOperand)     
        self.addStateTransition(states['Fifth gear'], guard)
        
class GearboxFifthGearState(AbstractGearboxGearState):
  
    def __init__(self, name, gearbox):
        AbstractGearboxGearState.__init__(self, name, 0.84)
        self.gearbox = gearbox
    
    def __setupStateTransitions__(self, states):
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 4
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )
        self.addStateTransition(states['Fourth gear'], guard)
        
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 6
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )
        self.addStateTransition(states['Sixth gear'], guard)
        
class GearboxSixthGearState(AbstractGearboxGearState):
  
    def __init__(self, name, gearbox):
        AbstractGearboxGearState.__init__(self, name, 0.56)
        self.gearbox = gearbox
        
    def __setupStateTransitions__(self, states):
        leftOperand = FieldVariableOperand(self.gearbox, 'gear')
        rightOperand = 5
        guard = Guard(EqualsOperator(), leftOperand, rightOperand )
        self.addStateTransition(states['Fifth gear'], guard)
        
    