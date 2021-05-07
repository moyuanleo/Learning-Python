count1=0
count2=0
odd_sum=0
even_sum=0
i=input()
while(i!='A'):
    b=eval(i)
    if (b%2)!=0:
        odd_sum+=b
        count1+=1
    else:
        even_sum+=b
        count2+=1
    i=input()
print("odd_sum=",odd_sum)
print("even_sum=",even_sum)
print("average=",(odd_sum+even_sum)/(count1+count2))    