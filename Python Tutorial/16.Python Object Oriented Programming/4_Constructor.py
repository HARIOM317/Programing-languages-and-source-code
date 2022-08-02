class Employee:
    # def __init__(self, Name, Role, Salary):
    #     self.name = Name
    #     self.role = Role
    #     self.salary = Salary

    # We can also change self keyword to another keyword.

    def __init__(Hsr, Name, Role, Salary):
        Hsr.name = Name
        Hsr.role = Role
        Hsr.salary = Salary

Hariom = Employee("Hariom", "Software developer", 10000000)
print(f"Name is {Hariom.name}, Role is {Hariom.role} and Salary is {Hariom.salary}")
