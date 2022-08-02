class A:
    classVar1 = "I am a variable of class A"       # Third Find here

    def __init__(self):
        # Now this instance variable will not print because this constructor has been override
        self.classVar1 = "I am a variable of class A inside The Constructor"    # First Find here

class B(A):
    classVar1 = "I am a variable of class B"    # Second Find here

    def __init__(self):     # Override the constructor
        # self.classVar1 = "I am a variable of class B inside The Constructor"    # First Find here
        pass


a = A()
b = B()
print(b.classVar1)