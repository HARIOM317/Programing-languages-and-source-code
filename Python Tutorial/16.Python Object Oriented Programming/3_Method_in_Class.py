class Employee:
    no_of_Leaves = 10
    def Print_Details(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

hariom = Employee()
Abhishek = Employee()

hariom.salary = 2500000
hariom.name = "Hariom"
hariom.role = "Software Engineer"

Abhishek.salary = 300000
Abhishek.name = "Abhishek"
Abhishek.role = "Product Manager"

print(hariom.Print_Details())
print(Abhishek.Print_Details())