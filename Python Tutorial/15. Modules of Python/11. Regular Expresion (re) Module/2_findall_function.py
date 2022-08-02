import re

string = """Hello my Number is 1234567898, 9869234560 and
            my friend's number is 9876543921 and my teacher's number is 9870543670"""

regex = '\d+'

match = re.findall(regex, string)
print(match)
