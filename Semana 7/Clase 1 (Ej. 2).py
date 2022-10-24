from Caballos import Horse
from Carrera import Race
from Válida import Valid
def validate_number(input_given):
    while not input_given.isnumeric():
        input_given=input("Invalid input. Please enter your selection again: ")
    return int(input_given)
def main():
    valids=input("How many valids do you want? ")
    races=input("How many races do you want for each valid? ")
    valids=validate_number(valids)
    races=validate_number(races)
    valid_info=Valid(valids,races)
    horse_1=Horse("Rayo",1)
    horse_2=Horse("Azabache",2)
    horse_3=Horse("Trueno",3)
    horse_4=Horse("Rey",4)
    horse_5=Horse("Princesa",5)
    horse_6=Horse("Tormenta",6)
    horse_list=[horse_1,horse_2,horse_3,horse_4,horse_5,horse_6]
    for valid in range(valids):
        race_list=[]
        for race in range(races):
            race_object=Race(race,horse_list)
            race_list.append(race_object)
        for race in race_list:
            race.start_Race()
            race.choose_winner()
main()