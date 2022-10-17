def welcome():
    print("***Welcome***")
def get_option(studies):
    for key,value in studies.items():
        for key_interno, value_interno in value.items():
            print(f"\n* {key}: {value_interno}", end=".")
            #arreglar impresión
    return input("\nPlease enter your option: ")
def get_client_data(study):
    client={
        "ID":int(input("Please enter your ID number: ")),
        "age":int(input("Please enter your age: ")),
        "sex":input("Please enter your sex (M/F): "),
        "study":study
    }
    return client
def print_invoice(client,studies):
    print("***RECEIPT***")
    print("ID number: ", client.get["ID"])
    print("Age ", client.get["age"])
    print("Sex: ", client.get["sex"])
    print("Study in question: ", studies.get(client.get["study"]))
def discounts_gotten(client, studies, client_number):
    discount_applied=0
    if client.get("Sex")=="F" and client.get("Age")>55:
        discount_applied+=(studies.get(client.get("study")).get("cost"))*0.25
    elif client.get("Sex")=="M" and client.get("Age")>65:
        discount_applied+=(studies.get(client.get("study")).get("cost"))*0.25
    if client_number%2!=0:
        discount_applied+=(studies.get(client.get("study")).get("cost"))*0.02
    return discount_applied
def get_total(studies,client,discount):
    total_amount=0
    total_amount=(studies.get(client.get("study")).get("cost"))-discount
    return total_amount
def main():
    studies={
        "U":{
            "description": "Ultrasonido",
            "cost": 8900
        },
        "T":{
            "description": "Tomografía",
            "cost": 12640
        },
        "R":{
            "description": "Resonancia",
            "cost": 15600
        }
    }
    welcome()
    clients=[]
    discount=0
    total_discounts=0
    total_day=0
    clients_u=0
    clients_t=0
    clients_r=0
    average_per_client=0
    average_u=0
    average_t=0
    average_r=0
    while True:
        option=get_option(studies)
        client=get_client_data(option)
        clients.append(client)
        discount=discounts_gotten(client, studies, len(clients))
        total_client=get_total(studies,client,discount)
        client["total"]=total_client
        total_discounts+=discount
        total_day+=total_client
        print_invoice(client,studies)
        if client.get("study")=="U":
            clients_u+=1
        elif client.get("study")=="T":
            clients_t+=1
        else:
            clients_r+=1
        if len(clients)>=1:
            average_per_client=(total_day)/(len(clients))
        else:
            print("There were no clients today.")
        if clients_u>=1:
            pass
        if clients_t>=1:
            pass
        if clients_r>=1:
            pass
        if input("Do you wish to continue? \nY for yes. \nN for no. \n---> ")=="N":
            break
        # print_end_day(promedio de pago por tipo de estudio)
main()