f = open("Hariom.txt")

# tell() function is used for knowing the exact file pointer location(index number where pointer is present).
print(f.tell())
print(f.readline())

print(f.tell())
print(f.readline())

print(f.tell())
print(f.readline())

print(f.tell())
print(f.readline())

print(f.tell())
f.close()