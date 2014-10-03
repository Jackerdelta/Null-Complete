'''
Created on Oct 2, 2014

@author: jack
'''
from main import Game

global pointsDict
pointsDict={}

class shop_main():
    pointsDict={}
    def __init__(self,user,score,pointsDict):
        self.user=user
        self.score=score
        this=shop_main
        this.upgradeOptions(self)
    def upgradeOptions(self):
        print "TEST"
        
        
        this=shop_main
        
        shop_upgrades=raw_input("Upgrade Module 'type 'help' for help':").split()
        
        
        args=[x for x in shop_upgrades]
        
        
        if shop_upgrades=='help' or shop_upgrades=='?' or shop_upgrades=='Help' or shop_upgrades=='h':
            
            this.upgradeOptions(self)
        if args[0] == 'return' or args[0] == 'r' :
            me=Game.Game
            i1=me.main(self.user,self.score).returnFromShopEvent(pointsDict)
        
        
        
        print "DEBUG:",args
        
        
        if args[0]=='help' and args[1]=='--Point' and args[2]=='Machine':
            pointsDict['Machine']=True
            for i in range(100):
                    key='Machine'
                    if key in pointsDict:
                        print "You have now unlocked the Point Machine Module!"
                        
                        print pointsDict
                        
                        me=Game.Game
                        me.shop_main(self.user,self.score,pointsDict)
                        break;
                    else:
                        print "Oh no! It appears there was an error purchasing this item!"
        else:
            print("Invalid Command.")
            me=Game.Game
            me.shop_main(self.user,self.score,pointsDict)
    def helpMenu(self):
        print("Upgrade List:")
        print("--Point Machine")
        print("--Point Factory")
        print("--Point Empire")
        print("'help <upgrade>' for a description of each upgrade. e.g 'help --Point Machine'")
        print("WARNING: Upgrades are case sensitive. INVALID: 'help Point Machine'")
        print("DON'T DO THAT.")
    def PointMenu(self):
        print("Point Menu")
        print("--Point Machine")
        print("--Point Factory")
        print("--Point Empire")
        