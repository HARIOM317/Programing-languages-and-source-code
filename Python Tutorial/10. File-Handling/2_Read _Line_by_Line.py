read1 = open("Hsr.txt")  # by default open in "r" (read) mode
print("Reading file line by line by using for loop:")
for line in read1:
    print(line)

read1.close()

read2 = open("Hsr.txt", "r")
print("\nReading file line by line by using readline function:")
print(read2.readline())
print(read2.readline())

read2.close()
