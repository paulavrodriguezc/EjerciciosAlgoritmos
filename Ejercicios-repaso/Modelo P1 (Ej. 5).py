def get_number():
    number=input("Please enter an integer number greater than 0: ")
    while not number.isnumeric():
        print("Invalid input.")
        number=input("Please enter an integer number greater than 0: ")
    while int(number)<=0:
        print("Invalid input.")
        number=input("Please enter an integer number greater than 0: ")
    return int(number)
def divisors(number):
    divisors=[]
    for x in range(1,number):
        if number%x==0:
            divisors.append(x)
    return divisors
def sum_divisors(divisors_list):
    sum=0
    for x in divisors_list:
        sum+=x
    return sum
def main():
    while True:
        n1=get_number()
        n2=get_number()
        divisors_n1=divisors(n1)
        divisors_n2=divisors(n2)
        sum_n1=sum_divisors(divisors_n1)
        sum_n2=sum_divisors(divisors_n2)
        if sum_n1==n2 and sum_n2==n1:
            print(f"The numbers {n1} and {n2} are amicable numbers.")
        else:
            print(f"The numbers {n1} and {n2} are not amicable numbers.")
        if input("Do you wish to continue? \n-Y for yes \n-N for no \n---> ").capitalize()=="N":
            break
main()