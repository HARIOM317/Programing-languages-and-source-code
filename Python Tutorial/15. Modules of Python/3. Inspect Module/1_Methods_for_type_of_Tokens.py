import inspect
class A:
    def Cube(self, a):
        return a * a * a
    pass

def Sqrt(self,a):
    return a*a

a = A()

# isclass
print(inspect.isclass(A))

# ismodule
print(inspect.ismodule(inspect))

# isfunction
print(inspect.isfunction(Sqrt))
print(inspect.isfunction(a.Cube))

# ismethod
print(inspect.ismethod(Sqrt))
print(inspect.ismethod(a.Cube))
