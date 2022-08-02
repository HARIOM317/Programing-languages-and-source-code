with open("Currency_details.txt") as f:
    lines = f.readlines()

currency_Dict = {}
for line in lines:
    parsed = line.split("\t")
    currency_Dict[parsed[0]] = parsed[1]

# print(currency_Dict)
Amount = int(input("Enter amount: "))
print(f'''Enter the name of currency you want to convert this amount to?
Available Options:
''')
[print(item) for item in currency_Dict.keys()]

Currency = input("Please Enter one fo these values:  ")
print(f"{Amount} INR = {float(currency_Dict[Currency]) * Amount} {Currency}")
