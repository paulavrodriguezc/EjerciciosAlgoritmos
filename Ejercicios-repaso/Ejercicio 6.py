number=input("Please enter an integer number greater than 0: ")
if number.isnumeric():
    number=int(number)
    if number>0:
        for i in range(number+1):
            if i%2!=0:
                print(i, end=", ")
    else:
        print(f"The number {number} is not greater than 0.")
else:
    print("Invalid answer.")