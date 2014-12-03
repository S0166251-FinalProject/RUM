''' 
    Lines of Code: 49
    Max CC2: 5
    LCOM4: 1
    TCC:
    CBO: 9
    CF:    
'''

from Vehicle.Driver.StandardDriver import StandardDriver

class SpeedyDriver(StandardDriver):

    def __init__(self):
        StandardDriver.__init__(self)
        
    '''CC2: 1'''         
    def driveTo(self, destination, vehicle):
        routePlanner = vehicle.getRoutePlanner()            
        route = routePlanner.determineFastestRouteTo(destination)            
        routePlanner.setRoute(route)  
        self.drive(vehicle, route) 
        print('arrived at '+destination.__repr__())    
   
    '''CC2: 5''' 
    def regulatePropulsion(self, vehicle):
        routePlanner = vehicle.getRoutePlanner()
        world = routePlanner.getWorld()
        destination = routePlanner.getNextStop()
        connection = world.findConnection(routePlanner.getCurrentLocation(), destination)
        resistance = world.determineResistanceForRoad(connection, routePlanner.getCurrentLocation())
        maxSpeed = connection[2].getMaxSpeed()*resistance
        vehicle.engineOn()       
        '''determine desired throttle and gear'''    
        desiredGear = self.determineDesiredGear(maxSpeed, vehicle)
        desiredThrottle = self.determineDesiredThrottle(world, maxSpeed, routePlanner.getNextRoadSteepness(), desiredGear, vehicle)
        '''then set throttle and gear to those numbers'''
        if vehicle.getGearbox().getCurrentGear() > desiredGear:                
            vehicle.decThrottle(100)
            while vehicle.getGearbox().getCurrentGear() > desiredGear: 
                vehicle.decGear()
        elif vehicle.getGearbox().getCurrentGear() < desiredGear:
            vehicle.incThrottle(100)
            while vehicle.getGearbox().getCurrentGear() < desiredGear:     
                vehicle.incGear()
                    
        if vehicle.getThrottle().getThrottle() < desiredThrottle:
            vehicle.incThrottle(desiredThrottle - vehicle.getThrottle().getThrottle())
        elif vehicle.getThrottle().getThrottle() > desiredThrottle:
            vehicle.decThrottle(vehicle.getThrottle().getThrottle() - desiredThrottle)  
        
        print("speed set to: "+vehicle.getSpeed().__repr__())
    
    '''CC2: 2'''                
    def determineDesiredGear(self, desiredSpeed, vehicle):
        threshold = vehicle.gearStrategy.switchThresholdsUp
        gear = 1
        for t in threshold:
            if desiredSpeed >= threshold[t]:
                gear +=1        
        return gear
    
    '''CC2: 1'''     
    def determineDesiredThrottle(self, world, desiredSpeed, steepness, desiredGear, vehicle):
        cargoModifier = (100-vehicle.getTrunk().getCargoWeight()/50)/100
        gearboxRPM = desiredSpeed/60*1000.0/vehicle.getWheelCircumference()        
        gearbox = vehicle.getGearbox()
        currGear = gearbox.gear
        gearbox.gear = desiredGear        
        RPM = gearbox.GetRequiredRPMFor(gearboxRPM)
        desiredThrottle = vehicle.getEngine().getRequiredThrottleForRPM(RPM, cargoModifier, steepness, world.getWeather())
        gearbox.gear = currGear
        return desiredThrottle 
   
        
        
    