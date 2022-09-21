number=int(input("Please enter a number: "))
aux=number-1
accum=0
while aux>=1:
    if number%aux==0:
        accum+=aux   
    aux-=1
if accum>number:
    print(f"The number {number} is abundant.")
else:
    print(f"The number {number} is not abundant.")