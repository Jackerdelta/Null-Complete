'''
Created on Oct 2, 2014

@author: jack
'''
from main import Game
from main.Handler.UpgradeHandler import UpgradeHandler
from main.Upgrades.PointMachine import PointMachine
from main.Upgrades.PointFactory import PointFactory
from main.Upgrades.PointEmpire import PointEmpire
from main.Upgrades.Person import Worker, Engineer
from main.Handler.UserHandler import UserHandler

global UpgradeDict
UpgradeDict={}

global LvlDict
LvlDict = {}

class shop_main():
    UpgradeDict = {}
    def __init__(self,user,score,UpgradeDict):
        self.user=user
        self.score=score
    
        self.MachineLVL=0
        self.FactoryLVL=0
        self.EmpireLVL=0
    
    def storeFront(self):    
        
        
        print "You have:",self.score,"points."
        shop_upgrades=raw_input("Welcome to the store, type 'help' for help:").split()
        
        args=[x for x in shop_upgrades]
        
        if args[0] == 'return' or args[0] == 'r' :
            Game.Game.main(self.user,self.score).returnFromShopEvent(UpgradeDict,self.score)
        if args[0] == 'h' or args[0] == 'help' or args[0] == '?' or args[0] == 'Help':
            print("Upgrade List:")
            print("--Point Machine")
            print("--Point Factory")
            print("--Point Empire")
        
            print("-" * 30)
        
            print("'help <upgrade>' for a description of each upgrade. e.g 'help --Point Machine'")
            print("'get <upgrade>' for a description of each upgrade. e.g 'get --Point Machine")
            print("'upgrade <upgrade>' to upgrade the skill of your choice. e.g 'upgrade --Point Machine ")
            
            print("-" * 30)
            
            print('EXTRA INFO:')
            print("WARNING: Upgrades are case sensitive. INVALID: 'help Point Machine'")
            print("DON'T DO THAT.")
            Game.Game.shop_main(self.user,self.score,UpgradeDict)
        
                    
        #COMMANDS#
        
        
        if args[0] == 'modules':
            print "(1.) Apple Machine - Pump out those points faster than a chinese toy factory!"
            print "(2.) Apple Factory - Its like 10 Point Machines in one!"
            print "(3.) Apple Empire - A series of factories working in perfect harmony!"
            Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
            
        if args[0] == 'stats':
            Game.Game.shop_main(self.user,self.score,UpgradeDict).userStats()       
        if args[0] == 'upgrades':
            print "(1.) Apple Machine - Hire more workers to pump out more apples! "
            print "(2.) Apple Factory - Get better equipment to increase production 10x fold!"
            print "(3.) Apple Empire - Hire more factories to work for you!"
            print "--------------------------------------------------------------------------"
            print "(4.) Worker Population - Hire more workers to work in your Apple Orcherds!"
            print "(5.) Engineer Population - Hire more engineers to ensure for better machinery and longer seasons!"
            print "--------------------------------------------------------------------------"
            Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
             
        else:
            Game.Game.shop_main(self.user,self.score,UpgradeDict).storeFront()
    
    def moduleOptions(self):
        User = UpgradeHandler(UpgradeDict, LvlDict)
            
        module_input = raw_input(">>>")
        args_m = [x for x in module_input]
            
        #Point Machine
        if args_m[0]=='1':
            if self.score>=500 and User.hasUpgrade('Machine') is False:
                self.score-=500
                UpgradeDict['Machine']=True
                
                #Check if point machine was actually purchased.
                if User.hasUpgrade('Machine'):
                    print "You have now unlocked the 'Apple Machine' Module for 500 Apples!"
                    print "You now have ", self.score, " Apples!"
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
            
            elif self.score < 500:
                print "You don't have enough points to buy this!"
                Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
                
            else:
                print "Oh no! It appears there was an error purchasing this item!"
                Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
        
            #Point Factory
        if args_m[0]=='2':
            if self.score > 1500 and User.hasUpgrade('Factory') is False:
                self.score -= 1500
                UpgradeDict['Factory']=True
                
                #Check if Factory was actually purchased.
                if User.hasUpgrade('Factory'):
                    print "You have now unlocked the 'Apple Factory' Module for 1500 Apples!"
                    print "You now have ", self.score, " Apples!"
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
            
            elif self.score < 1500:
                print "You don't have enough points to buy this!"
                Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
            
            else:
                print "Oh no! It appears there was an error purchasing this item!"
                Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
        
        #Point Empire
        if args_m[0]=='3':
            if self.score>3000 and User.hasUpgrade('Empire') is False:
                self.score-=3000
                UpgradeDict['Empire']=True
                    
                #Check if Point Empire was actually purchased.
                if User.hasUpgrade('Empire'):
                    print "You have now unlocked the 'Apple Empire' Module for 3000 Apples!"
                    print "You now have ", self.score, " Apples!"
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
                
            elif self.score<3000:
                print "You don't have enough points to buy this!"
                Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
                
            else:
                print "Oh no! It appears there was an error purchasing this item!"
                Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
        if args_m[0] == 'r':
            Game.Game.shop_main(self.user,self.score,UpgradeDict).storeFront()
        else:
            print "Invalid Command!"
            Game.Game.shop_main(self.user,self.score,UpgradeDict).moduleOptions()
            

    def upgradeOptions(self):
        User = UpgradeHandler(UpgradeDict, LvlDict)
        
        print "You currently have %s Apples to spend." % (self.score)
        upgrades_input = raw_input(">>>").split()
        args_u = [x for x in upgrades_input]
                
        if args_u[0]=='1':
            if len(args_u) >= 2 and self.score >= int(PointMachine().getLevel() * 2000): 
                if User.hasUpgrade('Machine') and args_u[1]=='x':
                    times_1 = int(args_u[2])
                    for i in range(times_1):
                        if self.score <= 0 or times_1 <= 0 or self.score <= int(PointFactory().getLevel() * 2000):
                            print "You had enough points to upgrade your 'Apply Machine' to level %s!" % (PointMachine().getLevel())
                            Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                            break
                        else:   
                            self.score-=int(PointMachine().getLevel() * 2000)
                            LvlDict['Machine'] = PointMachine().upgradeLevel(1)
                            times_1 -= 1
                    print "You have successfully upgraded your 'Apple Machine' to level %s." % (PointMachine().getLevel())
                    print "You now have, %s Apples!" % (self.score)
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                    
                else:
                    print "You haven't purchased the 'Apple Machine' upgrade yet!"
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
            else:
                print "You don't have enough points for this!"
                Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()             
                    
        if args_u[0]=='2':
            if len(args_u) >= 2 and self.score >= int(PointFactory().getLevel() * 5000):
                if User.hasUpgrade('Factory') and args_u[1]== 'x':
                    times_2 = int(args_u[2])
                    for i in range(times_2):
                        if self.score <= 0 or times_2 <= 0 or self.score <= int(PointFactory().getLevel() * 5000):
                            print "You only had enough points to upgrade your 'Apple Factory' to level %s!" % (PointFactory().getLevel())
                            Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                            break
                        else:
                             
                            self.score -=int(PointFactory().getLevel() * 5000)
                            LvlDict['Factory'] = PointFactory().upgradeLevel(1)
                            times_2 -= 1
                    print "You have successfully upgraded your 'Apple Factory' to Level" , PointFactory().getLevel(), " for a total of, ", int((PointFactory().getLevel() * 5000) - 5000), " Apples!"
                    print "You now have, ", self.score, " Apples!"
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions() 
                else:
                    print "You haven't purchased the 'Apple Factory' upgrade yet!"
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions() 
            else:
                print "You need another %s points to upgrade this module to the next level." % (int(PointFactory().getLevel() * 5000))
                Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
        
        if args_u[0]=='3':
            if len(args_u) >= 2 and self.score >= int(PointEmpire(self.user, self.score).getLevel() * 26000):
                if User.hasUpgrade('Empire') and args_u[1]== 'x':
                    times_3 = int(args_u[2])
                    for i in range(times_3):
                        if self.score <= 0 or times_3 <= 0 or self.score <= int(PointEmpire(self.user, self.score).getLevel() * 26000):
                            print "You only had enough points to upgrade your 'Apple Empire' to level %s" % (PointEmpire(self.user,self.score).getLevel()) 
                            Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                            break
                        else:
                            self.score -=int(PointEmpire(self.user, self.score).getLevel() * 26000)
                            LvlDict['Empire'] = PointEmpire(self.user, self.score).upgradeLevel(1)
                            times_3 -= 1 
                    
                    print "You have successfully upgraded your 'Apple Empire' to Level" , PointEmpire(self.user, self.score).getLevel(), " for a total of, ", int((PointEmpire(self.user, self.score).getLevel() * 26000) - 26000), " Apples!"
                    print "You now have, ", self.score, " Apples!" 
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                else:
                    print "You haven't purchased the 'Apple Empire' upgrade yet! Be sure to use 'x'!"
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()  
        if args_u[0]=='4':
            if len(args_u) >= 2 and self.score >= int(Worker().getLevel() * 100):
                if args_u[1] == 'x':
                    times_4 = int(args_u[2])
                    for i in range(times_4):
                        if self.score <= 0 or times_4 <= 0 or self.score <= int(Worker().getLevel() * 100):
                            print "You only had enough points to upgrade your work force to %s Workers!" % (Worker().getLevel())
                            Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                            break
                        else:
                            self.score -= int(Worker().getLevel() * 100)
                            LvlDict['Worker'] = Worker().upgradeLevel(1)
                            times_4 -= 1
                        
                    print "You have successfully upgraded your work force to", Worker().getLevel(), "Workers!"
                    print "You now have %s Apples!" % (self.score)
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                else:
                    print "Be sure to use 'x'!"
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
            else:
                print "You don't have enough money for that! It will cost %s to upgrade your work force to the next level!" % (Worker().getLevel() * 100)
            if self.score >= int(Worker().getLevel() * 100) and len(args_u) <= 0:
                self.score -= int(Worker().getLevel() * 100)
                
                LvlDict['Worker'] = Worker().upgradeLevel(1)
                print "You have successfully upgraded your work force to", Worker().getLevel(), "Workers!"
                print "You now have, ", self.score, " Apples!"
                Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
        
        if args_u[0]=='5':
            if len(args_u) >= 2 and self.score >= int(Engineer().getLevel() * 175):
                if args_u[1] == 'x':
                    times_5 = int(args_u[2])
                    for i in range(int(args_u[2])):
                        if self.score <= 0 or times_5 <= 0 or self.score <= int(Engineer().getLevel() * 175):
                            print "You only had enough points to upgrade your Engineer work force to %s Engineers!" % (Engineer().getLevel())
                            Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                            break
                        else:
                            self.score -= int(Engineer().getLevel() * 175)
                            LvlDict['Engineer'] = Engineer().upgradeLevel(1)
                            times_5-=1
                    
                    print "You have successfully upgraded your Engineer work force to,", Engineer().getLevel(), "Engineers!"
                    print "You now have %s Apples!" % (self.score)
                    Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
                else:
                    print "Remember to use 'x'"
            else:
                print "You need another %s Apples to upgrade your Engineer work force to the next level!" % (Engineer().getLevel() * 175)    
                    
            if self.score >= int(Engineer().getLevel() * 175) and len(args_u) <= 1:
                self.score -= int(Engineer().getLevel() * 175)
                
                LvlDict['Engineer'] = Engineer().upgradeLevel(1)
                print "You have succesfully upgraded your Engineer work force to, %s Engineers!" % (Engineer().getLevel())
                Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()
            else:
                print "You don't have enough points for this!"
        elif args_u[0]=='r':
            Game.Game.shop_main(self.user,self.score,UpgradeDict).storeFront()
        else:
            Game.Game.shop_main(self.user,self.score,UpgradeDict).upgradeOptions()

    def userStats(self):
        User = UpgradeHandler(UpgradeDict,LvlDict)
        
        if User.hasUpgrade('Machine'):
            print "(STATS) Apple Machine --- Level(%s)" % (PointMachine().getLevel())
        if User.hasUpgrade('Factory'):
            print "(STATS) Apple Factory --- Level(%s)" % (PointFactory().getLevel())
        if User.hasUpgrade('Empire'):
            print "(STATS) Apple Empire --- Level(%s)" % (PointEmpire(self.user,self.score).getLevel())
        
        print "(STATS) %s currently has %s Workers." % (UserHandler().getNick(self.user, False),Worker().getLevel())
        print "(STATS) %s currently has %s Engineers." % (UserHandler().getNick(self.user, False), Engineer().getLevel())
        
            
                    
        