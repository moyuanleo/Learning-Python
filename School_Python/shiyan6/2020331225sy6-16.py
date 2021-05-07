lst_floor=[1,4,2,5,7,3]
for i in range(1,len(lst_floor)):
    end=lst_floor[i]
    begin=lst_floor[i-1]
    if begin<end:
        print("↑"*(end-begin),end="")
    else:
        print("↓"*(begin-end),end="")
print()

path="↑↑↓↓↓↑↑↓↑↑↑↑"
lst_floor=[2]
floor=2
for a in path:
    if a=="↑":
        floor+=1
    else:
        floor-=1
    lst_floor.append(floor)
print(",".join([str(x) for x in lst_floor]))