from rum.Interceptor import Interceptor
from rum.Interjector import Interjector
from rum.statemachine.States import StateMachine

class FunctionalComponentRUM(Interceptor, StateMachine):    

    def __init__(self, lightWeight = True):
        Interceptor.__init__(self, lightWeight)   
        StateMachine.__init__(self)

class OptimizerRUM(Interjector):
    
    def __init__(self, optimizer = None, queryModule = None):
        Interjector.__init__(self)
        self.optimizer = optimizer
        self.queryModule = queryModule
        self.simulations = {}  
                
    def query(self, RUM, destination, singleResult = False):
        return self.queryModule.query(RUM, destination)
    
    def getStateByName(self, RUM, name):
        if name in RUM.states.keys():
            return RUM.states[name]
        else:
            return None
        
    def getStateByIndex(self, RUM, index):
        if len(RUM.states.values()) > index:
            i = 0
            for state in RUM.states:
                if i == index:
                    return RUM.states[state]
                else:
                    i+=1
        else:
            return None
        
    def getStateNames(self, RUM):
        return RUM.states.keys()
    
    def getStatesDictionary(self, RUM):
        return RUM.states
    
    def getStatesList(self, RUM):
        result = []
        for state in RUM.states:
            result.append(RUM.states[state])
        return result
    
    def getPossibleStateTransitions(self, RUM):
        return RUM.currentState.__exit_guards__
    
    def getPossibleNextStates(self, RUM):
        return RUM.currentState.__nextStates__
    
    '''the simulation methods can be used by an optimizer to temporarily change
    the state of a RUM, and to change the value of a field of one of a component.
    These changes are undone by calling the endSimultions method'''
    def startSimulationOnRUM(self, RUM):
        self.simulations[RUM] = RUM.currentState
    
    def startSimulationOnComponent(self, component, field, value):
        self.simulations[(component, field)] = value
        
    def endSimulations(self):
        for key in self.simulations:
            if isinstance(key, RUM):
                key.currentState = self.simulations[key]
            else:
                setattr(key[0], key[1], self.simulations[key])
    
    
class RUM(FunctionalComponentRUM, OptimizerRUM):
    
    def __init__(self, lightWeight = True, optimizer = None, queryModule = None):
        FunctionalComponentRUM.__init__(self, lightWeight)
        OptimizerRUM.__init__(self, optimizer, queryModule)        
    
    def __setupStates__(self):
        return    