def get_number():
    number=input("Please enter an integer number greater than 0: ")
    while True:
        try:
            number=int(number)
            if number==0:
                raise Exception
                # levanta una excepción para hacerle saber al programa que lo introducido no es válido
            break
        except:
            print("Invalid input.")
    return number
def factorial(number):
    accum=1
    for x in range(2,number+1):
        accum*=x
    return accum
def main():
    number=get_number()
    # definir number=get_number() y accum=factorial(number) para que la función pueda devolver un valor, sino la variable SÓLO existe en la función
    accum=factorial(number)
    print(f"Your factorial is: {accum}.")
main()