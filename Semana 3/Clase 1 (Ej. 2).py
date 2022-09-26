number=input("Please enter an integer number greater than 0: ")
while not number.isnumeric() or int(number)<=0:
    number=input("Invalid answer. Please enter a number: ")
number=int(number)
for i in range(1,number+1,2):
    aux=i
    while aux>=1:
        if aux==1:
            print(aux)
        else:
            print(aux, end=" ")
        aux-=2