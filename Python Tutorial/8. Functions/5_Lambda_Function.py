# Lambda function is also known as anonymous function
# This is a one liner function

add = lambda x, y: x + y
minus = lambda x, y: x - y
product = lambda x, y: x * y
divide = lambda x, y: x / y

x = float(input("Enter first number:"))
y = float(input("Enter second number:"))
print("Addition of", x, "and", y, "is:", add(x, y))
print("Subtraction of", x, "and", y, "is:", minus(x, y))
print("Multiplication of", x, "and", y, "is:", product(x, y))
print("Division of", x, "and", y, "is:", divide(x, y))
