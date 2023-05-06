try:
    f = open("HSR.txt")

except Exception as e:
    print(e)

finally:
    print("This block is necessary")
    