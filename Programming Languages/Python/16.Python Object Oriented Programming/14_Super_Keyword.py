class A:
    classVar1 = "I am a variable of class A"       # Third Find here

    def __init__(self):
        print("This is constructor of class A.")
        # Now this instance variable will print because we used super method
        self.classVar1 = "I am a variable of class A inside The Constructor"    # First Find here

class B(A):
    classVar1 = "I am a variable of class B"    # Second Find here

    def __init__(self):     # Override the constructor
        super().__init__()
        print("This is constructor of class B.")

        self.classVar1 = "I am a variable of class B inside The Constructor"    # First Find here

a = A()
b = B()
print(b.classVar1)