num1 = float(input("Enter first Number "))
num2 = float(input("Enter second Number "))
operation = input("Enter an Operator ['+','-','*','/'] ")
if operation == '+':
    if num1 == 56 and num2 == 9 or num2 == 56 and num1 == 9:
        print("Your answer is 77")
    else:
        print("your answer is: ", num1+num2)

elif operation == '-':
        print("your answer is: ", num1-num2)

elif operation == '*':
    if num1 == 45 and num2 == 3 or num2 == 45 and num1 == 3:
        print("Your answer is 444")
    else:
        print("your answer is: ", num1*num2)

elif operation == '/':
    if num1 == 56 and num2 == 6 or num2 == 56 and num1 == 6:
        print("Your answer is 4")
    else:
        print("your answer is: ", num1/num2)

else:
    print("Please choose a valid operator")