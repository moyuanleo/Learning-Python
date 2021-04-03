n=int(input("请输入项数："))
PI=0
for i in range (1,n+1):
    PI=PI+(-1)**(i+1)*(1/(2*i-1))
print("PI=",PI*4)