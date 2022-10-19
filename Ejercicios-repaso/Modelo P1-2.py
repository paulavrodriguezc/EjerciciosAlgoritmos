tupla_dada=([313, 6786, 5151], [1, 4, 10], [41, 53, 86, 56, 12],
[84, 4], [], [35, 4, 1, 2],
[1, 4], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9],
[100, 84, 4781], [], [53, 56, 1, 4, 45],
[84, 88, 407], [153, 25], [10, 35, 9474],)
piramidales_triangulares=[]
for listas in tupla_dada:
    for elemento in listas:
        for x in range(1,elemento+1):
            if (x*(x+1)*(x+2))/6==elemento:
                if elemento in piramidales_triangulares:
                    break
                piramidales_triangulares.append(elemento)
piramidales_triangulares.sort()
print(f"The list of piramidal triangular numbers is: {piramidales_triangulares}.")