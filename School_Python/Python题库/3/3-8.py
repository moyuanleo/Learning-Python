#coding：utf-8 
'''------------------------------------------------------
【程序设计】
---------------------------------------------------------

题目：孙子问题

描述：在我国古代算书《孙子算经》中有这样一个问题：
      “今有物不知其数，三三数之剩二，五五数之剩三，
      七七数之剩二，问物几何？”意思是，“一个数除
      以3余2，除以5余3，除以7余2.求适合这个条件的
      最小数。”请给出你的解法

要求：

     输入格式：
     此题无输入

     输出格式：
     一个正整数

---------------------------------------------------------
注意：仅在注释标志之间填入所编写语句。
------------------------------------------------------'''
#**********Program**********
for i in range(1,100):
    if i%3==2 and i%5==3 and i%7==2:
       print(i)







#**********  End  **********