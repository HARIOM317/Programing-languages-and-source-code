print("Reading file by using with block\n")
with open("Hsr.txt") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
# There is no need to close the file

print("\nReading another file\n")
with open("Hariom2.txt") as F:
    data = F.read()
    print(data)