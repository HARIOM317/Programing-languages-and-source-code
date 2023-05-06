import sys

def print_to_stderr(*a):
    # Here a is the array holding the objects passed as the argument of the function
    print(*a, file=sys.stderr)

print_to_stderr("Hello World")