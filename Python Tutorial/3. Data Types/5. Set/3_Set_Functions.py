s1 = set([1, 3, 2, 5, 72, 9, 10, 4, 3])     # This is first way to create a set
s2 = {38, 98, 76, 1, 34, 45, 4, 87}     # This is second way to create a set
print("Type of s1 is: ", type(s1))
print("Type of s2 is: ", type(s2))

print("\nBefore update s1: ", s1)

# Update the set by adding some new elements
s1.update([12, 34, 76])
s1.update(s2)

print("After update s1: ", s1)

# Delete some elements from the set

# If element not exist in set than it will not throw error
s1.discard(72)
s1.discard(34)
# If element not exist in set than it will throw an error
s1.remove(3)
s1.remove(87)
# The pop() function will randomlly delete element from the set
print("Popped element is: ", s1.pop())
print("Popped element is: ", s1.pop())
print("Popped element is: ", s1.pop())

print("After Delete some element, s1: ", s1)

print("Length of s1 is: ", len(s1))
print("Max element of s1 is: ", max(s1))
print("Min element of s1 is: ", min(s1))
print(s1.isdisjoint(s2))

print("Elements of s2 are: ", s2)
# Adding new elements in s2
s2.add(4)
s2.add(5)

print("Now Elements of s2 are: ", s2)

# Remove all elements from set s2
s2.clear()
print("After clear s2 is: ", s2)
