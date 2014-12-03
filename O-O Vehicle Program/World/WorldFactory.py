from World.World import World
from World.Location.Location import Location
from World.Location.Buildings.FuelStation import FuelStation
from World.Road.Road import Road
from World.packages.Package import Package
from World.packages.PackageManager import PackageManager
from World.Location.Buildings.Building import Building
import random

class WorldFactory(object):

    def __init__(self):
        return
    
    def CreateWorld(self):
        l1 = Location("A")
        l1.addBuilding(Building("B1", l1))
        l2 = Location("B")
        l2.addBuilding(Building("B2", l2))
        l3 = Location("C")
        l3.addBuilding(Building("B3", l3))
        l4 = Location("D")
        l4.addBuilding(Building("B4", l4))
        l5 = Location("E")
        l5.addBuilding(Building("B5", l5))
        l6 = Location("F")
        l6.addBuilding(Building("B6", l6))
        l7 = Location("G")
        l7.addBuilding(Building("B7", l7))
        l8 = Location("H")
        l8.addBuilding(Building("B8", l8))
        l9 = Location("I")
        l9.addBuilding(Building("B9", l9))
        l10 = Location("J")
        l10.addBuilding(Building("B10", l10))
        l11 = Location("K")
        l11.addBuilding(Building("B11", l11))
        l12 = Location("L")
        l12.addBuilding(Building("B12", l12))  
        f1 = Location("M")
        f1.addBuilding(FuelStation("Fuelstation 1", f1))
        f2 = Location("N")
        f2.addBuilding(FuelStation("Fuelstation 2", f2))
    
        'create the roads connecting these locations'
        r1 = Road("R1", 0, 20, 120, 180)
        r2 = Road("R2", 0, 40, 40, 60)    
        r3 = Road("R3", 0, 35, 30, 50)    
        r4 = Road("R4", 0, 20, 60, 80)
        r5 = Road("R5", 15, 18, 30, 45)    
        r6 = Road("R6", 0, 35, 60, 80)
        r7 = Road("R7", 0, 60, 100, 140)    
        r8 = Road("R8", 0, 15, 50, 60)    
        r9 = Road("R9", 10, 50, 50, 60)
        r10 = Road("R10", 0, 53, 100, 140)    
        r11 = Road("R11", 10, 12, 30, 50)
        r12 = Road("R12", 5, 5, 60, 80) 
        r13 = Road("R13", -12, 8, 30, 45)
        r14 = Road("R14", -30, 10, 10, 30)
        r15 = Road("R15", 5, 5, 60, 80)
        r16 = Road("R16", -20, 12, 30, 40)
        r17 = Road("R17", 0, 10, 60, 90)
        r18 = Road("R18", 0, 20, 60, 90)
        r19 = Road("R19", 0, 120, 120, 180)    
    
        'add the roads to the locations, to they know which roads they have and which locations they border'        
        world = World()
        world.addConnection(l1, l2, r1)
        world.addConnection(l1, l3, r2)
        world.addConnection(l1, l4, r3)
        world.addConnection(l2, l3, r4)
        world.addConnection(l2, l9, r5)
        world.addConnection(l3, l4, r6)
        world.addConnection(l3, l10, r7)
        world.addConnection(l4, l5, r8)
        world.addConnection(l5, l6, r9)
        world.addConnection(l5, l11, r10)
        world.addConnection(l6, l7, r11)
        world.addConnection(l6, f2, r12)
        world.addConnection(l7, l8, r13)
        world.addConnection(l8, l11, r14)
        world.addConnection(l8, f2, r15)
        world.addConnection(l9, l10, r16)
        world.addConnection(l10, f1, r17)
        world.addConnection(l11, f1, r18)
        world.addConnection(l11, l12, r19)
           
        return world   
        
    
    def CreateAndDeployPackages(self, amount, world, vehicle):
        routePlanner = vehicle.getRoutePlanner()
        locations = world.getLocations()
        buildings = []
        for location in locations:
            for building in location.getBuildings():
                buildings.append(building)   
        
        manager = PackageManager()    
        vehicle.getRoutePlanner().setPackageManager(manager)
        
        i = 0
        while i < amount:
            loc = random.randrange(0, len(locations)-1, 1)
            dest = random.randrange(0, len(locations)-1, 1)  
            weight = random.randrange(0, 100, 10)
            volume = random.randrange(0, 20, 1)
            package = Package(buildings[loc], buildings[dest], weight, volume)    
            buildings[loc].addPackage(package)         
            manager.addPackage(package)
            i += 1
        