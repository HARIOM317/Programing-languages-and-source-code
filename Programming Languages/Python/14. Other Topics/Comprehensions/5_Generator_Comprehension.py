# Creating generator by using comprehension
evens = (x**3 for x in range(1, 11) if x % 2 == 0)
print(type(evens))
print("Cube of Even numbers[1 - 10] : ")
for items in evens:
    print(items, end=" ")
