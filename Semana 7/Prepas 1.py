def jugar(intento=1):
    respuesta=input("¿De qué color es una naranja? ").title()
    if respuesta!="Naranja":
        if intento<3:
            print("\n¡Fallaste! Inténtalo otra vez.")
            intento+=1
            jugar(intento)
        else:
            print("\n¡Perdiste!")
    else:
        print("¡Ganaste!")
def main():
    jugar()
main()