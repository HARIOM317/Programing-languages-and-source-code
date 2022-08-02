# program to illustrate public access modifier in a class

class First:

    # constructor
    def __init__(self, name, age):
        # public data members
        self.Name = name
        self.Age = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.Age)


# creating object of the class
obj = First("R2J", 20)

# accessing public data member
print("Name: ", obj.Name)

# calling public member function of the class
obj.displayAge()