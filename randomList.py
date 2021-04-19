import random

def randomList(n):
    '''返回一个长度为n的整数列表，数据范围[0,1000)'''
    iList = []
    for i in range(n):
        iList.append(random.randrange(1000))
    return iList

if __name__ == "__main__":
    iList= randomList(10)
    print(iList)