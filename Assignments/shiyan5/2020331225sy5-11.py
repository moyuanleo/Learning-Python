def hcf(x, y):      #该方法返回两个数的最大公约数
   if x > y:
       smaller = y
   else:
       smaller = x
 
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i
 
   return hcf

def lcm(x, y):      #该方法返回两个数的最小公倍数
   if x > y:
       greater = x
   else:
       greater = y
 
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
 
   return lcm

import random
RND1=random.randint(0,100)
RND2=random.randint(0,100)
print("RND1=",RND1)
print("RND2=",RND2)
print( RND1,"和",RND2,"的最大公约数为", hcf(RND1,RND2))
print( RND1,"和",RND2,"的最小公倍数为", lcm(RND1,RND2))