#例3-26
n=int(input("请输入数列项数："))
x1=1
x2=1
count=2
print("{:>10}{:>10}".format(x1,x2),end='')
for i in range(3,n+1):
    x3=x1+x2
    print("{:>10}".format(x3),end='')
    count+=1
    if count%4==0:
        print()
    x1=x2
    x2=x3