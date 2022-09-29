password=input("Please enter a password for your user: ")
password_info=[]
confirmation=False
while confirmation==False:
    if len(password)<8:
        print("Your password is too short! Remember it must have at least 8 characters.")
        password=input("Please enter a password for your user: ")
    elif password.islower():
        print("Your password only has lowercase. Remember it must have at least one capital letter!")
        password=input("Please enter a password for your user: ")
    elif password.isupper():
        print("Your password only has uppercase. Remember it must have at least one lower letter!")
        password=input("Please enter a password for your user: ")
    elif password.isalpha():
        print("Your password must have at least one number!")
        password=input("Please enter a password for your user: ")
    elif password.isalnum():
        print("Your password must have at least one not alphanumeric character!")
        password=input("Please enter a password for your user: ")
    else:
        confirmation=True
password_info.append(password)
print(password_info)