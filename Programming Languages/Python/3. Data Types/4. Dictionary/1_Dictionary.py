D1 = {"Hariom":"Blue","Abhishek":"Red", "Pooja":"Pink", "Harish":"Green", "Sahil":"Orange"}
print(D1)
print("favorite color of Hariom is:", D1["Hariom"])
print("favorite color of Pooja is:" ,D1["Pooja"])
D1["Rahul"] = "Yellow"
D1["Nitin"] = "Black"
del D1["Sahil"]
print(D1,"\n")

D2 = {"Hariom":"Samosa",
      "Raj":{"Brake fast":"Breade", "Lunch":"Roti", "Dinner":"Halwa"},
      "Abhishek":"Kachori",
      "Pooja":"Jalebi",
      "Harish":"Hot dog", "Sahil":"Sigrate"}

print("Raj follow the Following schedule: ", D2["Raj"])
print("Raj will eat in lunch: ", D2["Raj"]["Lunch"])