import inspect
import collections
from tkinter import *

class A:
    pass

class B(A):
    pass

class C(B):
    pass

def func(a, b):
    return a * b

a = A()
root = Tk()
print("\nThe getmro() method of inspect module: \n", inspect.getmro(C))
print("\nThe getclasstree() method of inspect module: \n", inspect.getclasstree(inspect.getmro(C)))
print("\nThe getmembers() method of inspect module: \n", inspect.getmembers(a))
print("\nThe getsource() method of inspect module: \n", inspect.getsource(func))
print("\nThe getmodule() method of inspect module: \n", inspect.getmodule(collections))
print("\nThe getdoc() method of inspect module: \n", inspect.getdoc(root))