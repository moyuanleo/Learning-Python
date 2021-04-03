a=int(input("请输入投掷的次数："))
import random
count_0=0
count_1=0
for i in range (1,a+1):
    num=random.randint(0,1)     #randint()函数包含首尾两项
    if num==0:
        count_0+=1
    else: count_1+=1
print("0出现的次数为：",count_0)
print("1出现的次数为：",count_1)