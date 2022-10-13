from itertools import product
def add_numbers(n1,n2):
    sum=n1+n2
    return sum
def multiply_numbers(n1,n2):
    product=n1*n2
    return product
number_1=input("Please enter a number: ")
while not number_1.isnumeric():
    print("Invalid input.")
    number_1=input("Please enter a number: ")
number_2=input("Please enter a number: ")
while not number_2.isnumeric():
    print("Invalid input.")
    number_2=input("Please enter a number: ")
number_1=int(number_1)
number_2=int(number_2)
sum=add_numbers(number_1,number_2)
print(f"The result of the sum is {sum}.")
product=multiply_numbers(number_1,number_2)
print(f"The product of the numbers is {product}.")