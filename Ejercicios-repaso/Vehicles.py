class Vehicle:
    def __init__(self, plate, brand, parking_space, toa, tod, type):
        self.plate=plate
        self.brand=brand
        self.parking_space=parking_space
        self.toa=toa
        self.tod=tod
        self.type=type
    def print_information(self):
        print(f"Plate: {self.plate} \nBrand: {self.brand} \nParking space number: {self.parking_space} \nTime of arrival: {self.toa} \nTime of departure: {self.tod} \nType of vehicle: {self.type} \n")
class Car(Vehicle):
    def __init__(self, plate, brand, parking_space, toa, tod, type, disabled):
        super().__init__(plate, brand, parking_space, toa, tod, "Car")
        self.disabled=disabled
    def print_information(self):
        print(f"Plate: {self.plate} \nBrand: {self.brand} \nParking space number: {self.parking_space} \nTime of arrival: {self.toa} \nTime of departure: {self.tod} \nType of vehicle: {self.type} \nDisabled parking space: {self.disabled}")    