# Creating Queue using list
list1 = []

while True:
    choice = int(input('''
    _______________Choose any option for continue_________________

    1. Enqueue Element
    2. Dequeue Element
    3. Get Front Element
    4. Get Rear Element
    5. Display Queue
    6. Exit

    '''))

    if choice == 1:
        new_Element = int(input("\nEnter new element:   "))
        list1.append(new_Element)
        print("Your Queue is:  ", list1)

    elif choice == 2:
        if len(list1) == 0:
            print("Queue is Empty!")
        else:
            print("Dequeueing element is:  ", list1[0])
            del list1[0]
            print("Now your Queue is:  ", list1)

    elif choice == 3:
        if len(list1) == 0:
            print("Queue is Empty!")
        else:
            print("Front element of Queue is:  ", list1[0])

    elif choice == 4:
        if len(list1) == 0:
            print("Queue is Empty!")
        else:
            print("Last element of Queue is:  ", list1[-1])

    elif choice == 5:
        print("Displaying Queue:  ", list1)

    elif choice == 6:
        break

    else:
        print("Invalid Input!")
