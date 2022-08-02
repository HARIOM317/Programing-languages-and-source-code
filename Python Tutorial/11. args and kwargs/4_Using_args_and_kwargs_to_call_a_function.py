def myFun(arg1, arg2, arg3):
    print("First Name: ", arg1)
    print("Middle Name: ", arg2)
    print("Last Name: ", arg3)

print("Using args:")
args = ("Hariom", "Singh", "Rajput")
myFun(*args)

print("\nUsing kwargs:")
kwargs = {"arg1":"Hariom", "arg2":"Singh", "arg3":"Rajput"}
myFun(**kwargs)