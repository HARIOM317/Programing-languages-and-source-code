s1 = set([12, 34, 56, 98, 2, 90, 3])
print(s1)

s = ["Hariom", "Raju", "Komal", "Suresh", "Yogendra"]
s2 = set(s)
print(s2)

print(type(s1))
print(type(s2))

s3 = set()  # Create a empty set

# Adding elements in set by using add method
s3.add(5)
s3.add(3)
s3.add(6)
s3.add(3)   # Cannot add any duplicate value in set
s3.add(23)
s3.add(12)

print(s3)