sum = 0
while True:
    UserInput = input("Enter Item price or 'q' for quit:  ")
    if UserInput != 'q':
        sum = sum + int(UserInput)
        print(f"Order Total so far: {sum}")
    else:
        print()
        print(f"Total: {sum}")
        print("Thanks for coming on our shop")
