D1 = {"Hariom":"Blue","Abhishek":"Red", "Pooja":"Pink", "Harish":"Green", "Sahil":"Orange"}
D2 = D1.copy()  # Copy D1 Dictionary in D2 as a reference by using D2 pointer
del D1["Abhishek"]  # Delete Abhishek key and it's value
print(D2)
print(D1)   # Abhishek has been deleted from Dictionary
print(D1.get("Hariom"))     # Return value of Hariom key
D1.update({"Nikhil":"Purple"})      # Update D1 Dictionary and add one more key "Nikhil"
D1.update({"Shyam":"White"})        # Update D1 Dictionary and add one more key "Shyam"
print("Now D1 Looks Like This: ", D1)
print("All Keys which are present in dictionary: ", D1.keys())  # Print all keys of dictionary
print("All Values which are present in dictionary: ", D1.values())  # print all values of dictionary
print("All Items which are present in dictionary: ", D1.items())  # print all Keys-values pairs of dictionary