import json

# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside Emp_Details
        file_data["Emp_Details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

# python object to be appended

y = {"Emp_name": "Nikhil",
     "Email": "nikhil@gmail.com",
     "Job profile": "Full Time"
     }

write_json(y)
