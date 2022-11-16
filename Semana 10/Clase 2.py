# Búsqueda lineal: busca en todas las posiciones de una secuencia de datos, hasta encontrar lo que estamos buscando.
def lineal_search(number_given: int, list: list):
    for number in list:
        if number==number_given:
            return number
def main():
    keep_going=True
    list=[6,5,3,1,8,7,2,4]
    while keep_going:
        number_given=input("Please enter the number you wish to search on the list: ")
        while not number_given.isnumeric():
            number_given=input("Invalid input. Please enter the number you wish to search on the list: ")
        if lineal_search(int(number_given), list):
            print(f"The number {number_given} has been found on the list.")
        else:
            print(f"The number {number_given} has not been found on the list.")
        option=input("Do you wish to continue? \n*Y for yes \n*N for no \n---> ").capitalize()
        while not option in ["Y","N"]:
            option=input("Invalid input. Do you wish to continue? \n*Y for yes \n*N for no \n---> ").capitalize()
        if option=="N":
            keep_going=False
main()