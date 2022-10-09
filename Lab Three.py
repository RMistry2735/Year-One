#Question 1
name = input("What is your name? ")
if name == "":
    print("Hello, Stranger!")
else:
    print("Hello", name,". Good to meet you")
    
#Question 2
password = input("Please enter a password:")
password2 = input("Please enter the password again:")
if password == password2:
    print("Password set")
else:
    print("The 2 passwords were different")

#Question 3
password = input("Please enter a password:")
password2 = input("Please enter the password again:")
if password == password2 and 8 <= len(password) <= 12:
    print("Password set")
else:
    print("Password not accepted")
    
#Question 4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password = input("Please enter a password:")
password2 = input("Please enter the password again:")
if password == password2 and 8 <= len(password) <= 12 and password not in BAD_PASSWORDS:
    print("Password set")
else:
    print("Password not accepted")

#Question 5
def SetPassword():
    password = input("Please enter a password:")
    password2 = input("Please enter the password again:")
    if password == password2 and 8 <= len(password) <= 12 and password not in BAD_PASSWORDS:
        print("Password set")
    elif len(password) < 8:
        print("Password is too short, please try again")
        SetPassword()
    elif len(password) > 13:
        print("Password is too long, please try again")
        SetPassword()
    elif password is in BAD_PASSWORDS:
        print("Password not accepted, please try again")
        SetPassword()
    else:
        print("Password not accepted, please try again")
        SetPassword()

SetPassword()
