'''
Author: moyuanleo
Date: 2021-02-26 19:46:36
LastEditTime: 2021-02-26 19:52:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\huitu.py
'''

import turtle as t
import math
t.pensize(2)
t.right(90)
t.penup()
t.forward(200)
t.pendown()
t.left(90)
r=20
t.circle(r)
len=r*math.sqrt(3)
t.left(60)
t.forward(len)
t.left(120)
t.forward(len)
t.left(120)
t.forward(len)