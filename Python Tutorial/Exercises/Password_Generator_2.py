import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,.-_#@$%<>^?&!~"

if __name__ == '__main__':
    all = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(all, length))
    print("Your Strong Password is:  ", password)