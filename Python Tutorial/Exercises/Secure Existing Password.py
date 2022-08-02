SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('O', '0'), ('i', '1'), ('I', '|'), ('o', '*'))

def securePassword(password):
    for a, b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == '__main__':
    password = input("Enter your Password:  ")
    password = securePassword(password)
    print(f"Your secure password is:  {password}")

