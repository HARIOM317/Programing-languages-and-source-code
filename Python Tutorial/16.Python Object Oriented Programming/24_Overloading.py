class Area:
    def findArea(self, a=None, b=None):
        if a != None and b != None:
            print("Area of rectangle is: ", a * b)
        elif a != None:
            print("Area of square is: ", a * a)
        else:
            print("Nothing to find")

obj = Area()
obj.findArea()
# Function Overloading
obj.findArea(10)
obj.findArea(10, 20)
