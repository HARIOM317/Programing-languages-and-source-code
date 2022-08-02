class Employee:

    def __init__(self, Name, Role, Salary):
        self.name = Name
        self.role = Role
        self.salary = Salary

    @classmethod
    def from_slash(cls, string):
        # params = string.split("/")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("/"))      # This is one liner of above code

Raj = Employee.from_slash("Raj Rajput / Manager / 35000")
Hariom = Employee.from_slash("Hariom Rajput / Instructor / 85000")
print(f"Details of Employee: Name is {Raj.name}, salary is {Raj.salary} and role is {Raj.role}")
print(f"Details of Employee: Name is {Hariom.name}, salary is {Hariom.salary} and role is {Hariom.role}")