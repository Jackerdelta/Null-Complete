from main.Handler.PointHandler import *
from main.Handler.UserHandler import *
import sys,random



class main():

    
    
    def __init__(self,user):
        self.points=PointHandler(user,0)
        self.user=user
        this=main
        
        self.scoreLVL1=random.randint(1,5)
        self.scoreLVL2=random.randint(1,10)
        self.scoreLVL3=random.randint(1,20)
    
        self.print_score=0
        
        self.classInstance=shop(self.user,self.points.getPoints(self.user,False)
        
        st_=raw_input("Start? Y/N:")
        if st_.lower()=="yes" or "y":
            print("Wait there a second!, we to configure some stuff first.")
            time_to_show_score=raw_input("# of turns before score is shown: ")
            this.main_loop(self)
        else:
            print("Well thanks for coming along for the party!")
            sys.exit("Bye bye!")
            
            
            
    def main_loop(self):
        active_state=True
        while active_state==True:
            #Start loop
            
            prim=raw_input("Pick Apple? Y/N: ")
            
            if prim.lower()=="yes" or "y" or "Y":
                self.points.addPoint(self.scoreLVL1, False)
                self.print_score+=1
                
                if self.print_score==time_to_show_score:
                    self.points.getPoints(self.user, True)
                    time_to_show_score=0
                active_state=True
                
            if prim.lower()=="no" or "n" or "N":
                print("Thanks for playing.")
                sys.exit("Really, thanks!")
            if prim.lower()=="shop" or "s" or "S":
                
            else:
                print("Invalid Command.")
                
        self.points.addPoint(10, True)
        #Debugging Thing: points.getPoints(user,True)
        
        
    
