def factorial(n):
    """
    This a iterative method for factorial of a number. This is not a batter approach for factorial but it is easy.
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return  fac

def factorial_recursive(n):
    """
    This a recursive method for factorial of a number
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorialTrailingZeros(number):
    count = 0
    i = 5
    while(number//i != 0):
        count += int(number/i)
        i = i * 5
    return count

number = int(input("Enter a number: "))

print("Factorial using iterative method:")
print("Factorial of", number, "is:", factorial(number))
print("factorial trailing zeros = ", factorialTrailingZeros(number))

# print("\nFactorial using recursive method:")      # Not work for a long number
# print("Factorial of", number, "is:", factorial_recursive(number))
