s="Whether the weather be fine, or whether the weather be not. \
Whether the weather be cold, or whether the weather be hot. \
We will weather the weather whether we like it or not. "
s=s.lower()
s=s.replace(',',' ')
s=s.replace('.',' ')
#print(s)
lists=s.split(' ')
sets=set(lists)
#print(lists)
#print(sets)
a=list(sets)
for item in a:
    print(item, s.count(item))