import requests
json_data = {'username': 'Hariom', 'password': '1234'}
r = requests.post('https://httpbin.org/post', data=json_data)
# convert JSON to Python Dictionary
print(r.json())
# Storing in a variable
r_dictionary = r.json()
print(r_dictionary['form'])
