# LIST = [["Hariom", 8], ["Abhi", 7] , ["Sonu", 2] , ["kali", 9] , ["Ajay", 25]]
# for item, laddu in LIST:
#     print(item," eat ", laddu ," laddu daily")

list1 = ["Hariom", "Raju", "Mona", "Lallu", 2, 5, 9, 7, 3, 6, 23, 98, 65, 12, 43, 2]
list2 = list1
for item in list1:
    if str(item).isnumeric() and item > 10:
        print(item)
