from Vehicle.Cargo.AbstractTrunk import AbstractTrunk
        
class Trunk(AbstractTrunk):
   
    '''CC2: 1''' 
    def __init__(self, maximumVolume):
        AbstractTrunk.__init__(self, maximumVolume)
    
    '''CC2: 1'''         
    def remainingVolume(self):
        return self.maxVolume - self.currentlyUsedVolume;

    '''CC2: 1'''     
    def usedVolume(self):
        return self.currentlyUsedVolume

    '''CC2: 1'''     
    def canAddCargo(self, package):
        return self.remainingVolume() > package.getVolume()

    '''CC2: 2'''     
    def addCargo(self, package):
        if self.canAddCargo(package):
            self.currentlyUsedVolume += package.getVolume()
            self.cargo.append(package)
    
    '''CC2: 2'''             
    def removeCargo(self, package):
        try:
            self.cargo.remove(package)
            self.currentlyUsedVolume -= package.getVolume()
        except ValueError:
            print('error, cannot remove a package from the trunk since it is not contained within it')

    '''CC2: 1'''             
    def getCargoWeight(self):
        weight = 0
        for package in self.cargo:
            weight += package.getWeight()
        return weight
 
    '''CC2: 1'''    
    def containsPackage(self, package):
        return package in self.cargo
            