import json

# Data to be written
dictionary = {
    "id": "04",
    "name": "Hariom",
    "department": "HR",
    "Employee": True,
    "Extra": None
}
print("Python Object: ", dictionary)
print("Type: ", type(dictionary), "\n")

# Serializing json
json_object = json.dumps(dictionary, indent=4)
print("Json Object: ", json_object)
print("Type: ", type(json_object))