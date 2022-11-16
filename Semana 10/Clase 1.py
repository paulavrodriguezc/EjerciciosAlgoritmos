# Insertion
def main():
    lista=[6,5,3,1,8,7,2,4]
    print(f"The original list is {lista}.")
    for i in range(len(lista)):
        temp=i
        valor=lista[i]
        j=i-1
        while j>=0 and valor<lista[j]:
            lista[temp]=lista[j]
            lista[j]=valor
            temp-=1
            j-=1
    print(f"The list in order is {lista}.")
main()