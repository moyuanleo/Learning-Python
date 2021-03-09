'''
Author: your name
Date: 2021-03-09 19:38:32
LastEditTime: 2021-03-09 19:44:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\shiyan2\6.py
'''
num=eval(input("请输入一个三位整数:"))
a=num//100 #百位
b=(num%100)//10 #十位
c=(num%100)%10
print("这三个数的反序数是:",c*100+b*10+a)
