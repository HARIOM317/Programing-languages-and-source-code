str1 = "hello good morning.  well come back"
space = str1.find("  ")
str1 = str1.replace("  ", " ")  # Replace double spaces with a single space
print("Double space found at: ", space)
print(str1)