list1 = [12, 34, 98, 65, 3, 1, 2, 54, 9, 0, 87, 465, 45, 3, 2, 4, 75, 23, 45, 56, 78, 90, 100, 65, 24, 14]
odd_number = list(filter(lambda x: (x%2 != 0), list1))
even_number = list(filter(lambda x: (x%2 == 0), list1))
print("Odd numbers present in list1: ", odd_number)
print("Even numbers present in list1: ", even_number)
