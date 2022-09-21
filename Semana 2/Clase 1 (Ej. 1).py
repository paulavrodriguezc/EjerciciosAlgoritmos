x=input("Introducir un número (dividendo): ")
y=input("Introducir un número (divisor): ")
is_valid=True
if x.isnumeric():
    x=int(x)
else:
    is_valid=False
if y.isnumeric():
    y=int(x)
else: 
    is_valid=False
if is_valid:
    if y==0:
        print("Error.")
    else:
        print(x/y)
else:
    print("Caracter inválido.")