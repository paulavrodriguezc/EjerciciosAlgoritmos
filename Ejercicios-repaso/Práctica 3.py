number=input("Please enter an integer number greater than 0: ")
digits=[]
is_repunit=True
num=0
while not number.isnumeric() or int(number)<0:
    number=input("Invalid input. Please enter an integer number greater than 0: ")
for i in number:
    i=int(i)
    digits.append(i)
for x in digits:
    if digits[0]!=x:
        is_repunit=False
        break
    num+=x
if is_repunit:
    print(f"The number {number} is repunit.")
    square=num**(1/2)
    if square/int(square)==1:
        print(f"The sum of the digits in the number {number} is a square.")
    else:
        print(f"The sum of the digits in the number {number} is not a square.")
else: 
    print(f"The number {number} is not repunit.")