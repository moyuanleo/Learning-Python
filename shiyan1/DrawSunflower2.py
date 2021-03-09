'''
Author: your name
Date: 2021-03-09 19:04:32
LastEditTime: 2021-03-09 19:06:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\shiyan1\DrawSunflower2.py
'''
import turtle as t
t.speed(10)
t.color("red","yellow")
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos())<1:
        break
t.end_fill()
t.done()