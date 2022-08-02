D1 = {
    'Name' : 'Hariom Rajput',
    'Gender' : 'Mail',
    'DOB' : '6 july 2004',
    'Qualification' : 'B.Tech',
    'Job' : 'Software Engineer',
    'Salary' : 10000000
}

a1 = D1["DOB"]
print("DOB is: ", a1)

a2 = D1.get("Name")
print("Name is: ", a2)

print("\nKeys of Dictionary.........")
for x in D1.keys():
    print(x)

print("\nValues of Dictionary.........")
for x in D1.values():
    print(x)

print("\nItems of Dictionary.........")
for x in D1.items():
    print(x)

del D1["Gender"]
D1.pop('DOB')
print("\nNow Dictionary is: ", D1)

D2 = dict(Name = "Python", Fees = 10000, Duration = "6 Months")
print("\nNew Dictionary is: ", D2)
D2.update({"Fees":5000})
D2.update({"Duration":"3 Months"})
print("Updated Dictionary is: ", D2)

D1.clear()
print("\nAfter clearing, Dictionary 1 is: ", D1)

D2["Description"] = "This is Python Tutorial for absolute beginner!"
D2["Name"] = "Python Tutorial"

print("\nNow Dictionary 2 is: ", D2)
