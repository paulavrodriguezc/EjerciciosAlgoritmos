n=input("Please enter an integer number greater than 0: ")
while not n.isnumeric() or int(n)<0:
    n=input("Invalid input. Please enter an integer number greater than 0: ")
n=int(n)
fermat_number=(2**(2*n))+1
aux=0
for i in range(1,fermat_number+1):
    if fermat_number%i==0:
        aux+=1
if aux==2:
    print(f"The number {n} is a prime fermat number.")
else:
    print(f"The number {n} is not a prime fermat number.")