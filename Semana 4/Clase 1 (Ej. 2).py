number=int(input("Please enter an integer number greater than 0: "))
aux=1
is_pronic=False
while aux<number:
    if aux*(aux+1)==number:
        is_pronic=True
        break
    aux+=1
if is_pronic:
    print(f"The number {number} is pronic.")
else: 
    print(f"The number {number} is NOT pronic.")