# Creating Stack using list
list1 = []

while True:
    choice = int(input('''
    _______________Choose any option for continue_________________
    
    1. Push Element
    2. Pop Element
    3. Peek Element
    4. Display Stack
    5. Exit
    
    '''))

    if choice == 1:
        new_Element = int(input("\nEnter new element:   "))
        list1.append(new_Element)
        print("Your Stack is:  ", list1)

    elif choice == 2:
        if len(list1) == 0:
            print("Stack is Empty!")
        else:
            popped_element = list1.pop()
            print("Popped element is:  ", popped_element)
            print("Now your Stack is:  ", list1)

    elif choice == 3:
        if len(list1) == 0:
            print("Stack is Empty!")
        else:
            print("Last element of stack is:  ", list1[-1])

    elif choice == 4:
        print("Displaying Stack :   ", list1)

    elif choice == 5:
        break

    else:
        print("Invalid Input! ")

