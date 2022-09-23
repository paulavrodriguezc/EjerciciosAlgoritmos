number=input("Please enter an integer number greater than 0: ")
count = 0
if number.isnumeric():
    number=int(number)
    if number>0:
        for i in range(number, -1, -1):
            if count!=number:
                print(i, end=", ")
            else:
                print(i)
            count+=1
    else:
        print(f"The number {number} is not greater than 0.")
else:
    print("Invalid answer.")