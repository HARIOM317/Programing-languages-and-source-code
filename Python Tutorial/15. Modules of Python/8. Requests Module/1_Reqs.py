import requests
r = requests.get("https://www.hackerrank.com/domains/data-structures?filters%5Bdifficulty%5D%5B%5D=easy")
print("r = ", r)
print("Status Code is: ", r.status_code)
print("Encoding = ", r.encoding)      # returns 'utf-8'
print("Elapsed = ", r.elapsed)       # returns datetime.timedelta(0, 1, 666890)
print("Url = ", r.url)      # returns given URL
print("History = ", r.history)
print("Content = ", r.content)
print("Cookies = ", r.cookies)
print("Headers = ", r.headers['Content-Type'])
print("Text = ", r.text)
