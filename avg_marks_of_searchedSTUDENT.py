import os

students = {}

num_of_students = int(input())
for i in range(num_of_students):
    details = str(input())
    student_marks = []
    student_name, st_mark_1, st_mark_2, st_mark_3 = details.split(' ')
    st_mark_1 = float(st_mark_1)
    st_mark_2 = float(st_mark_2)
    st_mark_3 = float(st_mark_3)
    student_marks.append(st_mark_1)
    student_marks.append(st_mark_2)
    student_marks.append(st_mark_3)
    students[student_name] = student_marks

search_student = str(input())
if search_student in students :
    marks = students[search_student]
    total = sum(marks)
    avg = total/3
    print('{:.2f}'.format(avg))



# students = {}
# num_of_students = int(input())
# for i in range(num_of_students):
#     student_marks = []
#     student_name = str(input())
#     for j in range(3):
#         marks = int(input())
#         student_marks.append(marks)
#         students[student_name] = student_marks

# search_student = str(input())
# if search_student in students :
#     marks = students[search_student]
#     total = sum(marks)
#     avg = total/3
#     print('{:.2f}'.format(avg))
