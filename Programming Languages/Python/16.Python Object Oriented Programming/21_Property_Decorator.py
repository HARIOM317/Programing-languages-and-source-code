class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.Email = self.fname + self.lname + "1000@gmail.com"       # Cannot change the new email.

    def Explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    # It can change the new email.
    @property
    def Email(self):
        return f"{self.fname}{self.lname}444@gmail.com"

emp1 = Employee("Hariom", "mewada")
emp2 = Employee("Abhi", "mewada")
print("My old Email is: ", emp1.Email)
emp1.lname = "Rajput"
print("My new Email is: ", emp1.Email)
