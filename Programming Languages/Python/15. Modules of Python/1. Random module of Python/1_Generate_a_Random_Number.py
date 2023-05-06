import random
random_number = random.randint(1, 100)      # Generate a random number between 1 to 100
print("Random number is: ", random_number)

# Print random number 1 - 50 (Not 51) and take 2 steps, it means print only odd numbers
print("Random randrange = ", random.randrange(5, 51, 2))

rand = random.random() * 100   # Generate a floating point random number between 0 to 100
print("Floating point random number is: ", rand)
print(random.random())  # this will print a random number between 0 to 1
