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
    
        self.MachineLVL=0
        self.FactoryLVL=0
        self.EmpireLVL=0
        
        
        this=shop_main
        this.upgradeOptions(self)
    def upgradeOptions(self):
        
        
        this=shop_main
        print "You have:",self.score,"points."
        shop_upgrades=raw_input("Upgrade Module 'type 'help' for help':").split()
        
        
        args=[x for x in shop_upgrades]
        
        
        if shop_upgrades=='help' or shop_upgrades=='?' or shop_upgrades=='Help' or shop_upgrades=='h':
            this.upgradeOptions(self)
        if args[0] == 'return' or args[0] == 'r' :
            me=Game.Game
            i1=me.main(self.user,self.score).returnFromShopEvent(pointsDict,self.score)
        
        
        
        print "DEBUG:",args
        
        o=self.score
        y=self.MachineLVL
                    
        
        #COMMANDS#
        me=Game.Game
        if args[0]=='get' and args[1]=='--Point' and args[2]=='Machine':
            if self.score>=500:
                self.score=self.score-500
                pointsDict['Machine']=True
                for i in range(100):
                    key='Machine'
                    if key in pointsDict:
                        print "You have now unlocked the Point Machine Module!"
                        me.shop_main(self.user,self.score,pointsDict)
                        break;
            elif self.score < 500:
                print "You don't have enough points to buy this!"
                me.shop_main(self.user,self.score,pointsDict)
            else:
                    print "Oh no! It appears there was an error purchasing this item!"
                    me.shop_main(self.user,self.score,pointsDict)
        if args[0]=='get' and args[1]=='--Point' and args[2]=='Factory':
            if self.score>1500:
                self.score-=1500
                pointsDict['Factory']=True
                for i in range(100):
                    key1='Factory'
                    if key1 in pointsDict:
                        print "You have now unlocked the Point Factory Module!"
                        me.shop_main(self.user,self.score,pointsDict)
                        break;
            elif self.score < 1500:
                print "You don't have enough points to buy this!"
                me.shop_main(self.user,self.score,pointsDict)
            else:
                
                print "Oh no! It appears there was an error purchasing this item!"
                me.shop_main(self.user,self.score,pointsDict)
        if args[0]=='get' and args[1]=='--Point' and args[2]=='Empire':
                if self.score>3000:
                    self.score-=3000
                    pointsDict['Empire']=True
                    for i in range(100):
                        key2='Factory'
                        if key2 in pointsDict:
                            print "You have now unlocked the Point Empire Module!"
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                elif self.score<3000:
                    print "You don't have enough points to buy this!"
                    me.shop_main(self.user,self.score,pointsDict)
                else:
                
                    print "Oh no! It appears there was an error purchasing this item!"
                    me.shop_main(self.user,self.score,pointsDict)
        #END OF COMMANDS
        ###############
        #START OF UPGRADES
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Machine':
            print "hello"
            for i in range(100):
                key3='Machine'
                if key3 in pointsDict:
                    userHasPointMachine=True
                    break;
                else:
                    print("You haven't purchased the Machine Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointMachine==True:
                if self.MachineLVL==0:
                    print "hello 0"
                    if self.score >= 2000:
                        self.score=self.score-2000
                        pointsDict['MachineLVL']=1
                        key4='MachineLVL'
                        if key4 in pointsDict:
                            print "You have now upgraded your Point Machine to Level 1!"
                            self.MachineLVL=+1
                            print self.MachineLVL
                            me.shop_main(self.user,self.score,pointsDict)
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 2000:
                    print "You don't have enough points for this upgrade!"
                if y==1:
                    print "hi"
                    if o > 6000:
                        o=o-6000
                        pointsDict['MachineLVL']=2
                        self.MachineLVL=2
                        
                        key5='MachineLVL'
                            
                        if key5 in pointsDict:
                            print "You have now upgraded your Point Machine to Level 2!"
                            self.MachineLVL=+1
                            print self.MachineLVL
                            me.shop_main(self.user,o,pointsDict)
                            
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 6000:
                    print "You don't have enough points for this upgrade!"
                if self.MachineLVL==2:
                    if self.score > 12000:
                        self.score=self.score-12000
                        pointsDict['MachineLVL']=True
                        self.MachineLVL=3
                        for i in range(100):
                            key6='MachineLVL'
                            if key6 in pointsDict:
                                print "You have now upgraded your Point Machine to Level 3!"
                                print "This is the maximum level for this skill! For now."
                                me.shop_main(self.user,self.score,pointsDict)
                                break;
                            else:
                                print "There was an error purchasing this upgrade!"
                                me.shop_main(self.user,self.score,pointsDict)
                    elif self.score < 12000:
                        print "You don't have enough points for this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)
                elif self.MachineLVL >=3:
                    print "Woah there. It seems you've already eached the max level for this skill!"
#################### END OF UPGRADE FOR 'POINT MACHINE'
#################### END OF UPGRADE FOR 'POINT MACHINE'                
        else:
            print("Invalid Command.")
            me=Game.Game
            me.shop_main(self.user,self.score,pointsDict)
        
    def helpMenu(self):
        me=Game.Game
        print("Upgrade List:")
        print("--Point Machine")
        print("--Point Factory")
        print("--Point Empire")
        x=raw_input("<press any key to show more> else type 'exit'")
        if x=='exit':
            me.shop_main(self.user,self.score,pointsDict)
        
        print("'help <upgrade>' for a description of each upgrade. e.g 'help --Point Machine'")
        print("'get <upgrade>' for a description of each upgrade. e.g 'get --Point Machine")
        print("'upgrade <upgrade>' to upgrade the skill of your choice. e.g 'upgrade --Point Machine ")
        x1=raw_input("<press any key to show more> else type 'exit'")
        if x1=='exit':
            me.shop_main(self.user,self.score,pointsDict)
        print('EXTRA INFO:')
        print("WARNING: Upgrades are case sensitive. INVALID: 'help Point Machine'")
        print("DON'T DO THAT.")
        raw_input("<press any key to continue>")
        me.shop_main(self.user,self.score,pointsDict)
    def PointMenu(self):
        print("Point Menu")
        print("--Point Machine")
        print("--Point Factory")
        print("--Point Empire")
        