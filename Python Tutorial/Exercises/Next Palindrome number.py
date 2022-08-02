def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n
def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    n = int(input("Enter number of test cases: "))
    numbers = []
    for i in range(n):
        number = int(input(f"Enter number {i+1}: "))
        numbers.append(number)
    for i in range(n):
        print(f"Next palindrome of {numbers[i]} is: {next_palindrome(numbers[i])}")