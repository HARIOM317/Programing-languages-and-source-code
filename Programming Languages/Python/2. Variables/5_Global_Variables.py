l = "Hello"      # Global variable
def function1(x):
    m = 125     # Local variable
    print(l, x, "! How are you?")
    print(m)

print(l, "HSR")
# print(m)    # This will throw an error because m is a local variable

function1("Hariom")