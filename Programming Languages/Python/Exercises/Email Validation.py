email = input("Enter your email:  ")
j = 0
k = 0
l = 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count('@') == 1):
            if (email[-4] == '.') ^ (email[-3] == '.'):
                for i in email:
                    if i == i.isspace():
                        j = 1
                    elif i.isalpha():
                        if i == i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        l = 1

                if j == 1 or k == 1 or l == 1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")