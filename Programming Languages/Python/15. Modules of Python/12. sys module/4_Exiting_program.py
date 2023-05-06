import sys

while True:
    age = int(input("Enter age: "))
    if age < 18:
        # exits the program
        sys.exit("Age less than 18")
    else:
        print("Age is not less than 18")