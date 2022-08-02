list1 = ["Mango", "Apple", "Banana", "Pineapple", "Papaya", "Orange", "Plum", "Guava", "Grapes"]

# With break statement
for i in list1:
    print(i)
else:
    print("The for loop ended successfully!\n")     # This will run

# Without break statement
for j in list1:
    print(j)
    break
else:
    print("The for loop ended successfully!\n")     # This will not run because of break statement
