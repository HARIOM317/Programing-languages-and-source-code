def Avg(a, b):
    """This is a function which calculates the average of two numbers"""
    # The above line is not a comment, it is a doc string of a function
    avg = (a + b)/2
    return avg

print(Avg.__doc__)
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
ans = Avg(x, y)
print("Average = ", ans)

