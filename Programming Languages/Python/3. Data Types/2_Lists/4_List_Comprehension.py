l = []
# Normal way to create a list by using for loop
print("Creating list by using for loop...")
for i in range(1, 11):
    l.append(i)

print(l)

# Creating a list by using list comprehension
print("\nCreating list by using list comprehension...")
n = [m for m in range(1, 11)]
print(n)

# Give a condition by using list comprehension
print("\nEven numbers are...")
x = [y for y in range(1, 21) if y%2 == 0]
print(x)

# Convert a string into list  by using list comprehension
Str = "WELL-COME BACK"
b = [a for a in Str]
print("\nGiven string in list is..")
print(b)
