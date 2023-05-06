class Employee:
    def __init__(self, Name, Role, Salary):
        self.name = Name
        self.role = Role
        self.salary = Salary

    def Print_Details(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

    # Dunder methods
    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

    def __repr__(self):
        return f"Employee('{self.name}', '{self.role}', {self.salary})"

    def __str__(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

    def __len__(self):
        return len(self.name)


emp1 = Employee("Hariom", "Programmer", 100000)
emp2 = Employee("Abhishek", "Manager", 500000)

print(emp1+emp2)
print(emp1-emp2)
print(emp1*emp2)
print(emp1/emp2)
print(emp1//emp2)
print(emp1)
print(repr(emp1))
print(len(emp2))
