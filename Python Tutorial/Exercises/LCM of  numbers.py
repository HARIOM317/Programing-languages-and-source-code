a = int(input("Enter first number :  "))
b = int(input("Enter second number :  "))

maxNum = max(a, b)

while(True):
    if(maxNum %a == 0 and maxNum % b == 0):
        break
    maxNum = maxNum + 1

print(f"The LCM of {a} and {b} is {maxNum}")
