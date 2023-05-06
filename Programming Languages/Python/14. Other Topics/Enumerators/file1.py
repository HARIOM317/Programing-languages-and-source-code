def printhar():
    return f"This is a string!"

def add(a, b):
    return a + b

print("The name is ", __name__)
if __name__ == '__main__':  # This content will not print in other python file if we import this file in that python program

    print(printhar())
    addition = add(5, 6)
    print(addition)