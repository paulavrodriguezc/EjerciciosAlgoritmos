count=0
is_triangular=False
number=input("Please enter an integer number greater than 0: ")
while not number.isnumeric() or int(number)<1:
    print("Invalid option.")
    number=input("Please remember to enter an integer number greater than 0: ")
number=int(number)
if number%2==0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
for x in range(1,number+1):
    count+=x
    if count==number:
        is_triangular=True
        break
if is_triangular:
    print(f"The number {number} is triangular.")
else:
    print(f"The number {number} is not triangular.")