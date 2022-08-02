def dec1(func1):
    def Now_Execute():
        print("Executing Now")
        func1()
        print("Executed")
    return Now_Execute

def name_1():
    print("My name is Hariom Mewada")

name_1 = dec1(name_1)
name_1()

print("\nThis is another way to use decorator in python")
@dec1
def name_2():
    print("I am also HSR")

name_2()
