x=float(input())
y=float(input())
if x>0 and y>0:
    print("第一象限")
elif x>0 and y<0:
    print("第二象限")
elif x<0 and y<0:
    print("第三象限")
elif x<0 and y>0:
    print("第四象限")
