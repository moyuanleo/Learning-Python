print("1000以内的孪生素数对有：")
for n in range (3,1000):
    for i in range (2,n):
        if n%i==0:
            break
    m=n+2
    for j in range (2,m):
        if m%j==0:
            break
    if i==n-1 and j==m-1:
        print(n,",",m)