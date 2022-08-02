a = input("Enter first number: ")
b = input("Enter second number: ")

try:
    print("The sum of these two numbers is: ", int(a) + int(b))

except Exception as e:
    print(e)

print("The exception handling ia working properly!")