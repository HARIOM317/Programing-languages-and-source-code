m, _ = (23, 65)     # Skip 65 (It will work only if there are two elements in our tuple)
print(f"m = {m}")

a, *_ = (2, 44, 5, 6, 6, 66, 98, 64)
print(f"a = {a}")    # print only a = 2

x, *_, y = (12, 43, 76, 98, 75, 9, 22, 43)
print(f"x = {x} and y = {y}")   # Print x = 12 and y = 43


