import random
num=random.randint(0,9)
#print(num)
count=0
while True:
    guess=int(input("请输入现在是什么数字："))
    count+=1
    if guess==num:
        print("预测{}次，你猜中了".format(count))
        break
    elif guess>num:
        print("遗憾，太大了")
    elif guess<num:
        print("遗憾，太小了")