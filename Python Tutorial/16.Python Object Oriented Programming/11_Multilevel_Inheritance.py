class Grand_parants:
    def Job(self):
        print("I am a doctor")

class Parants(Grand_parants):
    def Skill(self):
        print("I am a cricket player but also a freelancer!")

class Son(Parants):
    def Study(self):
        print("I am doing M.tech")

class Child(Son):
    print("Me to abhi bachcha hu ji!")

Sonu = Child()
Sonu.Study()
Sonu.Skill()
Sonu.Job()
