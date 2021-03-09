'''
Author: your name
Date: 2021-03-09 19:44:58
LastEditTime: 2021-03-09 19:48:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\shiyan2\7.py
'''
from math import*
a=eval(input("请输入三角形的第1条边长："))
b=eval(input("请输入三角形的第2条边长："))
c=eval(input("请输入三角形的第3条边长："))
l=(a+b+c)/2
s=sqrt(l*(l-a)*(l-b)*(l-c))
print("改三角形的面积为：",s)