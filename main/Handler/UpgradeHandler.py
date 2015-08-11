'''
Created on Aug 9, 2015

@author: jack
'''


class UpgradeHandler():
    def __init__(self,UpgradeDict, LvlDict):
        self.UpgradeDict = UpgradeDict
        self.LvlDict = LvlDict
    def hasUpgrade(self,upgrade):
        try:
            if str(upgrade) in self.UpgradeDict:
                return True
            else:
                return False
        except Exception as e:
            return e;
    
    def getUpgradeLevel(self,upgrade):
        try:
            return self.UpgradeDict[upgrade]
        except Exception as e:
            return e;
        
        