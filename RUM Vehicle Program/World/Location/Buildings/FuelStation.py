from World.Location.Buildings.Building import Building

class FuelStation(Building):

    def __init__(self, name, location):
        Building.__init__(self, name, location)
        
    def getFuel(self, amount):
        return amount
        