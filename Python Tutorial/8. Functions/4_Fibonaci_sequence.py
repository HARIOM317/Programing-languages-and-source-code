def febonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return febonacci(n-1) + febonacci(n-2)

number = int(input("Enter a number: "))
# print(number, "th index is of fibonacci series is:", febonacci(number))

print("Your fibonacci series is:")
for i in range(number):
    print(febonacci(i), end=" ")

