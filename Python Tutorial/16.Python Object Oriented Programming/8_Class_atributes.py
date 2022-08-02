class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    def display_details(self):
        print("Name:%s, ID:%d, age:%d" %(self.name,self.id, self.age))
s = Student("John",101,22)
s.display_details()
print(s.__doc__)
print(s.__dict__)
print(s.__module__)
