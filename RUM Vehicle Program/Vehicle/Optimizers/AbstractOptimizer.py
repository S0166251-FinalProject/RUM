from rum.Query import *
import abc
from abc import ABCMeta

class AbstractOptimizer():

    __metaclass__ = ABCMeta
    
    def __init__(self, vehicle, propulsion, gearbox):
        self.vehicle = vehicle
        self.propulsion = propulsion
        self.gearbox = gearbox
        
    '''CC: 3'''
    def stop(self):
        if self.vehicle.getRoutePlanner().getNextStop() == None and self.propulsion.isOn():
            self.propulsion.stop()   
            
    '''CC: 3'''
    def engineOn(self):
        if self.vehicle.getRoutePlanner().getNextStop() != None and not self.propulsion.isOn():        
            self.propulsion.engineOn()
            
    '''CC: 3'''        
    def engineOff(self):
        if self.vehicle.getRoutePlanner().getNextStop() == None and self.propulsion.isOn():
            self.propulsion.engineOff()
            
    '''CC: 2'''        
    def incThrottle(self, amount):    
        if self.propulsion.isOn():
            self.__determineOptimalGearThrottleCombination__() 
            
    '''CC: 2'''       
    def decThrottle(self, amount):
        if self.propulsion.isOn():
            self.__determineOptimalGearThrottleCombination__() 
            
    '''CC: 2'''    
    def incGear(self):
        if self.propulsion.isOn():
            self.__determineOptimalGearThrottleCombination__() 
            
    '''CC: 2'''    
    def decGear(self):
        if self.propulsion.isOn():
            self.__determineOptimalGearThrottleCombination__() 
            
    '''CC: 1''' 
    def __determineOptimalGearThrottleCombination__(self):
        '''first go through all possible gear states to see how they affect the speed and fuel consumption
        for each gearRUM state, go through all possible propulsionRUM states and throttle values'''
        self.RUM.startSimulationOnRUM(self.gearbox.RUM)
        self.RUM.startSimulationOnRUM(self.propulsion.RUM)
        self.RUM.startSimulationOnComponent(self.propulsion, 'throttle', self.propulsion.throttle)
        
        road = self.vehicle.getRoutePlanner().getNextRoad()
        
        combinations = self.__determinePossibleCombinations__(road)
        desiredCombination = self.__determineOptimalCombination__(combinations)
        
        '''return states and throttle value to original values'''
        self.RUM.endSimulations()
        
        '''now find out how to get the RUMS into the optimal states and execute the required actions'''
        self.__optimizeTowardsDesiredCombination__(desiredCombination)
        
    '''CC: 3'''   
    def __optimizeTowardsDesiredCombination__(self, combination):
        gearboxQuery = self.RUM.query(self.gearbox.RUM, combination[0])
        propulsionQuery = self.RUM.query(self.propulsion.RUM, combination[1])   
        self.__processQueryResult__(gearboxQuery)
        self.__processQueryResult__(propulsionQuery)
        desiredThrottle = combination[2]
        if self.propulsion.getThrottle()<desiredThrottle:
            mod = desiredThrottle - self.propulsion.getThrottle()
            self.propulsion.incThrottle(mod)
        elif self.propulsion.getThrottle() > desiredThrottle:
            mod = self.propulsion.getThrottle() - desiredThrottle
            self.propulsion.decThrottle(mod)
        
    '''CC: 2'''        
    def __processQueryResult__(self, queryResult):
        queryResult = self.__getShortestResult__(queryResult)
        for q in queryResult:
            self.__visitAbstractQueryResult__(q)  
                  
    '''CC: 5'''        
    def __getShortestResult__(self, queryResult):
        if isinstance(queryResult, list) and len(queryResult) > 0 and isinstance(queryResult[0], list):
            return self.__getShortestListInListResult(queryResult)        
        else:
            return queryResult

    '''CC: 5'''     
    def __getShortestListInListResult(self, queryResult):
        shortest = -1
        for query in queryResult:        
            if isinstance(query, list):
                length = len(query)
            else:
                length = 1                
            if length < shortest or shortest == -1:
                shortest = length
                result = query
        return result

    '''CC: 4'''
    def __visitAbstractQueryResult__(self, queryResult):
        if isinstance(queryResult, AndQueryResult):
            self.__visitAndQueryResult__(queryResult)
        elif isinstance(queryResult, OrQueryResult):
            self.__visitOrQueryResult__(queryResult)
        elif isinstance(queryResult, InvokeServiceQueryResult):
            self.__visitInvokeServiceQueryResult__(queryResult)
        else:
            self.__VisitQueryResult__(queryResult)

    '''CC: 5'''
    def __ExecutePropulsionAction__(self, action, step, field):
        if action == 'inc' and field[1]:
            self.propulsion.incThrottle(step)
        elif action == 'dec':
            self.propulsion.decThrottle(step)
        elif action == 'set':
            current = self.propulsion.getThrottle()
            step -= current
            if step > 0:
                self.propulsion.incThrottle(step)
            else:
                self.propulsion.decThrottle(step)

    '''CC: 3'''
    def __VisitQueryResult__(self, queryResult):
        result = queryResult.getQueryResults()
        action = result[0]
        step = result[1]
        field = result[2]
        if field[0] == self.gearbox:
            self.__ExecuteGearboxAction__(action)
        elif field[0] == self.propulsion:
            self.__ExecutePropulsionAction__(action, step, field)
 
    '''CC: 3'''    
    def __ExecuteGearboxAction__(self, action):
        if action == 'inc':
            self.gearbox.incGear()
        elif action == 'dec':
            self.gearbox.decGear()

    '''CC: 2'''                        
    def __visitAndQueryResult__(self, queryResult):
        queries = queryResult.getQueryResults()
        for q in queries:
            self.__visitAbstractQueryResult__(q)
 
    '''CC: 2'''           
    def __visitOrQueryResult__(self, queryResult):
        queries = queryResult.getQueryResults()
        if len(queries) >0:
            self.__visitAbstractQueryResult__(queries[0])
 
    '''CC: 1'''            
    def __visitInvokeServiceQueryResult__(self, queryResult):
        queryResult.getQueryResults()()        
   
    @abc.abstractmethod 
    def __determinePossibleCombinations__(self, desiredSpeed):
        return
    
    @abc.abstractmethod    
    def __determineOptimalCombination__(self, combinations):
        return
    