# función recursiva depende de parámetros y un bucle depende de lo ocurrido en su scope
def validate_number():
    n=input("Please enter an integer number greater than 0: ")
    while not n.isnumeric() or int(n)<0:
        n=input("Invalid input. Please enter an integer number greater than 0: ")
    return int(n)
def factorial(n: int):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
def main():
    n=validate_number()
    print(f"The factorial is {factorial(n)}.")
main()