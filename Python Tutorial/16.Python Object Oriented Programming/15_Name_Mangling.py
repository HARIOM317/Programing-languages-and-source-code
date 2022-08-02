class My_Data:
    # Private Access Specifier
    __Name = "Hariom"
    __Semester = 3
    __Collage = "SISTech"
    __GPA = 8.5
    # Protected Access Specifier
    _Course = "B.Tech"

Student = My_Data()
# print("My name is: ", Student.__Name)     # This will give an error because we can't use private specifier Outside the class

# We will use Name Mangling for using Private data of the class
print("My name is: ", Student._My_Data__Name)
print("Semester: ", Student._My_Data__Semester)
print("Collage: ", Student._My_Data__Collage)
print("GPA: ", Student._My_Data__GPA)

# There is no need to use name mangling because it is a Protected specifier
print("Course: ", Student._Course)
print(dir(Student))
