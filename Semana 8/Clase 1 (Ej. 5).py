def validate_number():
    n=input("Please enter the maximum number of the Fibonacci list you wish to create: ")
    while not n.isnumeric() or int(n)<0:
        n=input("Invalid input. Please enter the maximum number of the Fibonacci list you wish to create: ")
    return int(n)
def fibonacci(max: int, n_1=0, n_2=1):
    print(n_1, end=" ")
    if max<n_2:
        return n_2
    return fibonacci(max, n_2, n_1+n_2)
def main():
    max=validate_number()
    fibonacci(max)
main()