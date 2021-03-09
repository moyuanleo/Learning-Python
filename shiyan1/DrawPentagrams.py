'''
Author: your name
Date: 2021-03-09 18:55:36
LastEditTime: 2021-03-09 18:58:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\shiyan1\DrawPentagrams.py
'''
import turtle as t
t.fillcolor("red")
t.begin_fill()
while True:
    t.forward(200)
    t.right(144)
    if abs(t.pos())<1:
        break
t.end_fill()
t.done()