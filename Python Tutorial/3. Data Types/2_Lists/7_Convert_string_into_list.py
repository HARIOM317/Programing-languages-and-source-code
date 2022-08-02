n = input("Enter a string: ")

# For a single string
l1 = n.split()
print("Your First List Is:  ", l1)

l2 = []
# For a multiple string
for a in range(1, 6):
    m = input("Enter sting " + str(a) + "-->  ")
    l2.append(m)

print("\nYour Second List Is:  ", l2)

