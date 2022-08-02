class Person:
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    def takeBreath(self):
        super().takeBreath()
        print("I am luckily taking the breath!")

class Programmer(Employee):
    def takeBreath(self):
        super().takeBreath()
        print("I am breathing nicely...")


programmer = Programmer()
programmer.takeBreath()
