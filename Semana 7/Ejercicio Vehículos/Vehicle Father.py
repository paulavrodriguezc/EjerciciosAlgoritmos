class Vehicles:
    def __init__(self, color, wheels):
        self.color=color
        # el de self.color es el atributo y el color en el def init es el parámetro: información dada por el usuario
        self.wheels=wheels
    def give_info(self):
        return f"* Color: {self.color} \n* Number of wheels: {self.wheels}"
        
class Car(Vehicles):
    def __init__(self, color, wheels, speed, motor_capacity):
        super().__init__(color, wheels)
        self.speed=speed
        self.motor_capacity=motor_capacity
    def give_info(self):
        return f"* Speed: {self.speed} \n* Motor capacity: {self.motor_capacity}"

class Truck(Car):
    def __init__(self, color, wheels, speed, motor_capacity, capacity):
        super().__init__(color, wheels, speed, motor_capacity)
        self.capacity=capacity
        # en el caso de que un atributo sea constante (es un valor dado e inmutable): no se pone como parámetro. SOLO se define con el
        # self.variable=constante
    def give_info(self):
        return f"* Capacity: {self.capacity}"

class Bike(Vehicles):
    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.type=type
    def give_info(self):
        return f"* Type: {self.type}"

class Motorbike(Bike):
    def __init__(self, color, wheels, type, speed, motor_capacity):
        super().__init__(color, wheels, type)
        self.speed=speed
        self.motor_capacity=motor_capacity
    def give_info(self):
        return f"* Speed: {self.speed} \n* Motor capacity: {self.motor_capacity}"