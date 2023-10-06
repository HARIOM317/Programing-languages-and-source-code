D1 = {"Pen": "Kalam", "Book": "Kitab", "Fruit": "Phal", "Flower": "Phool", "Color": "Rang"}
D2 = input("Please Enter a key of Dictionary: ")

try:
    print(D1[D2])
except(Exception):
    print("Key does not exist")

