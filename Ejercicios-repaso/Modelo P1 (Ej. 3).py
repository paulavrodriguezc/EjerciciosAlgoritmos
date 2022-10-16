def cont():
    option=input("Do you wish to continue? \n'Y' for yes \n'N' for no \n---> ").capitalize()
    while not option.isalpha():
        print("Invalid option.")
        option=input("Do you wish to continue? \n'Y' for yes \n'N' for no \n---> ").capitalize()
    return option
def get_number():
    number=input("Please enter an integer number greater than 0: ")
    while True:
        try:
            number=int(number)
            if number==0:
                raise Exception
            break
        except:
            print("Invalid input.")
    return number
def divisors_num(number):
    divisors=[]
    sum=0
    for x in range(1,number):
        if number%x==0:
            divisors.append(x)
    for x in divisors:
        sum+=x
    return sum
def is_perfect(sum):
    accum=0
    is_ambitious=True
    for x in range(1,sum):
        if sum%x==0:
            accum+=x
    if accum!=sum:
        is_ambitious=False
    return is_ambitious
def main():
    while True:
        number=get_number()
        sum=divisors_num(number)
        is_ambitious=is_perfect(sum)
        if is_ambitious:
            print(f"The number {number} is ambitious.")
        else:
            print(f"The number {number} is not ambitious.")
        option=cont()
        if option=="N":
            print("Thank you, have a great day.")
            break
main()