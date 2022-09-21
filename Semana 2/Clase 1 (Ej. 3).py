x=input("Please enter a number: ")
is_valid=True
if x.isnumeric():
    x=float(x)
else: 
    is_valid=False
if is_valid:
    if x%2==0:
        print(f"The number {x} is even.")
    else:
        print(f"The number {x} is odd.")