'''
Created on Aug 9, 2015

@author: jack
'''

from main.Handler.PointHandler import *

Level = 0

class PointEmpire:
    def __init__(self,user,points):
        self.user = user
        self.points = points
        
        self.Level = Level
    def calculatePoints(self):
        user_points = PointHandler(self.user,self.points).getPoints(self.user, False)
                
        final_user_points = (user_points/1000) * (Level + 5) + 100
        return final_user_points
    
    def setLevel(self, Lvl):
        global Level
        Level = Lvl
    
    def getLevel(self):
        return Level
    
    def upgradeLevel(self,amount):
        global Level
        Level += amount