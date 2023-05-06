from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):    # Force for making printarea function in all child classes
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 9
    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())
# rect2 = Shape()       # Can't make the object of abstract class Shape
