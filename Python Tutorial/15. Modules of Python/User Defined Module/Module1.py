# This is a user define module which name is Module1.py
def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

def diff(a, b):
    return a - b

def product(*args):
    prd = 1
    for i in args:
        prd = prd * i
    return prd

def div(a, b):
    return a / b
