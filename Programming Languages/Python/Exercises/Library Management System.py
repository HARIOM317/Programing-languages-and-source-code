class Library:
    def __init__(self, list, name):
        self.books_list = list
        self.name = name
        self.lendDict = {}

    def displaybook(self):
        print(f"\033[93;1m__________The following books are available in our library: {self.name}__________")
        for book in self.books_list:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("\033[97;1mLender-book database has been updated. You can take the book now.")
        else:
            print(f"\033[91;1mBook is already being used by {self.lendDict[book]}")

    def addbook(self, book):
        self.books_list.append(book)
        print("\033[93;1mBook has been added to the book list.")

    def returnbook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    Library1 = Library(['Python Advance', 'C++ Basics', 'The big bang', 'World war 2', 'Hasi ka pitara', 'NCERT Math',
                         'Chand ke par chalo', 'Motu Patlu', 'The Super Hero'], "The Royal King")

    while True:
        print(f"\033[96;1m \nWell Come to the {Library1.name} Library.")
        print('''\033[97;1m
                         1. Display Books
                         2. Lend a book
                         3. Add a book
                         4. Return a book 
         ''')
        User_Choice = input("Enter your choice to continue... -->   ")
        if User_Choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            User_Choice = int(User_Choice)

        if User_Choice == 1:
            Library1.displaybook()

        elif User_Choice == 2:
            user = input("Enter your name:    ")
            book = input("Enter the name of the book you want to lend:    ")
            Library1.lendbook(user, book)

        elif User_Choice == 3:
            book = input("Enter thr name of the book you want to add:    ")
            Library1.addbook(book)

        elif User_Choice == 4:
            book = input("Enter the name of the book you want to return:   ")
            Library1.returnbook(book)

        else:
            print("\033[92;1mNot a valid option")

        User_Choice2 = ""
        while(User_Choice2 != 'q' and User_Choice2 != 'c'):
            print("\033[33;1m \nPress q to quite and c to continue...")
            User_Choice2 = input()

            if User_Choice2 == 'q':
                exit()
            elif User_Choice2 == 'c':
                continue
