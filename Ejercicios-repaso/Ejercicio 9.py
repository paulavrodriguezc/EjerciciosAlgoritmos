number=input("Please enter an integer number greater than 0: ")
if number.isnumeric():
    number=int(number)
    if number>0:
        for i in range(1,number+1,2):
            for j in range(i,0,-2):
                print(j, end=" ")
            print("")
    else:
        print(f"The number {number} is not greater than 0.")
else:
    print("Invalid answer.")