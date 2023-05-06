apples = int(input("Enter Number of Apples: "))
mn = int(input("Enter the minimum number to check:  "))
mx = int(input("Enter the maximum number to check:  "))
for i in range(mn, mx + 1):
    if apples % i == 0:
        print(f"{i} is a divisor of {apples}")
    else:
        print(f"{i} is not a divisor of {apples}")
