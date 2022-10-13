number=input("Please enter an ineteger number greater than 0: ")
while not number.isnumeric() or int(number)<1:
    print("Invalid input. Remember the input must be an integer number greater than 0")
    number=input("Please enter said number: ")
number=int(number)
aux=0
is_prime=True
is_mersenne=True
for x in range(1,number+1):
    if number%x==0:
        aux+=1
if aux==2:
    is_prime=True
else:
    is_prime=False
if is_prime:
    for i in range(1,number+1):
        mersenne=(2**i)-1
        if mersenne==number:
            print(f"The number {number} is a mersenne prime.")
            is_mersenne=True
            break
        else:
            is_mersenne=False
    if is_mersenne==False:
        print(f"The number {number} is not a mersenne prime.")
else:
    print(f"The number {number} is not a mersenne prime.")