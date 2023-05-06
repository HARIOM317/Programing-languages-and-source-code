try:
    name = input("Enter your name? :  ")
    if name == "Hariom" or name == "hariom" or name == 'HARIOM':
        raise ValueError("Hariom is blocked!")

    if name.isnumeric():
        raise Exception("Numbers are not allowed.")

    age = int(input("How old are you? :  "))
    if age == 0:
        raise ZeroDivisionError("Age can not be 0")

except ValueError as e:
    print(e)

except Exception as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

if name == "Hariom" or name == "hariom" or name == 'HARIOM':
    print("Gate Out...")
else:
    print(f"Hello {name}")
