f = open("Hariom.txt")

print(f.tell())
print(f.readline())
f.seek(0)   # This will reset the file pointer location according to index value

print(f.tell())
print(f.readline())
f.seek(17)

print(f.tell())
print(f.readline())
f.seek(35)

print(f.tell())
print(f.readline())
f.seek(17)

print(f.tell())
print(f.readline())

f.close()