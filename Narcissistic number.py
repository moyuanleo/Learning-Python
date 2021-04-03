n=int(input("请输入要查找的n以内的水仙花数(n>100):"))
for i in range (100,n+1):
    a=i//100
    b=i//10%10
    c=i%10
    if a**3+b**3+c**3==i:
        print(i,end=" ")