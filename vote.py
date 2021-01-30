'''
Author: your name
Date: 2021-01-30 21:40:11
LastEditTime: 2021-01-30 22:09:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\vote.py
'''
voted={}

def check_voter(name):
    if voted.get(name):
        print("kick it out!")
    else:
        voted[name] = True
        print("let them vote!")
check_voter("tom")
check_voter("tom")
check_voter("leo")