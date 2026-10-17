import string
import secrets
import getpass

def passwordgenerator(long):
    password_type = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for p in range(long):
        password = password + secrets.choice(password_type)
    return(password)


def check_password(password):
    common_pass = ["Password", "12345", "Admin", "letmein", "qwerty"]
    if password.lower() in common_pass:
        return "Weak 🔴", ["This is a very common password"]
    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_number=True
        elif char in string.punctuation:
            has_symbol=True

    score = 0
    if len(password)>= 8:
        score = score + 1
    if len(password)>= 12:
        score=score + 1
    if has_upper:
        score = score + 1
    if has_lower:
        score = score + 1
    if has_symbol:
        score = score + 1
    if has_number:
        score = score + 1

    if score <= 2:
        rating = "Weak 🔴"
    elif score <= 4:
        rating = "Medium 🟡"
    else:
        rating = "Strong 🟢"

    extra = []
    if not has_number:
        extra.append("Add a number")
    if not has_lower:
        extra.append("Add a small letter")
    if not has_upper:
        extra.append("Add a capital letter")
    if not has_symbol:
        extra.append("Add a symbol e.g %")
    return rating, extra

def get_long():
    while True:
        try:
            long = int(input("How long should your password be?"))
        except ValueError:
            print("Your password should be a number e.g 5")
            continue
        if long < 8:
            print("Your password is too short")
        elif long > 10:
            print("Your password is above maximum")
        else:
            return(long)

def menu():
    print("\n---Password Tool---")
    print("1. Generate a password")
    print("2. Check your password")
    print("3. Quit")


while True:
    menu()
    choose = input("Choose a section: ")
    if choose == "1":
        long = get_long()
        print("Your password is ",passwordgenerator(long))
    elif choose == "2":
        test = getpass.getpass("Type in your password: ")
        rating, extra = check_password(test)
        print("Strength: ", rating)
        for t in extra:
            print("-", t)
    elif choose == "3":
        print("Goodbye!")
        break
    else:
        print("Choose your category. Thank you.")