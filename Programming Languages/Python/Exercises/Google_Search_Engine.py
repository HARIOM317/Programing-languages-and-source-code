from googlesearch import search

keyword = input("Search :  ")
result = search(keyword, 10)     # Show 10 results

for i in result:
    print(i)
