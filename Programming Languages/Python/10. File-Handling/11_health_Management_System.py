def gettime():
    import datetime
    return datetime.datetime.now()

def take(n):
    if n==1:
        m = int(input("Enter 1 for Exercises and 2 for died: "))

        if m == 1:
            value = input("Type here! \n")
            with open("Hariom_Exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully writen...")

        elif m == 2:
            value = input("Type here! \n")
            with open("Hariom_died.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully writen...")

    elif n == 2:
        m = int(input("Enter 1 for Exercises and 2 for died: "))

        if m == 1:
            value = input("Type here! \n")
            with open("Abhishek_Exersize.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully writen...")

        elif m == 2:
            value = input("Type here! \n")
            with open("Abhishek_Died.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully writen...")

    elif n == 3:
        m = int(input("Enter 1 for Exercises and 2 for died: "))

        if m == 1:
            value = input("Type here! \n")
            with open("Anand_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully writen...")

        elif m == 2:
            value = input("Type here! \n")
            with open("Anand_Died.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully writen...")

    else:
        print("Please enter a valid input: 1(Hariom), 2(Abhishek), 3(Anand)")

def retrieve(n):
    if n == 1:
        m = int(input("Enter 1 for Exercises and 2 for Died: "))
        if m == 1:
            with open("Hariom_Exercise.txt") as op:
                for i in op:
                    print(i, end="")

        elif m == 2:
            with open("Hariom_died.txt") as op:
                for i in op:
                    print(i, end="")
    elif n == 2:
        m = int(input("Enter 1 for Exercises and 2 for Died: "))
        if m == 1:
            with open("Abhishek_Exersize.txt") as op:
                for i in op:
                    print(i, end="")

        elif m == 2:
            with open("Abhishek_Died.txt") as op:
                for i in op:
                    print(i, end="")

    elif n == 3:
        m = int(input("Enter 1 for Exercises and 2 for Died: "))
        if m == 1:
            with open("Anand_exercise.txt") as op:
                for i in op:
                    print(i, end="")

        elif m == 2:
            with open("Anand_Died.txt") as op:
                for i in op:
                    print(i, end="")

    else:
        print("Please enter a valid input: 1(Hariom), 2(Abhishek), 3(Anand)")

print("Wellcome to the Health Management System")
a = int(input("Press 1 for log the data and 2 for retrieve the data: "))

if a == 1:
    b = int(input("Press 1 for Hariom, 2 for Abhishek, and 3 for Anand: "))
    take(b)
else:
    b = int(input("Press 1 for Hariom, 2 for Abhishek, and 3 for Anand: "))
    retrieve(b)
