import math
gamma_var = 6
# Printing the gamma value.
print("The gamma value of the given argument is : ", math.gamma(gamma_var))

# checking isinf() values with inbuilt numbers
print(math.isinf(math.pi))
print(math.isinf(math.e))
# checking for inf value
print(math.isinf(float('inf')))

# checking isnan() values with inbuilt numbers
print(math.isnan(math.pi))
print(math.isnan(math.e))
# checking for NaN value
print(math.isnan(float('nan')))