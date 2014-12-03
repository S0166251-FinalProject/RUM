from World.AbstractWorld import AbstractWorld

class World(AbstractWorld):

    def __init__(self):
        AbstractWorld.__init__(self)
        
    def addConnection(self, loc1, loc2, road):
        tempTuple = loc1, loc2, road
        '''add the locations and road to the corresponding lists, in case they aren't in them yet
        the corresponding add methods will prevent the creation of duplicates, so no need to check for it here'''
        self.addLocation(loc1)
        self.addLocation(loc2)
        self.addRoad(road)
        if tempTuple not in self.roadNetwork:
            self.roadNetwork.append(tempTuple)
        
    def addRoad(self, road):
        if road not in self.roads:
            self.roads.append(road)
        
    def addLocation(self, location):
        if location not in self.locations:
            self.locations.append(location)
            
    def findConnection(self, loc1, loc2):
        for connection in self.roadNetwork:
            if (connection[0] == loc1 and connection[1] == loc2) or (connection[1] == loc1 and connection[0] == loc2):
                return connection
        return None
            
    def driveVehicleTo(self, vehicle, destination):
        speed = vehicle.getSpeed()
        currentLoc = vehicle.getCurrentLocation()
        connection = self.findConnection(currentLoc, destination)
        if connection != None:
            distance = connection[2].getDistance()
            resistance = self.determineResistanceForRoad(connection, currentLoc)
            effectiveSpeed = speed/resistance
            if effectiveSpeed <= 0:
                return 0            
            time = distance/effectiveSpeed*3600
            currentLoc.removeVehicle(vehicle)
            destination.addVehicle(vehicle)
            '''now that the vehicle has moved, determine if the weather has changed'''
            self.weather.determineWeather()
            return time
        else:
            return 0
        
    def determineResistanceForRoad(self, connection, currentLoc):
        resistance = connection[2].getSteepness(connection[1] == currentLoc)
        resistance += self.weather.getResistance()
        resistance = 1+resistance/100
        return resistance
    
    def getSteepness(self, currentLocation, road):
        connection = [item for item in self.roadNetwork if road in item and currentLocation in item]
        return road.getSteepness(connection[0][1] == currentLocation)        
        
    def getAvailableRoadsAt(self, location):
        available = []
        for connection in self.roadNetwork:
            if connection[0] == location:
                available.append((connection[1], connection[2]))
            elif connection[1] == location:
                available.append((connection[0], connection[2]))
        return available
        
    def getLocations(self):
        return self.locations    
    
    def getWeather(self):
        return self.weather

        