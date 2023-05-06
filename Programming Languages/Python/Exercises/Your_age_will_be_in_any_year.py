User_Age = int(input("What is your Age/Year of birth? "))

isAge = False
isYear = False

if len(str(User_Age)) == 4:
    isYear = True

else:
    isAge = True

if (User_Age < 1900 and isYear):
    print("You seem to be the oldest person alive.")
    exit()

if User_Age > 2022:
    print("You are not yet born.")
    exit()

if isAge:
    User_Age = 2022 - User_Age

print(f"You will be 100 year old in {User_Age + 100}")

intrestedYear = int(input("Enter the year you want to know your age in:   "))
print(f"You will be {intrestedYear - User_Age} year old in {intrestedYear}")
