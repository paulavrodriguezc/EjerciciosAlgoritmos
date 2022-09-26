number=input("Please enter an integer number greater than 2: ")
while not number.isnumeric() or int(number)<2:
    number=input("Invalid answer. Please try again: ")
number=int(number)
d=2
while number%d!=0:
    d+=1
if d==number:
    print(f"The number {number} is prime.")
else:
    print(f"The number {number} is NOT prime.")