'''
Author: your name
Date: 2021-03-09 19:10:08
LastEditTime: 2021-03-09 19:22:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learning Python\shiyan1\DrawTaiJI.py
'''
from turtle import*
def yin(radius,color1,color2):
    width(3)
    color("black",color1)
    begin_fill()
    circle(radius/2.,180)
    circle(radius,180)
    left(180)
    circle(-radius/2.,180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1,color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200,"black","white")
    yin(200,"white","black")
    ht()
    return "Done!"

main()