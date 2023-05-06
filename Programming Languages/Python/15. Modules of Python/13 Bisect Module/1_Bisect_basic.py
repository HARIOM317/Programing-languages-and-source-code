import bisect
a = [1, 2, 3, 6, 7, 9, 10, 34, 56, 88]
print(a)

new_element = 27
# it will return the index number where our new element will be insert yet list will also be sorted
# Note :- List should be sorted in ascending order for bisect.bisect() method.
print("The new element is: ", new_element)
print("For keeping sorted list a, the index will be for new element: ", bisect.bisect(a, new_element))
bisect.insort(a, new_element)    # It will insert new element at it's correct position for keeping sorted our list
print(a)

