def searcher():
    import time
    # Assume that this is a 4 seconds time consuming task
    time.sleep(4)

    with open("latter.txt", "r") as f:
        names = f.read()

    while True:     # On next call search will start from here
        Name = (yield)
        if Name in names:
            print(f"This Name is available in the latter!")
        else:
            print("This text is not available in the latter!")

if __name__ == '__main__':

    search = searcher()
    next(search)
    i = input("Enter name:  ")
    search.send(i)
    input("Press any key: ")

    i = input("Enter name:  ")
    search.send(i)
    input("Press any key: ")

    i = input("Enter name:  ")
    search.send(i)

    search.close()
