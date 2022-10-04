number=input("Please enter an integer number: ")
while not number.isnumeric():
    number=input("Invalid input. Please enter an integer number: ")
number=int(number)
aux=0
for i in range(1,number+1,1):
    if number%i==0:
        aux+=1
if aux==2:
    print(f"The number {number} is prime.")
else:
    print(f"The number {number} is composite.")
is_pronic=False
for i in range(1,number+1):
    if number==(i)*(i+1):
        is_pronic=True
if is_pronic:
    print(f"The number {number} is pronic.")
else:
    print(f"The number {number} is not pronic.")        
#palíndromo (cómo recorro número por número el número completo y cómo los comparo/hago que los dígitos se guarden en una lista? y después comparo?)
count=0
for x in range(1,number):
    if number%x==0:
        count+=x
if count==number:
    print(f"The number {number} is perfect.")
elif count>number:
    print(f"The number {number} is abundant.")
else:
    print(f"The number {number} is deficient.")
square=number**(1/2)
if square/int(square)==1:
    print(f"The number {number} is a square.")
else:
    print(f"The number {number} is not a square.")