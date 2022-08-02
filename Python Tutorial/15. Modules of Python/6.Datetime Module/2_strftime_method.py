import datetime
current = datetime.datetime.now()
year = current.strftime("%Y")
print("Current Month name short version: ", current.strftime("%b"))
print("Current Month name full version: ", current.strftime("%B"))
print("Current Month as a number: ", current.strftime("%m"))
print("Current Year name short version: ", current.strftime("%y"))
print("Current Year name full version: ", current.strftime("%Y"))
print("Current Hour [in 24 hour format]: ", current.strftime("%H"))
print("Current Hour [in 12 hour format]: ", current.strftime("%I"))
print("Current Minutes: ", current.strftime("%M"))
print("AM or PM: ", current.strftime("%p"))