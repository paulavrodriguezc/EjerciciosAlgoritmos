# Búsqueda binaria: se tiene un número referencia, en base a eso, se subdivide la secuencia de datos ORDENADA.
def selection(list: list):
    for i in range(len(list)):
        menor=i
        for j in range(i+1,len(list)):
            if list[j]<list[menor]:
                menor=j
        temp=list[i]
        list[i]=list[menor]
        list[menor]=temp
    return list
def binary_search(list: list, number: int):
    start=0
    final=len(list)-1
    middle=(start+final)//2
    if len(list)==1:
        if list[0]==number:
            return number
        else:
            return -1
            # -1 indica que NO se consiguió (en lenguaje de programación=False)
    if number>list[middle]:
        return binary_search(list[middle:final],number)
    elif number<list[middle]:
        return binary_search(list[start:middle],number)
    else:
        return number
def main():
    list=[6,5,3,1,8,7,2,4]
    list_in_order=selection(list)
    number_given=input("Please enter the number you wish to search on the list: ")
    while not number_given.isnumeric():
        number_given=input("Invalid input. Please enter the number you wish to search on the list: ")
    binary_search(list_in_order, int(number_given))
    if binary_search(list_in_order,int(number_given))!=-1:
        print(f"The number {number_given} was found on the list.")
    else:
        print(f"The number {number_given} was not found on the list.")
main()