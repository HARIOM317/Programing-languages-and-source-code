import random
import string

if __name__ == '__main__':
    try:
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        pass_length = int(input("Enter password length:  "))
        s = []
        # extend() method inserts elements of list s1, s2, s3, and s4 in list s yet append() method inserts list not list elements.
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print(s)
        random.shuffle(s)
        print("Your password is: ", "".join(s[0:pass_length]))

    except Exception as e:
        print("Something went Wrong!")
