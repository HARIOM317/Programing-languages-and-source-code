num = 25

def func1():

    global num
    print("The value of global num is:", num)
    num = num+25    # Now we can change the value of global variable
    print("Now The value of global num is:", num)

func1()
print(num)
