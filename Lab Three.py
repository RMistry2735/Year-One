name = input("What is your name? ")
if name == "":
    print("Hello, Stranger!")
else:
    print("Hello", name,". Good to meet you")
    

password = input("Please input a password: ")
password2 = input("Please input the password again: ")
if password == password2:
    print("Password set")
else:
    print("The 2 passwords were different")
