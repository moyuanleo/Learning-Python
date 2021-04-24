ls=[str(i)+'*'+str(j)+'='+str(i*j)+('\n' if i==j else ' ') for i in range(1,10) for j in range(1,i+1)]
for item in ls:
    print(item,end='')
