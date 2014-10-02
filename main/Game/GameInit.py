'''
Created on Sep 27, 2014

@author: jack
'''
from main.Handler.UserHandler import UserHandler
from main.Handler.PointHandler import PointHandler
from main.Game import Game


username=raw_input("Enter Username: ")
nickname=raw_input("Enter Nickname: ")

user=UserHandler()
user_main=user.createUser(username, nickname)
user_arg=user.getUsername(nickname, False)


'''
If you wanted to add points.
score.addPoint(10, False)
#DebuggingFTW.
'''
start=Game.main(user_arg)