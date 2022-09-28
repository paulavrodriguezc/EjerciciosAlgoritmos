age=input("Please state the age of who the ticket is for: ")
while not age.isnumeric():
    print("Remember to enter the age as a number.")
    age=input("Please state the age of who the ticket is for: ")
age=int(age)
if age<4:
    print("The entry ticket is free.")
elif age==4 or age<=18:
    print("The price for the entry ticket is $10.")
else:
    print("The price for the entry ticket is $14.")