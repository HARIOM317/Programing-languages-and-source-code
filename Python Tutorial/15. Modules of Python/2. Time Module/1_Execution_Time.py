import time
initial1 = time.time()

i = 0
print("Using while loop")
while i < 10:
    print("I am Hariom!")
    i += 1
print("Time of while loop is: ", time.time() - initial1, "seconds")

initial2 = time.time()

print("\nUsing for loop")
for i in range(10):
    print("I am Hariom!")

print("Time of for loop is: ", time.time() - initial2, "seconds")
