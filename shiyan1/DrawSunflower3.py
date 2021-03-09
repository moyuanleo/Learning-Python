'''
Author: your name
Date: 2021-03-09 19:08:44
LastEditTime: 2021-03-09 19:09:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\shiyan1\DrawSunflower3.py
'''
from turtle import*
speed(10)
color("red","yellow")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()