'''
Created on Sep 27, 2014

@author: jack
'''
class PointHandler:
    
    pointDict={}
    global pointDict
    
    def __init__(self,user,points=0):
        self.user=user
        self.points=points
        pointDict[user]=points
        
    def addPoint(self, pointsToAdd=0,output=False):
        try:
            int(pointsToAdd)
        except:
            print("Error: Expected int and got something else.")
        finally:
            self.points=self.points+int(pointsToAdd)
            pointDict[self.user]=self.points
            if output==True:
                print pointDict[self.user]
    def setPoints(self,value,output=False):
        try:
            int(value)
        except:
            print("Error: Expected int and got something else.")
        finally:
            self.points=value
            pointDict[self.user]=self.points
            if output==True:
                print pointDict[self.user]
    def subtractPoint(self,pointsToSub,output=False):
        try:
            int(pointsToSub)
        except:
            print("Error: Expected int and got something else.")
        finally:
            self.points-=pointsToSub
            pointDict[self.user]=self.points
            if output==True:
                print(self.points)
    def resetPoints(self,output=False):
        self.points=0
        pointDict[self.user]=self.points
        if output==True:
            print("Points now equals: "+self.points)
    def multPoints(self,multiplier,output=False):
        try:
            int(multiplier)
        except:
            print("Error: Expected int and got something else.")
        finally:
            self.points=self.points*multiplier
            pointDict[self.user]=self.points
            if output==True:
                print(self.points)
    def getPoints(self,user,output=False):
        if output==True:
            print(pointDict[user])
        else:
            return pointDict[user]
        
            
        