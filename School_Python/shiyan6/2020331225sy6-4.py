lst_busstop=["龙江新城市","阳光广场","汉江路","嫩江路","清凉山公园","拉萨路","五台山","莫愁路"]
begin=input("请输入起始站：")
end=input("请输入终点站：")
b=lst_busstop.index(begin)
e=lst_busstop.index(end)
#print(b,e)
if b<e:
    print("从"+begin+"站前往"+end+"站需要{:}站路".format(e-b))
else:
    print("您需要乘坐反方向线路")
