'''
Created on Aug 9, 2015

@author: jack
'''

import random,math
Level = 0

class PointMachine:
    def __init__(self):
        self.Level = Level
    def calculatePoints(self):
        
        final_points = (Level + 1) * ((Level ** 2) + 45) * 4
        
        return final_points 
      
    def setLevel(self, Lvl):
        global Level
        Level = int(Lvl)
    
    def getLevel(self):
        return Level
   
    def upgradeLevel(self,amount):
        global Level
        Level = Level + amount
    