a = [[3, 4], [6, 9], [2, 1], [11, 32], [98, 76], [54, 23]]
a.sort(key=lambda x: x[1])  # this lambda function will sort x[1] index values not x[0]
print(a)
