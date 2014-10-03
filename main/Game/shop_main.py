'''
Created on Oct 2, 2014

@author: jack
'''

class shop_main():
    def __init__(self,user,score,pointsDict):
        self.user=user
        self.score=score
        self.pointsDict=pointsDict
        this=shop_main
        this.upgradeOptions(self)
    def upgradeOptions(self):
        shop_upgrades=raw_input("Upgrade Module 'type 'help' for help':").split()
        if shop_upgrades=='help' or shop_upgrades=='?' or shop_upgrades=='Help' or shop_upgrades=='h':
            this=shop_main
            this.upgradeOptions(self)
        args=[x for x in shop_upgrades]
        print args
        if args[0]=='help':
            this.upgradeOptions()
            if args[1]=='--Point':
                if args[2]=='Machine':
                        self.pointsDict['Machine']=True
    def helpMenu(self):
        print("Upgrade List:")
        print("--Point Machine")
        print("--Point Factory")
        print("--Point Empire")
        print("'help <upgrade>' for a description of each upgrade. e.g 'help --Point Macine'")
        print("WARNING: Upgrades are case sensitive. INVALID: 'help Point Machine'")
        print("DON'T DO THAT.")
    def PointMenu(self):
        print("Point Menu")
        print("--Point Machine")
        print("--Point Factory")
        print("--Point Empire")
        