from World.Weather.AbstractWeather import AbstractWeather
import random

class Weather(AbstractWeather):
            
    def __init__(self):
        AbstractWeather.__init__(self)        
        
    def determineWeather(self):
        'determines the weather randomly.'
        '60% chance it has not changed in strength'
        '15% chance it has increased by one step, unless it is at the max strength, then it instead decreases in strength'
        '15% chance it has decreased by one step, unless it is at the minimum strength, then it instead increases in strength'
        '5% chance it has changed by 2 steps.'
        change = random.random()*100
        if ((change > 60) & (change <=75) & (self.strength<self.max_strength)) | ((change >75) & (change <=90) & (self.strength==0)):
            self.strength +=1
        elif ((change > 60) & (change <=75) & (self.strength==self.max_strength)) | ((change >75) & (change <=90) & (self.strength>0)):
            self.strength -=1
        elif ((change > 90) & (change <=95) & (self.strength<self.max_strength)) | ((change >95) & (change <=100) & (self.strength==0)):
            self.strength = min(self.strength+2, self.max_strength)
        elif change>90:
            self.strength = max(self.strength-2, 0)
            
        'direction is where the wind is coming from compared to the car, so front, back or side'
        '60% chance it does not change, 20% chance it changes to one of the other options'
        change = random.random()*100;
        if change>40:            
            self.direction = random.randrange(0,3, 1)  
    
    def getResistance(self):
        if self.getDirection() == self.direction_front:
            resistance = pow(self.strength,2)
        elif self.getDirection == self.direction_side:
            resistance = self.strength
        else:
            resistance = pow(self.strength, 1.5)*-1
        return resistance
        
        