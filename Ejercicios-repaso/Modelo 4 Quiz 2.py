from Vehicles import Vehicle, Car
def validate_option(option: str):
    while not option.isnumeric() or not option in ["1","2","3","4"]:
        option=input("Invalid input. Please select one option from the following: \n1. Register an arriving vehicle \n2. Register the departure of a vehicle \n3. Show all vehicles in the parking lot \n4. Exit \n---> ")
    return int(option)
def greet_and_menu():
    print("Welcome to our system!")
    option=input("Please select one option from the following: \n1. Register an arriving vehicle \n2. Register the departure of a vehicle \n3. Show all vehicles in the parking lot \n4. Exit \n---> ")
    option=validate_option(option)
    return option
def validate_string(information: str):
    input_given=input(f"Please enter {information}: ")
    while not input_given.isalpha():
        input_given=input(f"Invalid input. Please enter {information}: ")
    return input_given
def validate_number(information: str):
    number_given=input(f"Please enter {information}: ")
    while not number_given.isnumeric():
        number_given=input(f"Invalid input. Please enter {information}: ")
    return int(number_given)
def register_vehicle(parking_lot_db: list, plates: list):
    plate=input("Please enter the plate of the vehicle: ")
    while not plate.isalnum():
        plate=input("Invalid input. Please enter the plate of the vehicle: ")
    while plate in plates:
        plate=input("The vehicle already exists. Please enter the plate of the vehicle: ")
    plates.append(plate)
    brand=validate_string("the brand of the vehicle")
    parking_space=validate_number("number of the parking space of the vehicle")
    toa=input("Please enter the time of arrival of the vehicle in this format (10:00): ")
    type=input("Is the vehicle a motorcycle (M) or a car (C)? \n---> ").capitalize()
    while not type.isalpha() or not type in ["M","C"]:
        type=input("Invalid input. Is the vehicle a motorcycle (M) or a car (C)? \n---> ").capitalize()
    if type=="C":
        disabled=input("Is the car in a disabled parking space? \n1. Yes \n2. No \n--> ")
        while not disabled.isnumeric() or not disabled in ["1","2"]:
            disabled=input("Invalid input. Is the car in a disabled parking space? \n1. Yes \n2. No \n--> ")
        if disabled=="1":
            disabled=True
        else:
            disabled=False
        car=Car(plate,brand,parking_space,toa,None,"Car",disabled)
        parking_lot_db.append(car)
    else:
        motorcyle=Vehicle(plate,brand,parking_space,toa,None,"Motorcycle")
        parking_lot_db.append(motorcyle)
def print_vehicles(parking_lot_db: list):
    vehicle_num=0
    for vehicle in parking_lot_db:
        vehicle_num+=1
        print(f"Vehicle #{vehicle_num}")
        vehicle.print_information()
def print_vehicles_in(parking_lot_db: list):
    vehicle_num=0
    for vehicle in parking_lot_db:
        if vehicle.tod==None:
            vehicle_num+=1
            print(f"Vehicle #{vehicle_num}")
            vehicle.print_information()
def departure_vehicle(parking_lot_db: list, plates: list):
    car_departed=input("Please enter the plate of the car departing: ")
    while not car_departed in plates:
        car_departed=input("The vehicle does not exist or has already left. Please enter the plate of the vehicle: ")
    tod=input("Please enter the time of departure of the vehicle in this format (10:00): ")
    for vehicle in parking_lot_db:
        if vehicle.plate==car_departed:
            vehicle.tod=tod
            vehicle.parking_space=None
    plates.remove(car_departed)
def main():
    continuing=True
    parking_lot_db=[]
    plates=[]
    while continuing:
        option=greet_and_menu()
        if option==1:
            register_vehicle(parking_lot_db, plates)
        elif option==2:
            print_vehicles(parking_lot_db)
            departure_vehicle(parking_lot_db, plates)
        elif option==3:
            print_vehicles_in(parking_lot_db)
        else:
            print("Thank you for preferring us, have a nice day!")
            continuing=False
main()