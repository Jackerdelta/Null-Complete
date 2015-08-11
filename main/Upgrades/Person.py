'''
Created on Aug 10, 2015

@author: jack
'''
import random

Level_Worker = 0
Level_Engineer = 0
class Worker:
    def calculatePoints(self):
        Level = Worker().getLevel()
        
        final_points = (Level + random.randint(1,Level+3)) 
        return final_points
    
    def setLevel(self, Lvl):
        global Level_Worker
        Level_Worker = Lvl
    def getLevel(self):
        return Level_Worker
    def upgradeLevel(self,amount):
        global Level_Worker
        Level_Worker += amount

class Engineer:
    def calculateSeasonLength(self):
        Level = Engineer().getLevel()
        
        final_turns = (Level + random.randint(Level+1,Level+5))
        
        return final_turns
    
    def setLevel(self, Lvl):
        global Level_Engineer
        Level_Engineer = Lvl
    def getLevel(self):
        return Level_Engineer
    def upgradeLevel(self,amount):
        global Level_Engineer
        Level_Engineer += amount