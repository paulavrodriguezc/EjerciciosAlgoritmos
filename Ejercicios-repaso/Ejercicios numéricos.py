number=input("Please enter an integer number: ")
while not number.isnumeric():
    number=input("Invalid input. Please enter an integer number: ")
number=int(number)
aux=0
#primo o compuesto
for i in range(1,number+1):
    if number%i==0:
        aux+=1
if aux==2:
    print(f"The number {number} is prime.")
else:
    print(f"The number {number} is composite.")
#oblongo
is_pronic=False
for i in range(1,number+1):
    if number==(i)*(i+1):
        is_pronic=True
if is_pronic:
    print(f"The number {number} is pronic.")
else:
    print(f"The number {number} is not pronic.")
#palíndromo
number=str(number)
reversed_num=number[::-1]
if number==reversed_num:
    print(f"The number {number} is a palindrome.")
else:
    print(f"The number {number} is not a palindrome.")
number=int(number)
#perfecto,abundante,deficiente
count=0
for x in range(1,number):
    if number%x==0:
        count+=x
if count==number:
    print(f"The number {number} is perfect.")
elif count>number:
    print(f"The number {number} is abundant.")
else:
    print(f"The number {number} is deficient.")
#cuadrado
square=number**(1/2)
if square/int(square)==1:
    print(f"The number {number} is a square.")
else:
    print(f"The number {number} is not a square.")
#libre de cuadrados
divisors=[]
for x in range(2,number+1):
    if number%x==0:
        divisors.append(x)
for i in divisors:
    square=i**(1/2)
    if square/int(square)==1:
        print(f"The number {number} is not free of squares.")
        free_square=False
        break
    else:
        free_square=True
if free_square:
    print(f"The number {number} is free of squares.")

############################# NÚMERO DE MERSENNE
# number=input("Please enter an ineteger number greater than 0: ")
# while not number.isnumeric() or int(number)<1:
#     print("Invalid input. Remember the input must be an integer number greater than 0")
#     number=input("Please enter said number: ")
# number=int(number)
# aux=0
# is_prime=True
# is_mersenne=True
# for x in range(1,number+1):
#     if number%x==0:
#         aux+=1
# if aux==2:
#     is_prime=True
# else:
#     is_prime=False
# if is_prime:
#     for i in range(1,number+1):
#         mersenne=(2**i)-1
#         if mersenne==number:
#             print(f"The number {number} is a mersenne prime.")
#             is_mersenne=True
#             break
#         else:
#             is_mersenne=False
#     if is_mersenne==False:
#         print(f"The number {number} is not a mersenne prime.")
# else:
#     print(f"The number {number} is not a mersenne prime.")

############################## REPUNIT
# digits=[]
# for i in number:
#     i=int(i)
#     digits.append(i)
# for x in digits:
#     if digits[0]!=x:
#         is_repunit=False
#         break
#     num+=x
# if is_repunit:
#     print(f"The number {number} is repunit.")
# else:
#     print(f"The number {number} is not repunit.")

################################ PRIMO DE FERMAT
# number=int(number)
# fermat_number=(2**(2*n))+1
# aux_1=0
# for i in range(1,fermat_number+1):
#     if fermat_number%i==0:
#         aux+=1
# if aux==2:
#     print(f"The number {number} is a prime fermat number.")
# else:
#     print(f"The number {number} is not a prime fermat number.")

################### FELIZ
# digits=[]
# for x in number:
#     digits.append(x)
# while len(digits)>1:
#     sum=0
#     for i in digits:
#         i=int(i)
#         sum+=(i**2) 
#     number=str(sum)
#     digits=[]
#     for x in number:
#         digits.append(x)
# if int(digits[0])==1:
#     print("The number is happy.")
# else:
#     print("The number is not happy.")

