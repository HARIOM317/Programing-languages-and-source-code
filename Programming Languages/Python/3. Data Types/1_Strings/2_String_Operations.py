str1 = "hariom is a good boy"
str2 = "Hariomisagoodboy"

#Return true if str1 is a alfanumeric else return false
print(str1.isalnum())       #Return false because there are spaces in string
print(str2.isalnum())       #Return true because there are no spaces in string

print(str1.endswith("boy"))     #Return true because given string is ending from boy
print(str1.count("i"))      #Count that how many i are presents in given string
print(str1.capitalize())    #Capitalize first character of given string
print(str1.find("is"))    #Find given values/string and return its index
print(str1.upper())     #Change all characters in uppercase of given string
print(str2.lower())     #Change all characters in lowercase of given string
print(str1.replace("hariom", "Hariom Singh Rajput"))    #Replace a string to another