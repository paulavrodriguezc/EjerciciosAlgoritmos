import random
class Race:
    def __init__(self,num_carrera,horses):
        self.num_carrera=num_carrera
        self.horses=horses
    def start_Race(self):
        print("Go!")
        print("The horses have started racing:")
        for horse in self.horses:
            print(f"*{horse.name}")
    def choose_winner(self):
        print(f"The winner is {random.choice(self.horses).name}.")
        # se pone el .name fuera del paréntesis porque lo que se va a escoger de manera aleatoria es el ganador (objeto)
        # después de elegirlo, es que busco su nombre. de lo contrario, me da su posición en la memoria