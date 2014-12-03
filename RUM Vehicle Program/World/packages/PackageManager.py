class PackageManager(object):

    def __init__(self):
        self.packages = []
        
    def addPackage(self, package):
        self.packages.append(package)
        
    def getPackages(self):
        return self.packages
    
    def getPackage(self, index):
        return self.packages[index]
    
    def allPackagesAreDelivered(self):        
        return len(self.getUndeliveredPackages()) == 0
    
    def getUndeliveredPackages(self):
        undelivered = []
        for package in self.packages:
            if not package.delivered():
                undelivered.append(package)
        return undelivered
            