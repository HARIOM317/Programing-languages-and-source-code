import json

# Data to be written
dictionary = {
    "Name": "Hariom",
    "Roll no.": 56,
    "cgpa": 8.6,
    "Phone number": "9756770500"
}

with open("sample.json", "w") as f:
    json.dump(dictionary, f)
