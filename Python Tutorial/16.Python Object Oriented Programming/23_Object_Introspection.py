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

# Type
a = 5
b = [1, 2, 3, 4, 5]
print("\nObject Introspection using type method: ")
print("Type of string Hello is: ", type('Hello'))
print("Type of object of the class is: ", type(emp1))
print("Type of a is: ", type(a))
print("Type of b is: ", type(b))

# str
a = str(a)
b = str(b)
print("\nObject Introspection using str method: ")
print("After Typecasting type of a is: ", type(a))
print("After Typecasting type of b is: ", type(b))

# id
print("\nObject Introspection using id method: ")
print("Id of given string is: ", id('Well Come'))
print("Id of given string is: ", id('Well Come Back'))
print("Id of a is: ", id(a))

# dir
string = "Good Morning"
print("\nObject Introspection using dir method: ")
print("Information about given string is: ", dir(string))
print("Information about given object is: ", dir(emp1))

# import inspect
# print(inspect.getmembers())