try:
    dict1 = {"Name": "Hariom", "Age": 19, "Skill": ['c', 'c++', 'python', 'batch scripting', 'powershell scripting']}
    name = input("Enter your name : ")

    for i in name:
        if i == '\t':
            raise TabError("Tab is not allowed")

    print(f"Well come {name}")

    info = input("Enter a key: ")

    if info not in dict1:
        raise KeyError("Key is not available in the dictionary")
    else:
        print(info, " = ", dict1[info])

except TabError as e:
    print(e)

except KeyError as e:
    print(e)
