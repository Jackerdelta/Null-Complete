'''
Created on Sep 27, 2014

@author: jack
'''

UserDict={}
global UserDict

NickDict={}
global NickDict

class UserHandler():
    def createUser(self,username,nickname):
        UserDict[username]=nickname
        NickDict[nickname]=username
    def getNick(self,username,output=False):
        if output==True:
            print(UserDict[username])
        else:
            return UserDict[username]
    def getUsername(self,nickname,output=False):
        if output==True:
            print(NickDict[nickname])
        else:
            return NickDict[nickname]
    def getAllUsers(self):
        for i in UserDict.items():
            print(i)