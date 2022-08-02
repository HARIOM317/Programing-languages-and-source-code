import json

# JSON data:
x = '{ "organization":"SISTech", "city": "Bhopal","country": "India"}'

# python object to be appended
y = {"pin": 110096}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))