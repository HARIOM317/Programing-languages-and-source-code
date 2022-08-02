import json

# JSON string
a = '{"name": "Hariom", "languages": "Hindi"}'

# deserializes into dict and returns dict.
y = json.loads(a)

print("JSON string = ", y)
print()

# JSON file
f = open('data.json', "r")

# Reading from file
data = json.loads(f.read())

# Iterating through the json list
for i in data['Emp_Details']:
    print(i)

# Closing file
f.close()