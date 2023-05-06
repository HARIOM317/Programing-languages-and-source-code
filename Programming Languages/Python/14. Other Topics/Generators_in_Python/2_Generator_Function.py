def febonnaci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

def factorial(n):
    fac = 1

    for i in range(n):
        fac = fac * (i+1)
        yield fac

choice = int(input('''
___________Choose any option for continue____________
1. Febonnaci number
2. factorial
'''))

if choice == 1:
    num = int(input("Enter any number:  "))
    print("The febonnaci sequence is as below: ")
    for i in febonnaci(num):
        print(i, end=" ")
elif choice == 2:
    num = int(input("Enter any number:  "))
    Number = 1
    for i in factorial(num):
        print(f"Factorial of {Number} is :  {i}")
        Number += 1
else:
    print("Invalid input!")
