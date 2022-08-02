import json

# Opening JSON file
f = open('data.json')

# returns JSON object as a dictionary
data = json.load(f)
print(type(data))

# Iterating through the json list
for i in data['Emp_Details']:
    print(i)

# Closing file
f.close()