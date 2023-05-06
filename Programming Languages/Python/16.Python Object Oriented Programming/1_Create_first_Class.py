class student:      # Creating a class
    pass

student_1 = student()   # Creating object 1 of class student
student_2 = student()   # Creating object 2 of class student
student_3 = student()   # Creating object 3 of class student

student_1.name = "Hariom"
student_1.sem = 2
student_1.section = "B1"
student_1.application_no = "ME022256A"

student_2.name = "Abhishek"
student_2.sem = 2
student_2.section = "B1"
student_2.application_no = "ME0228956A"

student_3.name = "Raju"
student_3.sem = 3
student_3.section = "A2"
student_3.application_no = "CS025460A"

print(student_1.application_no)
print(student_1.name)
print(student_1.sem)
print(student_1.section)