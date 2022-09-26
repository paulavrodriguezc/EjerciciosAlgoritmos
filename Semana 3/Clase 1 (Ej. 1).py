number=input("Please enter a round number: ")
while not number.isnumeric():
    number=input("Invalid answer. Please enter a number: ")
number=int(number)
for i in range(1,number+1):
    print(i*"*")