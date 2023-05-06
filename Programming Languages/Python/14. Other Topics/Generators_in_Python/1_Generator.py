def gen(n):
    for i in range(n):
        yield i

g = gen(100000000000000000000)
print(g)

name = "Hariom"
iter_name = iter(name)
print(iter_name.__next__())
print(iter_name.__next__())
print(iter_name.__next__())
print(iter_name.__next__())
print(iter_name.__next__())
print(iter_name.__next__())
print(iter_name.__next__())