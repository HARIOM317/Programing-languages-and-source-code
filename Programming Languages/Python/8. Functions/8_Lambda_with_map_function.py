# List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# power = list(map(lambda x: x*x, List))
# print("Squares are: ", power)

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print("a/b = %d"%c)
    # Using exception object with the except statement
except Exception as e:
    print("We can not divide this value by zero")
    print(e)
else:
    print("Hi I am else block")