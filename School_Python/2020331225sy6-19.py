lst=[("triangle","shape"),("red","color"),("square","shape"),
("yellow","color"),("green","color"),("circle","shape")]
lst_new=[[x[1],x[0]] for x in lst]
lst_sort=sorted(lst_new)
print(lst_sort)
lst_colors=[x[1] for x in lst_sort if x[0]=="color"]
print(lst_colors)