class BikeShop:
    def __init__(self, stoke):
        self.stoke = stoke

    def displayBikes(self):
        print("Total bikes available: ", self.stoke)

    def rentForBike(self, q):
        if q <= 0:
            print("Enter a positive value or greater than 0")
        elif q > self.stoke:
            print(f"No {q} stocks available. Please enter the value (less than stocks).")
            print(f"Bikes available: {self.stoke}")
        else:
            self.stoke = self.stoke - q
            print("Total price: ", q * 100)      # Rs. 100 per quantity
            print("Now Total available bikes: ", self.stoke)

while True:
    obj = BikeShop(100)

    user_choice = int(input('''
    1. Display Stocks
    2. Rent a bike
    3. Exit
    '''))

    if user_choice == 1:
        obj.displayBikes()
    elif user_choice == 2:
        n = int(input("Enter Quantity -->  "))
        obj.rentForBike(n)
    elif user_choice == 3:
        exit()
    else:
        print("Invalid Input...")
