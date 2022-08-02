num1 = int(input("Enter a number: "))
num2 = int(input("Enter a boolean condition: "))

if bool(num2) == False:
    for i in range(num1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
else:
    for i in range(1, num1+1):
        for j in range(i):
            print("*", end=" ")
        print()
