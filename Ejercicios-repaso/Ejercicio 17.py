poss=list(range(1,13))
values_list=[]
number=input("Please enter a round number between 2 and 12: ")
while not number.isnumeric() or int(number)<2 and int(number)>12:
    print("Invalid answer.")
    number=input("Please remember to enter a round number between 2 and 12: ")
number=int(number)
combo=""
for i in poss:
    for j in poss:
        if i+j==number:
            x=i,j
            y=j,i
            if x not in values_list and y not in values_list:
                combo+=f"\n* {i}-{j} "
                values = i,j
                values_list.append(values)
print(f"The possible combinations of numbers in the dice that added can amount to {number} are: {combo}")