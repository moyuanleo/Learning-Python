def func(n):
    f1 = 1
    f2 = 1
    for x in range(1, n+1):
        if x == 1:
            print(1, end=' ')
            continue
        elif x == 2:
            print(1, end=' ')
            continue
        f1, f2 = f2, f1+f2
        print(f2, end=' ')

        if x % 5 == 0:
            print()


func(20)