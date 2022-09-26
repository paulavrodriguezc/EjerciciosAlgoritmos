from random import randint
number=randint(1,1001)
print(f"Your generated password is {number}.")
password=input("Please enter your password: ")
# while not password.isnumeric():
#     print("Hint: your password is a number.")
#     password=input("Please try entering your password again: ")
# while int(password)!=number:
#     password=input("Incorrect password. Please try again: ")
# print("Correct password. Access has been granted.")
while password!=str(number):
    password=input("Please try entering your password again: ")
print("Correct password. Access has been granted.")
