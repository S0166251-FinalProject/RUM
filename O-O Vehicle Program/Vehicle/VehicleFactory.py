from Vehicle.Gearbox.Gearbox import Gearbox
from Vehicle.Fueltank.Fueltank import Fueltank
from Vehicle.Cargo.Trunk import Trunk
from Vehicle.Propulsion.Propulsion import Propulsion
from Vehicle.DeliveryVehicle import DeliveryVehicle
from Vehicle.RoutePlanner import RoutePlanner
from Vehicle.Gearbox.Strategy.EfficiencyGearboxStrategy import EfficiencyGearboxStrategy
from Vehicle.Propulsion.Strategy.EfficiencyPropulsionStrategy import EfficiencyPropulsionStrategy

class VehicleFactory(object):

    def __init__(self):
        return
    
    def CreateSpeedyVehicle(self, maxGears, maxFuel, trunkVolume, automatic, circumference, world, packages):  
        '''create the part of the vehicle'''        
        gearbox = Gearbox(maxGears)
        fueltank = Fueltank(maxFuel)
        trunk = Trunk(trunkVolume)
        propulsion = Propulsion()      
        
        '''create world and packages'''
        
        routePlanner = RoutePlanner(world, packages)
        '''create optimizers for these parts, where applicable'''
                
        vehicle = DeliveryVehicle("speedy", propulsion, gearbox, fueltank, routePlanner, trunk, circumference)
        
        gearboxStrategy = EfficiencyGearboxStrategy(gearbox, propulsion, vehicle)
        propulsionStrategy = EfficiencyPropulsionStrategy(propulsion, gearbox, vehicle)
        gearbox.setStrategy(gearboxStrategy)
        propulsion.setStrategy(propulsionStrategy)
        
        return vehicle
    
        
        
        