number=input("Please enter an integer number greater than 0: ")
divisors=[]
while not number.isnumeric() or int(number)<0:
    number=input("Invalid input. Please enter an integer number greater than 0: ")
number=int(number)
for i in range(2,number+1):
    if number%i==0:
        divisors.append(i)
for x in divisors:
    square=x**(1/2)
    if square/int(square)==1:
        print(f"The number {number} is not free of squares.")
        is_free_squares=False
        break
    is_free_squares=True
if is_free_squares:
    print(f"The number {number} is free of squares.")