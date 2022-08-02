class A:
   def displayInfo1(self, name=''):
       return f"Well come back {name} in class A"

   def displayInfo2(self, name=''):
       print(f"Well come back {name} in class A")

class B(A):
   def displayInfo1(self, name=''):     # Function Overriding
       super().displayInfo1()    # Calling displayInfo1() function of base class A by using super keyword.
       return f"Well come back {name} in class B"

   def displayInfo2(self, name=''):     # Function Overriding
       super().displayInfo2()    # Calling displayInfo2() function of base class A by using super keyword.
       print(f"Well come back {name} in class B")

a = B()
print("When function return somethind!")
print("print: ", a.displayInfo1())
print("print: ", a.displayInfo1("Abhishek"))    # Function Overloading

print("\nWhen function return nothing!")
print("return: ", a.displayInfo2())
print("return: ", a.displayInfo2("Hariom"))  # Function Overloading
