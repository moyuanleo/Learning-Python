m=int(input("请输入数字1~12："))
months="JanFebMarAprMayJunJulAugSepOctNovDec"
pos=(m-1)*3
print(m,"月对应的英文缩写是：",months[pos:pos+3])
