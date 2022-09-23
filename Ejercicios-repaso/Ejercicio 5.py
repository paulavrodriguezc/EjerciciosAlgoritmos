age=input("Please enter your age: ")
if age.isnumeric():
    age=int(age)
    for i in range(age):
        print("You have turned "+str(i+1) + " years.")
else:
    print("Invalid answer.")