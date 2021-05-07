from math import*
a=float(input())
b=float(input())
c=float(input())
s=0.0
l=0.0
if(a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a):
    l=a+b+c
    h=0.5*l
    s=sqrt(h*(h-a)*(h-b)*(h-c))
    print("三角形的周长为:{:.1f}".format(l))
    print("三角形的面积为:{:.1f}".format(s))
else:print("输入的三边无法构成三角形")
    
