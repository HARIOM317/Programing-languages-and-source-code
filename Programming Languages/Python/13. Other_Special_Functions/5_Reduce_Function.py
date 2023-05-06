from functools import reduce
list1 = [1, 2, 3, 4, 5]

# Iterative way
num = 0
for i in list1:
    num = num + i
print(num)

# By using reduce function
total_sum = reduce(lambda x, y: x+y, list1)
print("Total sum of list is: ", total_sum)

total_product = reduce(lambda x, y: x*y, list1)
print("Total product of list is: ", total_product)