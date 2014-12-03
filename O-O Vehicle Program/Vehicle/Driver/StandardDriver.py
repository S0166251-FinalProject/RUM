''' 
    Lines of Code: 15
    Max CC2: 2
    LCOM4: 1
    TCC:
    CBO: 5
    CF:    
'''

from Vehicle.Driver.AbstractDriver import AbstractDriver

class StandardDriver(AbstractDriver):

    def __init__(self):
        AbstractDriver.__init__(self) 
           
    '''CC2: 2'''    
    def drive(self, vehicle, route):
        world = vehicle.getRoutePlanner().getWorld()
        routePlanner = vehicle.getRoutePlanner()
        routePlanner.setRoute(route)        
        while not routePlanner.atDestination():    
            nextStop = routePlanner.getNextStop()   
            self.regulatePropulsion(vehicle)
            time = world.driveVehicleTo(vehicle, nextStop, vehicle.getSpeed())
            if time >0:
                consumption = vehicle.getEngine().getConsumption(vehicle.getThrottle().getThrottle())
                vehicle.consumeFuel(consumption*time/60)
                vehicle.setCurrentLocation(nextStop)
    


        