#找出1000以内的所有完全数 例3-24
for n in range (1,999+1):
    sum=0
    for i in range (1,n):
        if n % i == 0:
            sum+=i
    if sum == n:
        print(n,end="  ")