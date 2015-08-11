from main.Handler.PointHandler import *
from main.Handler.UserHandler import *
from main.Handler.UpgradeHandler import *

from main.Upgrades.PointEmpire import *
from main.Upgrades.PointFactory import *
from main.Upgrades.PointMachine import *
from main.Upgrades.Person import *

from main.Game.shop_main import shop_main, UpgradeDict, LvlDict
import sys,random
from main import Game



class main():

    
    
    def __init__(self,user,score):
        self.points=PointHandler(user,score)
        self.user=user
        
        self.points.addPoint(100000000, False)
        
        self.score=score
        
        self.scoreLVL1=random.randint(1,5)
        self.scoreLVL2=random.randint(1,10)
        self.scoreLVL3=random.randint(1,20)
        
        self.turns=Engineer().calculateSeasonLength()
        
        self.print_score=0
        
        self.UpgradeDict={}
        
        
        self.MachinePoints=0
        self.FactoryPoints=0
        self.EmpirePoints=0
    
    def getPoints(self):
        return self.points.getPoints(self.user)
    def fromStartEvent(self):
        this=main
        st_=raw_input("Start? Y/N:")
        if st_.lower()=="yes" or "y":
            this.main_loop(self,shop_main.UpgradeDict)
            PointMachine().setLevel(1)
            PointFactory().setLevel(1)
            PointEmpire(self.user, self.points.getPoints(self.user, False)).setLevel(1)
        else:
            print("Well thanks for coming along for the party!")
            sys.exit("Bye bye!")
            
    def returnFromShopEvent(self,UpgradeDict,score):
        self.points.setPoints(score, False)
        self.UpgradeDict.clear()
        self.UpgradeDict=UpgradeDict
        
        print self.UpgradeDict
        
        start_again=raw_input("Start Game? Y/N: ")
        if start_again.lower()=="y" or start_again.lower()=="yes":
            this=Game.Game
            this.main.main_loop(self, UpgradeDict)
            
    def main_loop(self,UpgradeDictt):
        User = UpgradeHandler(UpgradeDict, LvlDict)
        
        if User.hasUpgrade('Machine'):
            self.hasPointMachine=True
            print "Point Machine Module Enabled."
            
        if User.hasUpgrade('Factory'):
            print "Point Factory Module Enabled."
    
        if User.hasUpgrade('Empire'):
            print "Point Empire Module Enabled."    
        
        
        active_state=True
        while active_state==True:
            #Start loop

            prim=raw_input("Pick Apple? Y/N: ")
            print("Turns Remaining,", self.turns)
            
            #Yes
            if prim.strip()=='y' or prim.strip()=="Y" or prim.strip()=="yes" or prim.strip()=="YES" or prim.strip() == "yy".lower():
                for i in range(self.turns):
                    self.points.addPoint(Worker().calculatePoints(), True)
                    self.print_score+=1
                    self.turns-=1
                    
                    #Code for adding in bonus points based on what upgrades are owned.
                    
                    if User.hasUpgrade('Machine'):
                        self.MachinePoints = PointMachine().calculatePoints()
                        self.points.addPoint(self.MachinePoints, False)
                    
                    if User.hasUpgrade('Factory'):
                        self.FactoryPoints = PointFactory().calculatePoints()
                        self.points.addPoint(self.FactoryPoints, False)
                        
                    if User.hasUpgrade('Empire'):
                        self.EmpirePoints = PointEmpire(self.user, self.points.getPoints(self.user, False)).calculatePoints()
                        self.points.addPoint(self.EmpirePoints, False)
                    ########
                    
                    if self.turns == 0 or self.turns < 0:
                        self.turns += Engineer().calculateSeasonLength()
                        print "Your final score is:",self.points.getPoints(self.user, False)
                        
                        if User.hasUpgrade('Machine'):
                            print "You earned a bonus of",self.MachinePoints,"from your 'Points Machine' upgrade! Level(",PointMachine().getLevel(),")"
                            
                        if User.hasUpgrade('Factory'):
                            print "You earned a bonus of",self.FactoryPoints,"from your 'Points Factory' upgrade! Level(",PointFactory().getLevel(),")"
                                    
                        if User.hasUpgrade('Empire'):
                            print "You earned a bonus of",self.EmpirePoints,"from your 'Points Empire' upgrade! Level(",PointEmpire(self.user,self.score).getLevel(),")"
                        
                        shop_=raw_input("Go to shop? Y/N:")
                        if shop_.strip()=='y' or shop_.strip()=="Y" or shop_.strip()=="yes" or shop_.strip()=="YES":
                            
                            Game.Game.shop_main(self.user,self.points.getPoints(self.user, False),self.UpgradeDict).storeFront()
                            break;
            #No    
            elif prim.strip()=="n" or prim.strip()=="no" or prim.strip()=="N" or prim.strip()=="NO":
                break
                print("Thanks for playing!")
                sys.exit("Really, thanks!")
            
            else:
                break
                print("Invalid Command.")
        #Debugging Thing: points.getPoints(user,True)
        
        
    