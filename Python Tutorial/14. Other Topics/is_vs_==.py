a = [2, 4, 6, 8, 10]
b = a     # Value equality
c = a[:]    # Reference equality by slicing

print(a == b)
print(a is b)
print(a == c)
print(a is c)
print(b == c)
print(b is c)

print()
x = [2, 4, 'xyz', 'abc', 78, 100]
y = [2, 4, 'xyz', 'abc', 78, 100]
print(x == y)
print(x is y)