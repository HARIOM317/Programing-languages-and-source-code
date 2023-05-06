from getpass import getpass

Email = "hariommewada000@gmail.com"
Pass = "Hsr$123"

# Note:- getpass() method will not work properly on pycharm console, that's why run this program on CMD.
Email_address = input("Enter Email :  ")
Password = getpass("Enter Password :  ")

if Email_address == Email and Password == Pass:
    print("Login Successfully!")
else:
    print("Invalid Email or password!")
