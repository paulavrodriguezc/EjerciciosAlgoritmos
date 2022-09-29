personal_info={}
names=[]
last_names=[]
ages=[]
while True:
    name=input("Please enter your first name: ").title()
    last_name=input("Please enter your last name: ").title()
    age=input("Please enter your age (in numbers): ")
    names.append(name)
    last_names.append(last_name)
    ages.append(age)
    personal_info["First name"]=names
    personal_info["Last name"]=last_names
    personal_info["Age"]=ages
    cont=input("Would you like to continue adding information? \n-Y for yes. \n-N for no. \n---->")
    if cont=="N" or cont=="n":
        break
print(personal_info)