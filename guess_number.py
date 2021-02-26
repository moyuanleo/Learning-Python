'''
Author: your name
Date: 2021-02-26 20:00:43
LastEditTime: 2021-02-26 20:06:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\guess_number.py
'''
import random as rd
target = rd.randint(1,100)
print("已经产生一个1~100之间的随机整数，猜猜该数的数值。")
count = 0
while True:
    guess = eval(input("请输入猜测的数值："))
    count+=1
    if guess>target:
        print("猜的太大了！")
    elif guess<target:
        print("猜的太小了！")
    else:
        print("猜的好棒，{}次就猜中了".format(count))
        break