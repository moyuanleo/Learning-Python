from randomList import randomList
from quickSort import quickSort
import timeit
iList=quickSort(randomList(20))
print(iList)
x=int(input("请输入待查找的数："))

def binarySearch(iList,key):
    low=0
    high=len(iList)-1
    while low<=high:
        mid=(low+high)//2
        if iList[mid]<x:
            low=mid+1
        elif iList[mid]>x:
            high=mid-1
        else:
            print("找到{},索引为{}！".format(x,mid));
            break;
    else:
        print("没有找到{}".format(x))
binarySearch(iList,x)
print(timeit.timeit())