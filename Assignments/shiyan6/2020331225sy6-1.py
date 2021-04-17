import random
lst_who=['小马','小羊','小鹿']
lst_where=['草地上','电影院','家里']
lst_what=['看电影','听故事','吃晚饭']
a=random.randint(0,2)
b=random.randint(0,2)
c=random.randint(0,2)
print(a,b,c)
print(lst_who[a]+"在"+lst_where[b]+lst_what[c])
