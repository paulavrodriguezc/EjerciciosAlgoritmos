from ClasesModeloQuiz2 import Punto
def information_point(punto):
    punto.get_coordinate()
    punto.print_punto()
    punto.get_quadrant()
def main():
    punto=Punto()
    punto_2=Punto()
    information_point(punto)
    information_point(punto_2)
    punto.vector(punto,punto_2)
main()