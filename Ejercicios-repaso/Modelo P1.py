costos={"S":30000,"3":40000,"X":50000,"Y":70000,"C":90000}
user_number=0
recharge=0
clients={}
clients_s=0
clients_3=0
clients_x=0
clients_y=0
clients_c=0
total_s=0
total_3=0
total_x=0
total_y=0
total_c=0
while True:
    user_number+=1
    clients[user_number]={}
    email_user=input("Please enter your e-mail: ")
    while not "@" in email_user:
        print("Invalid e-mail.")
        email_user=input("Please enter your e-mail: ")
    age_user=input("Please enter your age (you must be older than 18): ")
    while not age_user.isnumeric() or int(age_user)<=18:
        print("Invalid input. Remember to enter your age in numeric characters and that you must be older than 18.")
        age_user=input("Please enter your age: ")
    model_selected=input("Please enter the model you wish to purchase: \n-S \n-3 \n-X \n-Y \n-C for cybertruck \n---> ").capitalize()
    while not model_selected in ["S","3","X","Y","C"]:
        print("Model not available. Please select from the given options:")
        model_selected=input("Please enter the model you wish to purchase: \n-S \n-3 \n-X \n-Y \n-C for cybertruck \n---> ").capitalize()
    autopilot=input("Do you wish to have the autopilot function? \n-Y for yes \n-N for no \n---> ").capitalize()
    while not autopilot in ["Y","N"]:
        print("Invalid input.")
        autopilot=input("Do you wish to have the autopilot function? \n-Y for yes \n-N for no \n---> ").capitalize()
    clients[user_number]["email"]=email_user
    clients[user_number]["age"]=int(age_user)
    clients[user_number]["model selected"]=model_selected
    clients[user_number]["autopilot function"]=autopilot
    for num_client,info_client in clients.items():
        for data,info in info_client.items():
            if num_client==user_number:
                if data=="model selected":
                    if info=="S":
                        clients[user_number]["total"]=costos.get("S")
                        clients_s+=1
                        break
                    elif info=="3":
                        clients[user_number]["total"]=costos.get("3")
                        clients_3+=1
                        break
                    elif info=="X":
                        clients[user_number]["total"]=costos.get("X")
                        clients_x+=1
                        break
                    elif info=="Y":
                        clients[user_number]["total"]=costos.get("Y")
                        clients_y+=1
                        break
                    else:
                        clients[user_number]["total"]=costos.get("C")
                        clients_c+=1
                        break              
    if autopilot=="Y":
        recharge=0.05*clients[user_number]["total"]
        clients[user_number]["total"]=clients[user_number]["total"]+recharge
    print("***RECEIPT***")
    for num_client,info_client in clients.items():
        for data,info in info_client.items():
            if num_client==user_number:
                print(f"\t*{data.capitalize()} - {info}")
    if input("Do you wish to see the stats of the day? \n-Y for yes \n-N for no \n---> ").capitalize()=="Y":
        model_seen=input("Please select the model of the car that you wish to see the purchases of: \n-S \n-3 \n-X \n-Y \n-C for cybertruck \n---> ").capitalize()
        while not model_seen in ["S","3","X","Y","C"]:
            print("Model not available. Please select from the given options:")
            model_seen=input("Please enter the model: \n-S \n-3 \n-X \n-Y \n-C for cybertruck \n---> ").capitalize()
        for num_client,info_client in clients.items():
            print(f"***RECEIPT***")
            for data,info in info_client.items():
                if info_client.get("model selected")==model_seen:
                    print(f"\t*{data.capitalize()} - {info}")
        for num_client,info_client in clients.items():
            for data,info in info_client.items():
                if data=="model selected":
                    if info=="S":
                        total_s+=clients[num_client]["total"]
                    elif info=="3":
                        total_3+=clients[num_client]["total"]
                    elif info=="x":
                        total_x+=clients[num_client]["total"]                    
                    elif info=="Y":
                        total_y+=clients[num_client]["total"]
                    else:
                        total_c+=clients[num_client]["total"]
        if clients_s!=0:
            print(f"The average for the model S is ${total_s/clients_s}.")
        if clients_3!=0:
            print(f"The average for the model 3 is ${total_3/clients_3}.")
        if clients_x!=0:
            print(f"The average for the model X is ${total_x/clients_x}.")
        if clients_y!=0:
            print(f"The average for the model Y is ${total_y/clients_y}.")
        if clients_c!=0:
            print(f"The average for the model Cybertruck is ${total_c/clients_c}.")
        montos_facturados=[]
        for num_client,info_client in clients.items():
            for data,info in info_client.items():
                if data=="total":
                    montos_facturados.append(info)
        montos_facturados.sort(reverse=True)
        index_selected=0
        print("The receipts ordered from greater to least amount are as follow:")
        for num_client,info_client in clients.items():
            if info_client.get("total")==montos_facturados[index_selected]:
                print("***RECEIPT***")
                for data,info in info_client.items():
                    print(f"\t*{data.capitalize()} - {info}")
                index_selected+=1
                if index_selected>len(montos_facturados)-1:
                    break
    if input("Do you wish to continue? \n-Y for yes \n-N for no \n---> ").capitalize()=="N":
        print("Have a nice day!")
        break