tupla_dada=([313, 153, 370], [], [31, 515, 78593, 3819, 12],
[407, 9041], [371, 706], [407,153, 1, 2],
[41, 4], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9],
[313, 54748, 370], [], [31, 515, 432, 313, 45],
[313, 88, 407], [153, 370], [1634, 8208, 9474])
narcissists=set()
for listas in tupla_dada:
    for elemento in listas:
        suma=0
        if len(str(elemento))>2:
            for x in str(elemento):
                cubo=int(x)**3
                suma+=cubo
                if suma==int(elemento):
                    narcissists.add(elemento)
print(f"The narcissists numbers are: {narcissists}.")