class A:
    def Met(self):
        print("This is a method of class A")

class B(A):
    def Met(self):
        print("This is a method of class B")

class C(A):
    def Met(self):
        print("This is a method of class C")

class D(B, C):
    def Met(self):
        print("This is a method of class D")

a = A()
b = B()
c = C()
d = D()
print(d.Met())
