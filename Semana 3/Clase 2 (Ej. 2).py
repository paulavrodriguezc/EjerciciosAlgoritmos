personal_info={}
while True:
    key_name=input("What data would you like to store in your user? e.g. Name, age, etc.: ")
    value_info=input("Please enter the information: ").title()
    personal_info[key_name]=value_info
    for key, value in personal_info.items():
        print(f"Your {key} is {value}.")
    if input("Would you like to continue adding information? \nY: Yes \nN: No \n----> ")=="N":
        break