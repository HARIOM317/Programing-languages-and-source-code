MtoM = 1
Mtomm = 1000
Mtocm = 100
Mtodm = 10
Mtokm = 0.001
Mtomicrom = 1000000

User_Choice1 = int(input('''
Select first digit:
0. M
1. mm
2. cm
3. dm
4. km
5. micrometer
'''))

User_Choice2 = int(input('''
Select second digit:
0. M
1. mm
2. cm
3. dm
4. km
5. micrometer
'''))

Unit1 = None
Unit2 = None
if User_Choice1 == 0:
    User_Choice1 = MtoM
    Unit1 = "Meter"
elif User_Choice1 == 1:
    User_Choice1 = Mtomm
    Unit1 = "Millimeter"
elif User_Choice1 == 2:
    User_Choice1 = Mtocm
    Unit1 = "Centimeter"
elif User_Choice1 == 3:
    User_Choice1 = Mtodm
    Unit1 = "Decimeter"
elif User_Choice1 == 4:
    User_Choice1 = Mtokm
    Unit1 = "Kilometer"
elif User_Choice1 == 5:
    User_Choice1 = Mtomicrom
    Unit1 = "Micrometer"

if User_Choice2 == 0:
    User_Choice2 = MtoM
    Unit2 = "Meter"
elif User_Choice2 == 1:
    User_Choice2 = Mtomm
    Unit2 = "Millimeter"
elif User_Choice2 == 2:
    User_Choice2 = Mtocm
    Unit2 = "Centimeter"
elif User_Choice2 == 3:
    User_Choice2 = Mtodm
    Unit2 = "Decimeter"
elif User_Choice2 == 4:
    User_Choice2 = Mtokm
    Unit2 = "Kilometer"
elif User_Choice2 == 5:
    User_Choice2 = Mtomicrom
    Unit2 = "Micrometer"

value = int(input("Enter Value: "))

print(f"{value} {Unit1} = {(User_Choice2/User_Choice1)*value} {Unit2}")

