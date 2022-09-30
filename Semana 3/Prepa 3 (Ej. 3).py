number=input("Please enter an integer number: ")
count=[]
sum=0
is_repunit=True
while not number.isnumeric():
    print("Remember the input MUST be in numeric characters.")
    number=input("Please enter an integer number: ")
count=list(number)
for i in count:
    if i!=count[0]:
        is_repunit=False
if is_repunit==True:
    print("The number is repunit.")
    for j in number:
        sum+=int(j)
    square=sum**(0.5)
    if square/int(square)==1:
        print(f"The square of the sum of the digits of the number {number} is {square}.")
    else: 
        print(f"The sum of the digits of the number is not a square.")
else:
    print("The number is NOT repunit.")