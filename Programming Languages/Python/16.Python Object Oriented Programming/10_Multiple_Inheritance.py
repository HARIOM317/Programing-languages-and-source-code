class Student:      # Class 1
    def __init__(self, name, standard, roll_no, result):
        self.name = name
        self.std = standard
        self.Roll_no = roll_no
        self.result = result

    def Print_details(self):
        return f"Student name is {self.name}, Standard is {self.std}, Roll number is {self.Roll_no} and Result is {self.result}"

class Player:       # Class 2
    def __init__(self, Game, position):
        self.game = Game
        self.position = position

    def Print_details(self):
        return f"Student game is {self.game} and Position is {self.position}"

    def skill(self):
        return "I can also play other games!"

class Cool_Student(Student, Player):        # Inherit all properties of class 1 and class 2
    # def skill(self):
    #     language = "Python"
    #     return f"Language : {language}"
    pass


hariom = Cool_Student("hariom", "12th", 1005, 90)
print(hariom.Print_details())
hariom.game = "Cricket"
hariom.position = "State Champian"
print(hariom.game)
print(hariom.position)
print(hariom.skill())

