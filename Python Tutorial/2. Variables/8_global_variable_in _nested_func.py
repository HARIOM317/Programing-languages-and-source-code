def func1():
    x = 20
    def func2():
        global x    # this will make a global variable x with value 50
        x = 50
    print("Before calling func2 x =", x)
    func2()
    print("After calling func2 x =", x)

func1()
print("value of global variable is:", x)

