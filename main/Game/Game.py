from main.Handler.PointHandler import *
from main.Handler.UserHandler import *
from main.Game.shop_main import shop_main
import sys,random
from main import Game



class main():

    
    
    def __init__(self,user,score):
        self.points=PointHandler(user,score)
        self.user=user
        this=main
        
        self.score=score
        
        self.scoreLVL1=random.randint(1,5)
        self.scoreLVL2=random.randint(1,10)
        self.scoreLVL3=random.randint(1,20)
        
        self.turns=random.randint(1,3)
        
        self.print_score=0
        
        self.pointDict={}
        
        self.MachineLVL1=random.randint(1,3)
        self.MachineLVL2=random.randint(1,5)
        self.MachineLVL3=random.randint(1,8)
        
        self.MachinePoints=0
        
        self.hasPointMachine=False
        self.hasPointFactory=False
        self.hasPointEmpire=False
        '''
        st_=raw_input("Start? Y/N:")
        if st_.lower()=="yes" or "y":
            this.main_loop(self,shop_main.pointsDict)
        else:
            print("Well thanks for coming along for the party!")
            sys.exit("Bye bye!")
        '''
    
    
    def fromStartEvent(self):
        this=main
        st_=raw_input("Start? Y/N:")
        if st_.lower()=="yes" or "y":
            this.main_loop(self,shop_main.pointsDict)
        else:
            print("Well thanks for coming along for the party!")
            sys.exit("Bye bye!")
    def returnFromShopEvent(self,pointDict):
        self.pointDict.clear()
        self.pointDict=pointDict
        
        print self.pointDict
        
        start_again=raw_input("Start Game? Y/N: ")
        if start_again.lower()=="y" or start_again.lower()=="yes":
            this=Game.Game
            this.main.main_loop(self, pointDict)
    def main_loop(self,pointDictt):
        for i in range(100):
            key='Machine'
            key1='Factory'
            key2='Empire'
            if key in self.pointDict:
                self.hasPointMachine=True
                print "Point Machine Module Enabled."
                break;
            if key1 in self.pointDict:
                self.hasPointFactory=True
                print "Point Factory Module Enabled."
                break;
            if key2 in self.pointDict:
                self.hasPointEmpire=True
                print "Point Factory Module Enabled." 
                break;   
            else:
                print "User does not have Point Machine enabled."
                print self.pointDict
                break;
        
        active_state=True
        while active_state==True:
            #Start loop

            prim=raw_input("Pick Apple? Y/N: ")
            print(self.turns)
            if prim.strip()=='y' or prim.strip()=="Y" or prim.strip()=="yes" or prim.strip()=="YES":
                self.points.addPoint(self.scoreLVL1, False)
                self.print_score+=1
                self.turns-=1
                
                #######
                
                if self.hasPointMachine==True:
                    self.points.addPoint(self.MachineLVL1, False)
                    self.MachinePoints+=self.MachineLVL1
            
                
                ########
                
                if self.turns == 0 or self.turns < 0:
                    print "Your final score is:",self.points.getPoints(self.user, False)
                    if self.hasPointMachine==True:
                        print "HI"
                        print "You earned a bonus of",self.MachinePoints,"from your 'Points Machine' upgrade!"
                    else:
                        pass
                    shop_=raw_input("Go to shop? Y/N:")
                    if shop_.strip()=='y' or shop_.strip()=="Y" or shop_.strip()=="yes" or shop_.strip()=="YES":
                        me=Game.Game
                        me.shop_main(self.user,self.points.getPoints(self.user, False),self.pointDict)
                        break
                else:
                    pass
                
            elif prim.strip()=="n" or prim.strip()=="no" or prim.strip()=="N" or prim.strip()=="NO":
                break
                print("Thanks for playing!")
                sys.exit("Really, thanks!")
            else:
                break
                print("Invalid Command.")
        #Debugging Thing: points.getPoints(user,True)
        
        
    