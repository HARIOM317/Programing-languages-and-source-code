def wish_morning(string):
    print(f"Hello! Good Morning {string}, How are you? ")
    print(f"Thanks {string} for looking the car. Have a nice day.")

class car:
    car_list = ['Audi', 'BMW', 'Nissan']

    def __init__(self):
        print("Well come to car show room.")

class Audi(car):
    def __init__(self):
        self.models = ['q7', 'a6', 'a8', 'a3']

    def outModels(self):
        print('These are the available models for Audi')
        for model in self.models:
            print('\t%s ' % model)


class Bmw(car):
    def __init__(self):
        self.models = ['i8', 'x1', 'x5', 'x6']

    def outModels(self):
        print('These are the available models for BMW')
        for model in self.models:
            print('\t%s ' % model)


class Nissan(car):
    def __init__(self):
        self.models = ['altima', '370z', 'cube', 'rogue']

    def outModels(self):
        print('These are the available models for Nissan')
        for model in self.models:
            print('\t%s ' % model)