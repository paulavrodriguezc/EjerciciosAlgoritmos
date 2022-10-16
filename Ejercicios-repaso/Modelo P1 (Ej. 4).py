from webbrowser import get
def get_number():
    number=input("Please enter an integer number greater than 0: ")
    while not number.isnumeric() or int(number)<=0:
        print("Invalid input.")
        number=input("Please enter an integer number greater than 0: ")
    return number
def prime_list(number):
    primes=[]
    for x in range(2,number+1):
        count=0
        for y in range(1,x+1):
            if x%y==0:
                count+=1
        if count==2:
            primes.append(x)
    return primes
def find_multipliers(primes,number):
    multipliers=[]
    not_multipliers=True
    for x in primes:
        indice=primes.index(x)
        while not_multipliers:
            indice+=1
            if indice>(len(primes)-1):
                break
            mult=x*primes[indice]
            if mult==number:
                multipliers.append(x)
                multipliers.append(primes[indice])
                not_multipliers=False
            else:
                continue
    return multipliers
def main():
    number=int(get_number())
    primes=prime_list(number)
    multipliers=find_multipliers(primes,number)
    print(f"The prime numbers that multiplied give {number} are: {multipliers}.")
main()