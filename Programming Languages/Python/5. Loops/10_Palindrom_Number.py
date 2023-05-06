number = int(input("Enter a number:  "))
temp = number
reverse = 0
while(number > 0):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number is:  ", reverse)

if temp == reverse:
    print("\nHence Number is a palindrome number.")
else:
    print("\nHence Number is not a palindrome number.")

