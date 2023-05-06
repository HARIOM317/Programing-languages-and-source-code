'''
What is Armstrong Number?
1249 = 1^4 + 2^4 + 4^4 + 9^4 --> order = 4
87 = 8^2 + 7^2 --> order = 2
98705 = 9^5 + 8^5 + 7^5 + 0^5 + 5^5 --> order = 5

Hence 153 is a armstrong number, because:
153 = 1^3 + 5^3 + 3^3
153 = 1+125+27
153 = 153
'''

number = int(input("Enter a number :  "))
sum = 0
order = len(str(number))
number_copy = number
while number > 0:
    digit = number % 10
    sum += digit ** order
    number = number//10
if sum == number_copy:
    print(f"{number_copy} is an Armstrong number.")
else:
    print(f"{number_copy} is not an Armstrong number.")
