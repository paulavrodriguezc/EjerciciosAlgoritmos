number=input("Please enter a number greater than 0: ")
if number.isnumeric():
    number=int(number)
    for i in range(1, number+1, 1):
        print((i)*"*")
else:
    print("Invalid answer.")