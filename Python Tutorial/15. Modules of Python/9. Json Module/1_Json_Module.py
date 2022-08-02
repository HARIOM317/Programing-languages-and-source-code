import json
data = '{"var1": "Hariom", "var2": 98}'
print(type(data))
# print(data['var1'])       # This will throw an error

parsed = json.loads(data)
print(parsed['var1'])
print(type(parsed))

# This is only python compatible object
data2 = {
    "Name": "Hariom",
    "Cars": ['BMW', 'Odi a8', 'Ferrari'],
    "Languages": ('C++', 'C', 'Python'),
    "Isbad": False
}

# json.dumps returns javascript compatible object
jscomp = json.dumps(data2)
print(jscomp)
