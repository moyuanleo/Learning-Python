myDic={'方糖':99,'X1':499,'魔盒':399,'曲奇':299}
for k,v in myDic.items():
    print("{} ………… {}元".format(k,v))
total = sum(item.get() for item in myDic)/len(myDic)
print(total)
print(type(myDic))