lst_student=["001","李梅",19,"002","刘祥",20,"003","张武",18]
lst_student.append("004")
lst_student.append("刘宁")
lst_student.append(20)
lst_student.append("006")
lst_student.append("梁峰")
lst_student.append(19)
lst_student.insert(12,"005")
lst_student.insert(13,"林歌")
lst_student.insert(14,20)
print(lst_student)
info_3=lst_student[6:9]
print(info_3)
name=lst_student[1::3]
print(name)
age=lst_student[2::3]
total=0
for ele in range(0, len(age)):
    total = total + age[ele]
#print(total)
ave_age=total/6
print(ave_age)