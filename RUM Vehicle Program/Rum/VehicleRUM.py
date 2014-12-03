from rum.RUM import RUM
from rum.statemachine.States import State
from rum.statemachine.Guards import *
from rum.statemachine.Operators import *
from rum.statemachine.Operands import *

class VehicleRUM(RUM):

    def __init__(self, vehicle, gearboxRUM, propulsionRUM):
        self.vehicle = vehicle
        self.gearboxRUM = gearboxRUM
        self.propulsionRUM = propulsionRUM
        RUM.__init__(self)
        
    def __setupStates__(self):
        self.addState(VehicleState('Standard', self.vehicle, self.gearboxRUM, self.propulsionRUM))
        self.setInitialState('Standard')        
    
    def getSpeed(self):
        return self.currentState.getSpeed()
    
class VehicleState(State):
    
    def __init__(self, name, vehicle, gearboxRUM, propulsionRUM):
        State.__init__(self, name)
        self.vehicle = vehicle
        self.propulsionRUM = propulsionRUM
        self.gearboxRUM = gearboxRUM
        
    def getSpeed(self):
        routePlanner = self.vehicle.getRoutePlanner()
        weather = routePlanner.getWorld().getWeather()
        steepness = routePlanner.getNextRoadSteepness()
        weightMod = self.vehicle.getWeightMod()
        return self.gearboxRUM.getRotation(self.propulsionRUM.getRPM(weightMod, steepness, weather))*self.vehicle.getWheelCircumference()/1000.0*60
    
    def __setupStateTransitions__(self, states):
        return
    
    