import pickle

# Pickling a python object
cars = ['Audi', 'Ferrari', 'BMW', 'Maruti Suzuki', 'Lamborghini', 'Mahindra', 'Tata']
file = "Mycars.pkl"
fileobj = open(file, 'wb')  # Note: pickle file will be write only in binary mode
pickle.dump(cars, fileobj)
fileobj.close()