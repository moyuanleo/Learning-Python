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
print(lst_student[6:9])
print(lst_student[1::3])
age=lst_student[2::3]
ave_age=sum(age)/len(age)
print(ave_age)
