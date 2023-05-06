with open("Hsr.txt") as f:
    content = f.read()

content = content.replace("donkey", "******")

with open("Hsr.txt", 'w') as f:
    f.write(content)
