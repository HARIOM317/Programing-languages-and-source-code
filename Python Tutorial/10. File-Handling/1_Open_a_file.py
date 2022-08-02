f = open("Hsr.txt", "r")

print("\n Reading in text mode:")
content = f.read(5)  # it will read 5 characters from starting of a file
print(content)
content = f.read(5)  # it will read next 5 characters from a file
print(content)

content = f.read()  # it will read all content from file
print(content)

f.close()

print("\n Reading in binary mode:")
read2 = open("Hsr.txt", "rb")
content = read2.read()
print(content)

read2.close()