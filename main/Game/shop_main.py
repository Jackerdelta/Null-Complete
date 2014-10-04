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
        
        
        this=shop_main
        print "You have:"+self.score+"points."
        shop_upgrades=raw_input("Upgrade Module 'type 'help' for help':").split()
        
        
        args=[x for x in shop_upgrades]
        
        
        if shop_upgrades=='help' or shop_upgrades=='?' or shop_upgrades=='Help' or shop_upgrades=='h':
            
            this.upgradeOptions(self)
        if args[0] == 'return' or args[0] == 'r' :
            me=Game.Game
            i1=me.main(self.user,self.score).returnFromShopEvent(pointsDict)
        
        
        
        print "DEBUG:",args
        
        #COMMANDS#
        me=Game.Game
        if args[0]=='get' and args[1]=='--Point' and args[2]=='Machine':
            if self.score>500:
                self.score-=500
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
                if self.score>2000:
                    self.score-=2000
                    pointsDict['MachineLVL']=1
                    for i in range(100):
                        key4='MachineLVL1'
                        if key4 in pointsDict:
                            print "You have now upgraded your Point Machine to Level 1!"
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 2000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)
        
        #LEVEL 2 MACHINE
        
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Machine':
            for i in range(100):
                key5='Machine'
                if key5 in pointsDict:
                    userHasPointMachine1=True
                    break;
                else:
                    print("You haven't purchased the Machine Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointMachine1==True:
                if self.score>6000:
                    self.score-=6000
                    pointsDict['MachineLVL']=2
                    for i in range(100):
                        key6='MachineLVL'
                        if key6 in pointsDict:
                            print "You have now upgraded your Point Machine to Level 2!"
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 6000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)     
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Machine':
            for i in range(100):
                key7='Machine'
                if key7 in pointsDict:
                    userHasPointMachine2=True
                    break;
                else:
                    print("You haven't purchased the Machine Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointMachine2==True:
                if self.score>12000:
                    self.score-=12000
                    pointsDict['MachineLVL']=3
                    for i in range(100):
                        key8='MachineLVL'
                        if key8 in pointsDict:
                            print "You have now upgraded your Point Machine to Level 3!"
                            print "This is the maximum level for this skill."
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 12000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)
#################### END OF UPGRADE FOR 'POINT MACHINE'

        #START OF FACTORY UPGRADE
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Factory':
            for i in range(100):
                f1='Factory'
                if f1 in pointsDict:
                    userHasPointFactory=True
                    break;
                else:
                    print("You haven't purchased the Machine Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointFactory==True:
                if self.score>3000:
                    self.score-=3000
                    pointsDict['FactoryLVL']=1
                    for i in range(100):
                        m2='FactoryLVL'
                        if m2 in pointsDict:
                            print "You have now upgraded your Point Factory to Level 1!"
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 3000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)
        
        #LEVEL 2 FACTORY
        
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Factory':
            for i in range(100):
                m3='Factory'
                if m3 in pointsDict:
                    userHasPointFactory1=True
                    break;
                else:
                    print("You haven't purchased the Machine Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointFactory1==True:
                if self.score>8000:
                    self.score-=8000
                    pointsDict['FactoryLVL']=2
                    for i in range(100):
                        m4='MachineLVL'
                        if m4 in pointsDict:
                            print "You have now upgraded your Point Factory to Level 2!"
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 8000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)     
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Factory':
            for i in range(100):
                m5='Factory'
                if m5 in pointsDict:
                    userHasPointFactory2=True
                    break;
                else:
                    print("You haven't purchased the Machine Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointFactory2==True:
                if self.score>16000:
                    self.score-=16000
                    pointsDict['FactoryLVL']=3
                    for i in range(100):
                        m6='MachineLVL'
                        if m6 in pointsDict:
                            print "You have now upgraded your Point Factory to Level 3!"
                            print "This is the maximum level for this skill."
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 16000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)
#################### END OF UPGRADE FOR 'POINT MACHINE' 
        
        #START OF EMPIRE UPGRADE
        
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Empire':
            for i in range(100):
                e1='Empire'
                if e1 in pointsDict:
                    userHasPointEmpire=True
                    break;
                else:
                    print("You haven't purchased the Empire Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointEmpire==True:
                if self.score>5000:
                    self.score-=5000
                    pointsDict['EmpireLVL']=1
                    for i in range(100):
                        e2='MachineLVL1'
                        if e2 in pointsDict:
                            print "You have now upgraded your Point Empire to Level 1!"
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 5000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)
        
        #LEVEL 2 EMPIRE
        
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Empire':
            for i in range(100):
                e3='Empire'
                if e3 in pointsDict:
                    userHasPointEmpire1=True
                    break;
                else:
                    print("You haven't purchased the Empire Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointEmpire1==True:
                if self.score>10000:
                    self.score-=10000
                    pointsDict['EmpireLVL']=2
                    for i in range(100):
                        e4='MachineLVL'
                        if e4 in pointsDict:
                            print "You have now upgraded your Point Empire to Level 2!"
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 10000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)     
        if args[0]=='upgrade' and args[1]=='--Point' and args[2]=='Empire':
            for i in range(100):
                e5='Machine'
                if e5 in pointsDict:
                    userHasPointEmpire2=True
                    break;
                else:
                    print("You haven't purchased the Empire Module upgrade yet!")
                    me.shop_main(self.user,self.score,pointsDict)
                    break;
            if userHasPointEmpire2==True:
                if self.score>20000:
                    self.score-=20000
                    pointsDict['EmpireLVL']=3
                    for i in range(100):
                        e6='MachineLVL'
                        if e6 in pointsDict:
                            print "You have now upgraded your Point Empire to Level 3!"
                            print "This is the maximum level for this skill."
                            me.shop_main(self.user,self.score,pointsDict)
                            break;
                        else:
                            print "There was an error purchasing this upgrade!"
                            me.shop_main(self.user,self.score,pointsDict)
                elif self.score < 20000:
                    print "You don't have enough points to purchase this upgrade!"
                    me.shop_main(self.user,self.score,pointsDict)
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
        