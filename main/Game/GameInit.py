'''
Created on Sep 27, 2014

@author: jack
'''
from main.Handler.UserHandler import UserHandler
from main.Handler.PointHandler import PointHandler
from main.Handler.UpgradeHandler import UpgradeHandler
from main.Game import Game


username=raw_input("Enter Username: ")
nickname=raw_input("Enter Nickname: ")

user=UserHandler()
user_main=user.createUser(username, nickname)
user_arg=user.getUsername(nickname, False)


start=Game.main(user_arg,0).fromStartEvent()