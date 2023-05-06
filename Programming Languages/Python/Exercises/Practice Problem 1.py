print("Enter the numbers of the list one by one \n")
size = int(input("Enter size of the list :  "))
print()
myList = []
for i in range(size):
    myList.append(int(input(f"Enter element {i+1} :  ")))
print(f"\nyour list is : {myList} \n")

reverse1 = myList[:]    # Store copy of myList
reverse1.reverse()     # Reverse list by using inbuilt function reverse()
print(f"My first reveres list is :  {reverse1}")

reverse2 = myList[::-1]     # Reverse list by using inbuilt list slicing
print(f"My second reveres list is :  {reverse2}")

reverse3 = myList[:]    # Reverse list by using swapping
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1], reverse3[i]
print(f"My third reveres list is :  {reverse3}")

if reverse1 == reverse2 == reverse3:
    print("\nAll three method gives same result.")
else:
    print("\nAll three method not gives same result.")


