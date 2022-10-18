def main():
    clients={}
    end_day={}
    prices={"A":2500,"S":3500}
    number_client=0
    clients_discounted=0
    clients_a=0
    clients_s=0
    income_a=0
    income_s=0
    while True:
        number_client+=1
        discount=0
        clients[number_client]={"CI":int(input("Please enter your ID number: ")),"Type":input("Please select the type of vehicle you wish to ride: \nA for automatic \nS for manual \n---> ").capitalize(),"Hours":int(input("Please enter the number of hours of classes: "))}
        for num_client,info in clients.items():
            if num_client==number_client:
                if clients[number_client]["Type"]=="A":
                    clients[number_client]["Total"]=clients[number_client]["Hours"]*prices.get("A")
                    clients_a+=1
                elif clients[number_client]["Type"]=="S":
                    clients[number_client]["Total"]=clients[number_client]["Hours"]*prices.get("S")
                    clients_s+=1
        if clients[number_client]["Hours"]>3:
            discount=clients[number_client]["Total"]*0.15
            clients_discounted+=1
            clients[number_client]["Total"]=clients[number_client]["Total"]-discount
        print("***RECEIPT***")
        for num_client,info in clients.items():
            for key,value in info.items():
                if num_client==number_client:
                    print(f"\t*{key} - {value}")
        end_day["Total clients"]=len(clients)
        end_day["Clients in A"]=clients_a
        end_day["Clients in S"]=clients_s
        end_day["Clients with discount"]=clients_discounted
        if clients[number_client]["Type"]=="A":
            income_a+=clients[number_client]["Total"]
        else:
            income_s+=clients[number_client]["Total"]
        if clients_a>=1:
            end_day["Average income per automatic car"]=income_a/clients_a
        if clients_s>=1:
            end_day["Average income per manual car"]=income_s/clients_s
        if input("Do you wish to continue? \n-Y for yes \n-N for no \n---> ").capitalize()=="N":
            print("***END OF DAY***")
            for data,info in end_day.items():
                print(f"\t*{data} - {info}")
            print("Have a great day!")
            break
main()