def searcher():
    import time
    # Assume that this is a 4 seconds time consuming task
    book = "This is a book about python, and you can get all knowledge of python from basic to very advance."
    time.sleep(4)
    print("This is a python book description")

    while True:     # On next call search will start from here
        text = (yield)
        if text in book:
            print("This text is available in the book!")
        else:
            print("This text is not available in the book!")

search = searcher()
next(search)
search.send("knowledge")
input("Press any key: ")
search.send("basic to very advance")
search.close()
input("Press any key: ")
search.send("This is a book")
