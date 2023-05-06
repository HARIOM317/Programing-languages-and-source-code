num1 = int(input("Enter a number :  "))
i = 1
print("Table using while loop")
while i <= 10:
    print(num1, " X ", i, " = ", num1 * i)
    i += 1
num2 = int(input("Enter a number again :  "))
print("Table using for loop")

for j in range(1, 11):
    print(num2, " * ", j, " = ", num2*j)
    j -= 1
