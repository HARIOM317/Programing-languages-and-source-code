def simpleGeneratorFun(n):
    num = 1
    for i in range(1, n+1):
        yield i

def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
        yield fac

x = factorial(10)
y = simpleGeneratorFun(10)
print(f"Factorial of {y.__next__()} is: {x.__next__()} ")
print(f"Factorial of {y.__next__()} is: {x.__next__()} ")
print(f"Factorial of {y.__next__()} is: {x.__next__()} ")
print(f"Factorial of {y.__next__()} is: {x.__next__()} ")
print(f"Factorial of {y.__next__()} is: {x.__next__()} ")
print(f"Factorial of {y.__next__()} is: {x.__next__()} ")
print(f"Factorial of {y.__next__()} is: {x.__next__()} ")
