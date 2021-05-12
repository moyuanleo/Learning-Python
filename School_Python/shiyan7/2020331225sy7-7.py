myDic={'John':"123",'Marry':"111",'Tommy':"123456"}
name=input("请输入用户名：")
if name not in myDic:
    print("用户名不正确!")
else:
    password=input("请输入密码:")
    if password != myDic[name]:
        print("密码不正确!")
    else:
        print("成功登录!")