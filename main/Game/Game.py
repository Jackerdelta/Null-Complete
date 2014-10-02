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
            print(prim)
            if prim.lower()=="yes" or "y" or "Y":
                self.points.addPoint(self.scoreLVL1, False)
                self.print_score+=1
                print("hi")
                
                if self.print_score==10:
                    self.points.getPoints(self.user, True)
                active_state=True
                
                
        self.points.addPoint(10, True)
        #Debugging Thing: points.getPoints(user,True)
        
        
    