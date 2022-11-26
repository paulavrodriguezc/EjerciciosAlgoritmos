def factorial(number: int):
    if number==1:
        return 1
    else:
        result=number*factorial(number-1)
        return result
def main():
    number=input("Please enter an integer number greater than 0: ")
    while not number.isnumeric() or int(number)<0:
        number=input("Invalid input. Please enter an integer number greater than 0: ")
    print(f"The factorial of {number} is {factorial(int(number))}.")
main()