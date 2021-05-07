sen=input()
lower_sen=sen.lower()
lst=[]
for i in lower_sen:
    if i not in lst:
        lst.append(i)
print(sorted(lst))