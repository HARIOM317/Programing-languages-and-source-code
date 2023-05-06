def Arrow(n):
    for i in range(n):
        if i == n - 1:
            print("\033[93;1m", (2 * n) * "*", end="")
            print("\033[91;1m", (i + 1)*"*")
        else:
            print((2 * n) * " ", end="")
            print("\033[96;1m", (i + 1) * "*")

    for j in range(n - 1, 0, -1):
        print((2 * n) * " ", end="")
        print("\033[96;1m", j * "*")

number = int(input("Enter a number:  "))
Arrow(number)
