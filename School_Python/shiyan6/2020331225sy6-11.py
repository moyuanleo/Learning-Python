lst_info=[["李玉","男",25],["金忠","男",23],["刘妍","女",21],
["莫心","女",24],["沈冲","男",28]]
name=input("请输入要删除的姓名：")
while name!="0":
    for info in lst_info:
        if info[0]==name:
            lst_info.remove(info)
            print(lst_info)
            break
    else:
        print("员工不存在！")
    name=input("请输入要删除的姓名：")
print("程序结束！")