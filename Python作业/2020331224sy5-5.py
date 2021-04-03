a=1
b=1
for i in range(4):
    for j in range(5):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
    print()
