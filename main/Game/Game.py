from main.Handler.PointHandler import *
from main.Handler.UserHandler import *
from main.Game.shop_main import shop_main
import sys,random
from main import Game



class main():

    
    
    def __init__(self,user):
        self.points=PointHandler(user,0)
        self.user=user
        this=main
        
        self.scoreLVL1=random.randint(1,5)
        self.scoreLVL2=random.randint(1,10)
        self.scoreLVL3=random.randint(1,20)
        
        self.turns=random.randint(8,20)
        
        self.print_score=0
        
        self.pointDict={}
        
        st_=raw_input("Start? Y/N:")
        if st_.lower()=="yes" or "y":
            this.main_loop(self)
        else:
            print("Well thanks for coming along for the party!")
            sys.exit("Bye bye!")
    def main_loop(self):
        active_state=True
        while active_state==True:
            #Start loop
            
            prim=raw_input("Pick Apple? Y/N: ")
            print(self.turns)
            if prim.strip()=='y' or prim.strip()=="Y" or prim.strip()=="yes" or prim.strip()=="YES":
                self.points.addPoint(self.scoreLVL1, False)
                self.print_score+=1
                self.turns-=1
                
                
                
                if self.turns== 0 or self.turns < 0:
                    print "Your final score is:",self.points.getPoints(self.user, False)
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
        
        
    