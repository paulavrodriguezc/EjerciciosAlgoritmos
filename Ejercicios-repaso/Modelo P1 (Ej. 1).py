def get_number():
    while True:
        try:
            number=int(input("Please enter an integer number greater than 0: "))
            if number<=0:
                raise Exception
            break
        except:
            print("Invalid input.")
    return number
def fibonacci_list(number):
    fibonacci_sequence=[0,1]
    for x in range(0,number+1):
        if x==0:
            n1=x
            n2=x+1
        n=n1+n2
        n1=n2
        n2=n
        fibonacci_sequence.append(n)
    return fibonacci_sequence
def main():
    while True:
        number=get_number()
        fibonacci_sequence=fibonacci_list(number)
        if number in fibonacci_sequence:
            print(f"The number {number} is part of the Fibonacci sequence.")
            break
        else:
            print(f"The number {number} is not a part of the Fibonacci sequence.") 
main()