################ AMIGOS
# def get_number():
#     number=input("Please enter an integer number greater than 0: ")
#     while not number.isnumeric():
#         print("Invalid input.")
#         number=input("Please enter an integer number greater than 0: ")
#     while int(number)<=0:
#         print("Invalid input.")
#         number=input("Please enter an integer number greater than 0: ")
#     return int(number)
# def divisors(number):
#     divisors=[]
#     for x in range(1,number):
#         if number%x==0:
#             divisors.append(x)
#     return divisors
# def sum_divisors(divisors_list):
#     sum=0
#     for x in divisors_list:
#         sum+=x
#     return sum
# def main():
#     while True:
#         n1=get_number()
#         n2=get_number()
#         divisors_n1=divisors(n1)
#         divisors_n2=divisors(n2)
#         sum_n1=sum_divisors(divisors_n1)
#         sum_n2=sum_divisors(divisors_n2)
#         if sum_n1==n2 and sum_n2==n1:
#             print(f"The numbers {n1} and {n2} are amicable numbers.")
#         else:
#             print(f"The numbers {n1} and {n2} are not amicable numbers.")
#         if input("Do you wish to continue? \n-Y for yes \n-N for no \n---> ").capitalize()=="N":
#             break
# main()

################################ PRIMOS QUE MULTIPLICADOS DAN UN NUMERO DADO
# from webbrowser import get
# def get_number():
#     number=input("Please enter an integer number greater than 0: ")
#     while not number.isnumeric() or int(number)<=0:
#         print("Invalid input.")
#         number=input("Please enter an integer number greater than 0: ")
#     return number
# def prime_list(number):
#     primes=[]
#     for x in range(2,number+1):
#         count=0
#         for y in range(1,x+1):
#             if x%y==0:
#                 count+=1
#         if count==2:
#             primes.append(x)
#     return primes
# def find_multipliers(primes,number):
#     multipliers=[]
#     not_multipliers=True
#     for x in primes:
#         indice=primes.index(x)
#         while not_multipliers:
#             indice+=1
#             if indice>(len(primes)-1):
#                 break
#             mult=x*primes[indice]
#             if mult==number:
#                 multipliers.append(x)
#                 multipliers.append(primes[indice])
#                 not_multipliers=False
#             else:
#                 continue
#     return multipliers
# def main():
#     number=int(get_number())
#     primes=prime_list(number)
#     multipliers=find_multipliers(primes,number)
#     print(f"The prime numbers that multiplied give {number} are: {multipliers}.")
# main()

######################### AMBICIOSO
# def cont():
#     option=input("Do you wish to continue? \n'Y' for yes \n'N' for no \n---> ").capitalize()
#     while not option.isalpha():
#         print("Invalid option.")
#         option=input("Do you wish to continue? \n'Y' for yes \n'N' for no \n---> ").capitalize()
#     return option
# def get_number():
#     number=input("Please enter an integer number greater than 0: ")
#     while True:
#         try:
#             number=int(number)
#             if number==0:
#                 raise Exception
#             break
#         except:
#             print("Invalid input.")
#     return number
# def divisors_num(number):
#     divisors=[]
#     sum=0
#     for x in range(1,number):
#         if number%x==0:
#             divisors.append(x)
#     for x in divisors:
#         sum+=x
#     return sum
# def is_perfect(sum):
#     accum=0
#     is_ambitious=True
#     for x in range(1,sum):
#         if sum%x==0:
#             accum+=x
#     if accum!=sum:
#         is_ambitious=False
#     return is_ambitious
# def main():
#     while True:
#         number=get_number()
#         sum=divisors_num(number)
#         is_ambitious=is_perfect(sum)
#         if is_ambitious:
#             print(f"The number {number} is ambitious.")
#         else:
#             print(f"The number {number} is not ambitious.")
#         option=cont()
#         if option=="N":
#             print("Thank you, have a great day.")
#             break
# main()

############################# SERIE DE FIBONACCI
# def get_number():
#     while True:
#         try:
#             number=int(input("Please enter an integer number greater than 0: "))
#             if number<=0:
#                 raise Exception
#             break
#         except:
#             print("Invalid input.")
#     return number
# def fibonacci_list(number):
#     fibonacci_sequence=[0,1]
#     for x in range(0,number+1):
#         if x==0:
#             n1=x
#             n2=x+1
#         n=n1+n2
#         n1=n2
#         n2=n
#         fibonacci_sequence.append(n)
#     return fibonacci_sequence
# def main():
#     while True:
#         number=get_number()
#         fibonacci_sequence=fibonacci_list(number)
#         if number in fibonacci_sequence:
#             print(f"The number {number} is part of the Fibonacci sequence.")
#             break
#         else:
#             print(f"The number {number} is not a part of the Fibonacci sequence.") 
# main()