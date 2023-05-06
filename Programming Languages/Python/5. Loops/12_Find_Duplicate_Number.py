def find_duplicate(list1):
    duplicates, seen = set(), set()
    for element in list1:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    print("Elements are :  ", seen)
    print("Duplicate Elements are : ", duplicates)
    return list(duplicates)

My_List = [1, 3, 8, 1, 9, 4, 3, 2, 9, 1, 7, 5, 8, 2, 6]

find_duplicate(My_List)
