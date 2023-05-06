#Slicing in string

mystr = "Hariom is a good boy"
print(mystr)
print("Lenght of mystr is: ", len(mystr))
print(mystr[0])
print(mystr[1])
print(mystr[2])
print(mystr[3])
print(mystr[4])
print(mystr[5])
print(mystr[-1])    #Print last character
print(mystr[12:21]) #Printing 12 to 20 characters
print(mystr[0:21:2]) #Print 1 char and skip second char from 0 to 20 characters
print(mystr[0:])    #Print 0 t0 full string
print(mystr[:6])    #Print 0 to 6 characters of string
print(mystr[::])    #Print full string mystr[0:21:1]
print(mystr[0:21:1])    #Print full string mystr[0:21:1]
print(mystr[::1])    #Print full string mystr[0:21:1]
print(mystr[:10:3])    #Print 0 t0 10 and skip 2 charcters sequence
print(mystr[-20:-1])    #Print full string mystr[-20 to -1]
print(mystr[::-1])    #Reverse the string
print(mystr[::-2])    #Reverse the string and skip 1 character sequence