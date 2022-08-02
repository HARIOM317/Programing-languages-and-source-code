# Prints today's date with help
# of datetime library
import datetime

today = datetime.datetime.today()
print(f"{today:%d %B, %Y}")