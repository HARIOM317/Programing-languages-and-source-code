l1 = ["Bhindi", "Gajar", 'Muli', "Dhaniya", "Aalu", "Gobi", "Matar", "Palak", "Tamater"]

for index, Item in enumerate(l1):
    if index % 2 == 0:
        print(f"Buy: {Item}")

# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)
print()
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)