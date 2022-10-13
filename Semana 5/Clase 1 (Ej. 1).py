def welcome():
    print("***Welcome***")
def get_option(studies):
    for key,value in studies.items():
        for key_interno, value_interno in value.items():
            print(f"\n* {key}: {value_interno}", end=".")
            #arreglar impresión
    return input("\n Please enter your option: ")
def get_client_data(study):
    client={
        "ID":int(input("Please enter your ID number: ")),
        "age":int(input("Please enter your age: ")),
        "sex":input("Please enter your sex (M/F): "),
        "study":study
    }
    return client
def print_invoice(client):
    print("***RECEIPT***")
    print("ID number: ", client.get["ID"])
    print("Age ", client.get["age"])
    print("Sex: ", client.get["sex"])
    print("Study in question: ", studies.get(client.get["study"]))
def discounts_gotten(client, studies, client_number):
    discount_applied=0
    if client.get("Sex")=="F" and client.get("Age")>55:
        discount_applied+=(studies.get(client.get("Study in question")).get("cost"))*0.25
    elif client.get("Sex")=="M" and client.get("Age")>65:
        discount_applied+=(studies.get(client.get("Study in question")).get("cost"))*0.25
    if client_number%2!=0:
        discount_applied+=(studies.get(client.get("Study in question")).get("cost"))*0.02
    # total_discounts+=1
    return discount_applied
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
    total_discounts=0
    while True:
        option=get_option(studies)
        client=get_client_data(option)
        clients.append(client)
        discounts=discounts_gotten(client, studies, len(clients))
        print_invoice(client, studies, total)
        # arreglar el client data con el descuento
        # función con get_amount(client,discounts,studies)=return studies.get()
        #
        if input("Do you wish to continue? \nY for yes. \nN for no. \n--->")=="N":
            break
        # print_end_day(clients,)
main()