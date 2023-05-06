try:
    f = open("Har.txt")

except EOFError as e:
    print("EOFError is found! ", e)

except IOError as e:
    print("IOError is found! ", e)

else:
    print("No exception found in program!")  # This block will run if except block will not run.

finally:
    print("This is necessary!")
