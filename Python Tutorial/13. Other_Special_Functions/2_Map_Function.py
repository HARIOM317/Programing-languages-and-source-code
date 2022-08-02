numbers = ["43", "98", "26", "98", "13", "6", "3", "76", "58"]
print("Given list is: ", numbers)
numbers = list(map(int, numbers))
numbers[3] = numbers[3] + 2
print("Now Value of numbers[3] is: ", numbers[3])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
square = list(map(lambda x: x*x, lst))
print("Squares are: ", square)

cube = list(map(lambda x: x*x*x, lst))
print("Cubes are: ", cube)

