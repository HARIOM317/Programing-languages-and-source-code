def is_anagrams(s1, s2):
    return set(s1) == set(s2)

print(is_anagrams("elvis", "lives"))
print(is_anagrams("odd", "dod"))
print(is_anagrams("hariom", "omhira"))
print(is_anagrams("good", "god"))
print(is_anagrams("god", "good"))
print(is_anagrams("hello", "Hello"))

