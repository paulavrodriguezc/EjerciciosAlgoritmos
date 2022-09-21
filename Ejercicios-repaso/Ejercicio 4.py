age=input("Please enter your age: ")
is_valid=True
if age.isnumeric():
    age=int(age)
    if age>=18:
        print("You are of age.")
    elif age<=0:
        print("Invalid answer.")
    else:
        print("You are a minor.")
else:
    is_valid=False
    print("Invalid answer.")