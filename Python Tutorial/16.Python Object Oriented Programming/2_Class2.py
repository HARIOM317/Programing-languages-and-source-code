class Employee:
    no_of_Leaves = 10

hariom = Employee()
Abhishek = Employee()

hariom.salary = 2500000
hariom.name = "Hariom"
hariom.role = "Software Engineer"

Abhishek.salary = 300000
Abhishek.name = "Abhishek"
Abhishek.role = "Product Manager"

print(Employee.no_of_Leaves)
print(hariom.no_of_Leaves)
print(Abhishek.no_of_Leaves)

hariom.no_of_Leaves = 12
print(hariom.__dict__)
print(Abhishek.__dict__)
print(Employee.no_of_Leaves)