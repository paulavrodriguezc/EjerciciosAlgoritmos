number=input("Please enter an integer number greater than 0: ")
while not number.isnumeric() or int(number)<1:
    number=input("Invalid answer, please try again: ")
while int(number)>=10:
    sum=0
    for i in str(number):
        sum+=int(i)
    number=sum
print(f"The result is {number}.")