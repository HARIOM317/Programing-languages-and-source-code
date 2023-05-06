import datetime
from datetime import date

# Print current time
print("Your current time is: ", datetime.datetime.now())

# date object of today's date
today = date.today()

print("\nCurrent year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
