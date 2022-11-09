def validate_number():
    n=input("Please enter an integer number greater than 0: ")
    while not n.isnumeric() or int(n)<0:
        n=input("Invalid input. Please enter an integer number greater than 0: ")
    return int(n)
def calculate(base: int, exponent: int):
    if exponent==0:
        return 1
    else:
        return base*calculate(base, exponent-1)
def main():
    base=validate_number()
    exponent=validate_number()
    print(f"The total is: {calculate(base, exponent)}.")
main()