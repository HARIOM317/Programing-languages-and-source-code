courses = {
    "C++": {"Duration": "2 Months", "Fees": 2000, "Type": "Beginner friendly"},
    "Java":  {"Duration": "3 Months", "Fees": 3000, "Type": "Advanced"},
    "Python":  {"Duration": "3 Months", "Fees": 5000, "Type": "Beginner friendly"},
    "PHP":  {"Duration": "2 Months", "Fees": 2000, "Type": "Beginner friendly"},
    "Java Script":  {"Duration": "2 Months", "Fees": 5000, "Type": "Beginner friendly"},
    "Django":  {"Duration": "3 Months", "Fees": 4500, "Type": "Very Advanced"}
}
print("Python Course: ", courses["Python"])
print("Java Course fees: ", courses["Java"]["Fees"])
print("Django Course Type: ", courses["Django"]["Type"])

courses["Java"]["Fees"] = 3500
print("\n")
for i, j in courses.items():
    print(i, j["Duration"], j["Fees"], j["Type"])
