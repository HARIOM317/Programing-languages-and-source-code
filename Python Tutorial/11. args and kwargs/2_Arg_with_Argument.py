def arg_function(first_line, *Item):
    print(line)
    for items in Item:
        print(items)

Item = ["Hariom", "Abhishek", "Rohan", "Ravi", "Veer", "Raj"]
# arg_function(*Item)

line = "This is the list of selected candidates in Google"
arg_function(line, *Item)
