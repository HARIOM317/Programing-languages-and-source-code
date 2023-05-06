import math

# ceil() function returns smallest integral value greater than the number. if value is 5.1 than it will return 6.
a = 12.3
b = 11.01
print("ceil of a is: ", math.ceil(a))
print("ceil of b is: ", math.ceil(b))

# fabs() function returns absolute value. if value is -5 than it will return 5
a = -10
print("Absolute value of a is: ", math.fabs(a))

# factorial() function returns factorial of given number.Raises an error if given value is not integral or is negative.
a = 6
print(f"Factorial of {a} is:  {math.factorial(a)}")

# This is Opposite of ceil(). floor() function returns the floor value of given number, it means It Returns the greatest integral value smaller than the number
a = 45.8
b = -20.3
print("Floor value of a is: ", math.floor(a))
print("Floor value of b is: ", math.floor(b))

# fsum() returns accurate floating point sum of values in the iterable.
l = [10, 20.5, 30, 40.5]
print("fsum of list is: ", math.fsum(l))

# sqrt() returns square root of a number.
a = 16
print(f"Square root of {a} is {math.sqrt(a)}")

# find greatest common divisor
a = 49
b = 7
print(f"The GCD of {b} and {a} is: {math.gcd(b, a)}")

# Print power of a number
print(f"2^6 is: ", math.pow(2, 6))