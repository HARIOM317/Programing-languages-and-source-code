import re

s = "Welcome to Anandipura!"
res = re.search(r"\bA", s)

print(res)
print(res.re)
print(res.string)

res = re.search(r"\D{7} A", s)
print(res.group())

s2 = "My name is hariom"
search = re.search(r"\bhari", s2)

print()
print(search.start())
print(search.end())
print(search.span())
