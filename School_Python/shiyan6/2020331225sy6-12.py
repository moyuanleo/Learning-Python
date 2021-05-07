lst_odd=[1,3,5,7,9]
lst_even=[2,4,6,8,10]
lst=lst_odd.copy()
lst.extend(lst_even)
lst.sort(reverse= True)
print(lst)