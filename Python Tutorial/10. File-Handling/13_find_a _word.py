content = True
i = 1
with open("Hariom.txt") as f:
    while content:
        content = f.readline()

        if 'hariom' in content.lower():
            print(f"Hariom is present in line number: {i}")
            print(content)

        i = i + 1

