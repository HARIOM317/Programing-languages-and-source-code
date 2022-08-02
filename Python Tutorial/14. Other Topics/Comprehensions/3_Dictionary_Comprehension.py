# Create a dictionary by using dictionary comprehension
Dict1 = {i : f"item {i} " for i in range(1, 6)}
print(Dict1)

# Create a dictionary by using dictionary comprehension with condition
Dict2 = {j : f"My_Item {j} " for j in range(1, 51) if j % 10 == 0}
print(Dict2)

# Interchange key with values
Dict3 = {value : key for key, value in Dict2.items()}
print(Dict3)