num1 = int(input("Enter first number :  "))
num2 = int(input("Enter second number :  "))

if num1 < num2:
    mn = num1
else:
    mn = num2

for i in range(1, mn + 1):
    if(num1 % i == 0 and num2 % i == 0):
        HCF = i

print(f"The HCF/GCD of {num1} and {num2} is :  {HCF}")
