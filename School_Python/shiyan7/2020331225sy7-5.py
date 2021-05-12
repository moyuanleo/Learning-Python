dic_student={}
for i in range(1,5+1):
    class_name=input("请输入第"+str(i)+"个学生的班级和姓名:")
    age=input("请输入第"+str(i)+"个学生的年龄:")
    dic_student[class_name]=age
for k,v in dic_student.items():
    print("{:<3}\t{}".format(k,v))