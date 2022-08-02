state = ['Gujarat', 'Maharashtra', 'Rajasthan', 'Madhya Pradesh']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur', 'Bhopal']

dict_using_comp = {key: value for (key, value) in zip(state, capital)}

print("Output Dictionary using dictionary comprehensions:",
      dict_using_comp)
print(type(dict_using_comp))