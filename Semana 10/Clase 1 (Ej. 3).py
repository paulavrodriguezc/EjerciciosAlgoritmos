# Quicksort
def quick_sort(lista: list):
    if len(lista)<2:
        return lista
    menor,pivote,mayor=partition(lista)
    return quick_sort(menor)+[pivote]+quick_sort(mayor)
def partition(lista: list):
    menores=[]
    mayores=[]
    pivote=lista[0]
    for i in range(len(lista)):
        if lista[i]<pivote:
            menores.append(lista[i])
        elif lista[i]>pivote:
            mayores.append(lista[i])
    return menores, pivote, mayores
def main():
    lista=[6,5,3,1,8,7,2,4]
    print(f"The original list is {lista}.")
    lista_actualizada=quick_sort(lista)
    print(f"The list in order is {lista_actualizada}.")
main()