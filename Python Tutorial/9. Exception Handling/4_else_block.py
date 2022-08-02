try:
    f = open("Hariom.txt")

except Exception as e:
    print("Exception found!")
    print(e)
    
else:
    print("No exception found in program!")     # This block will run if except block will not run.

finally:
    print("This is necessary!")
