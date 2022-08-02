# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def square(x):
    return x*x

def cube(x):
    return x*x*x

func = [square, cube]

for i in range(1, 11):
    val = list(map(lambda x:x(i), func))
    print(val)
