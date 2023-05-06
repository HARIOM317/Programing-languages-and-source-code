class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def Explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    # Getter method
    def Email(self):
        if self.fname == None and self.lname == None:
            return f"Your Email is not set. Please set it using setter..."
        return f"{self.fname}{self.lname}484@gmail.com"

    @Email.setter

    # Setter method
    def Email(self, string):
        print("Setting Now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @Email.deleter
    # Deleter method
    def Email(self):
        print("\nYour Email has been deleted successfully!")
        self.fname = None
        self.lname = None

emp1 = Employee("Hariom", "mewada")

print("My first name :  ", emp1.fname)
print("My last name :  ", emp1.lname)
print("My old Email is: ", emp1.Email)
emp1.lname = "Rajput"
print("My new Email is: ", emp1.Email)

print()
emp1.Email = "Harionsingh.Rajput@gmail.com"
print("My newest email is: ", emp1.Email)
print("My first name :  ", emp1.fname)
print("My last name :  ", emp1.lname)

del emp1.Email
print(emp1.Email)