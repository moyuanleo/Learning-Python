num=eval(input("请输入一个三位整数:"))
a=num//100 #百位
b=(num%100)//10 #十位
c=(num%100)%10
print("这三个数的反序数是:",c*100+b*10+a)
