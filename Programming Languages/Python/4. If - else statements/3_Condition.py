age = int(input("Please Enter Your Age: "))
if age > 18:
    if age > 100:
        print("Dadaji aapki jane ki umar ho gayi he!")
    else:
        print("Yes, You can drive!")
elif age < 18:
    if age < 1:
        print("Beta pahle peda to ho ja!")
    else:
        print("No! You cannot drive!")
else:
    print("You are just 18 years old and we can not decide that you can drive or not!")