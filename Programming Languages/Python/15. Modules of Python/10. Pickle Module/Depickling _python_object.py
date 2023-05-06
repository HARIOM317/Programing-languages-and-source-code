import pickle
file = "Mycars.pkl"
file_obj = open(file, 'rb')
mycar = pickle.load(file_obj)
print(mycar)
file_obj.close()
