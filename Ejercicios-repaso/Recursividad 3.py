# x es fila y y es columna
def find_exit(matriz:list, vector: list):
    exit_found=False
    if vector[0]!=6 and vector[1]!=6:
        for fila in matriz:
            if vector[0]==matriz.index(fila):
                for command in range(len(fila)):
                    if vector[1]==command:
                        if fila[command]=="UP":
                            vector[0]-=1
                            find_exit(matriz,vector)
                        elif fila[command]=="DOWN":
                            vector[0]+=1
                            find_exit(matriz,vector)
                        elif fila[command]=="RIGHT":
                            vector[1]+=1
                            find_exit(matriz,vector)
                        elif fila[command]=="LEFT":
                            vector[1]-=1
                            find_exit(matriz,vector)
    else:
        exit_found=True
    return exit_found
def main():
    matriz=[
["DOWN","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"],
["DOWN","DOWN","LEFT","LEFT","LEFT","LEFT","LEFT"],
["DOWN","WALL","RIGHT","DOWN","DOWN","LEFT","LEFT"],
["RIGHT","RIGHT","UP","DOWN","DOWN","RIGHT","DOWN"],
["WALL","DOWN","LEFT","LEFT","RIGHT","UP","DOWN"],
["UP","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"],
["UP","LEFT","LEFT","LEFT","LEFT","LEFT","EXIT"]]
    vector=[[0,0],[6,5],[2,6],[0,1]]
    for posicion in vector:
        print(f"{posicion}:")
        exit_found=find_exit(matriz, posicion)
        if exit_found:
            print(f"\tThe entry leads to the exit.\n")
        else:
            print(f"\tThe entry does not lead to the exit. \n")
main()