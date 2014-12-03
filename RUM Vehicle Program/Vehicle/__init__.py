from World.WorldFactory import *
from Vehicle.VehicleFactory import *
from Controller.VehicleController import VehicleController

def main():
    wFactory = WorldFactory()
    vFactory = VehicleFactory()
    world = wFactory.CreateWorld()
    vehicle = vFactory.CreateSpeedyVehicle(6, 50, 25, False, 2.09, world, [])
    wFactory.CreateAndDeployPackages(5, world, vehicle)    
    world.locations[0].addVehicle(vehicle)
    vehicle.getRoutePlanner().setCurrentLocation(world.locations[0])
    
    controller = VehicleController(vehicle, world)
    startingFuel = vehicle.getFuelTank().fuelLevel
    
    while not vehicle.getRoutePlanner().allPackagesAreDelivered():
        package = vehicle.getRoutePlanner().getNearestUndeliveredPackage()
        print('picking up package')
        controller.pickup(package)
        print('delivering package')
        controller.deliver(package)
    print(startingFuel)
    print(vehicle.getFuelTank().fuelLevel)
    print('fuel consumed = '+(startingFuel - vehicle.getFuelTank().fuelLevel).__repr__())
    

if __name__ == "__main__":
    main()