def show_inventory(vinyls):
    for number_vinyl,info_vinyl in vinyls.items():
                print(f"Vinyl ID: {number_vinyl}: ")
                for data,info in info_vinyl.items():
                    print(f"\t*{data.title()}: {info}")
def main():
    vinyls = {
        '1': { 'name': 'Cuando Los Acéfalos Predominan',
                'author': 'Rawayana',
                'release year': '2021',
                'stock': 1000,
                'sold': 0,
                'price': 10,
            },
        '2': { 'name': 'Notes on a Conditional Form',
                'author': 'The 1975',
                'release year': '2020',
                'stock': 1200,
                'sold': 0,
                'price': 20,
            },
        '3': { 'name': 'Call Me If You Get Lost',
                'author': 'Tyler, the Creator',
                'release year': '2021',
                'stock': 900,
                'sold': 0,
                'price': 30,
            },
        '4': { 'name': 'El Mal Querer',
                'author': 'Rosalía',
                'release year': '2018',
                'stock': 980,
                'sold': 0,
                'price': 40,
            },
        '5': { 'name': 'The Dark Side of the Moon',
                'author': 'Pink Floyd',
                'release year': '1973',
                'stock': 500,
                'sold': 0,
                'price': 50,
            },
        }
    clients={}
    cash_desk={"Total billed":0}
    number_client=0
    purchases=0
    while True:
        option=input("Please select one option from the given: \n1. See inventory \n2. Register a purchase \n3. Exit \n---> ")
        while not option.isnumeric() or int(option)<1 or int(option)>3:
            print("Invalid input.")
            option=input("Please select one option from the given: \n1. See inventory \n2. Register a purchase \n3. Exit \n---> ")
        if int(option)==1:
            option_inventory=input("Please select one option from the given: \n1. See inventory \n2. Look for a specific vinyl and its information \n---> ")
            while not option_inventory.isnumeric() or not int(option_inventory) in [1,2]:
                print("Invalid input.")
                option_inventory=input("Please select one option from the given: \n1. See inventory \n2. Look for a specific vinyl and its information \n---> ")
            if int(option_inventory)==1:
                show_inventory(vinyls)
            else:
                vinyl_search=input("Please enter the name of the vinyl: ").lower()
                is_in=True
                print("Your search result is as follows:")
                for number_vinyl,info_vinyl in vinyls.items():
                    if vinyl_search==info_vinyl["name"].lower():
                        is_in=True
                        print(f"Vinyl ID: {number_vinyl}: ")
                        for data,info in info_vinyl.items():
                            print(f"\t*{data.title()}: {info}")
                        break
                    else:
                        is_in=False
                if is_in==False:
                    print("The vinyl is not available.")
        elif int(option)==2:
            number_client+=1
            purchases+=1
            cash_desk["Total purchases"]=purchases
            clients[number_client]={"Name":input("Please enter the full name of the client: ")}
            id=input("Please enter the ID number of the client (e.g: 28327724): ") 
            while not id.isnumeric():
                print("Invalid input.")
                id=input("Please enter the ID number of the client (e.g: 28327724): ")
            clients[number_client]["ID"]=int(id)
            show_inventory(vinyls)
            vinyl_selected=input("Please enter the ID of the vinyl purchased: ")
            while not vinyl_selected.isnumeric() or int(vinyl_selected)<1 or int(vinyl_selected)>5:
                print("Invalid input.")
                vinyl_selected=input("Please enter the ID of the vinyl purchased: ")
            clients[number_client]["ID vinyl purchased"]=int(vinyl_selected)
            print("***RECEIPT***")
            for number,info_client in clients.items():
                if number_client==number:
                    for data,info in info_client.items():
                        print(f"\t*{data}: {info}")
            for number_vinyl,info_vinyl in vinyls.items():
                for data,info in info_vinyl.items():
                    if vinyl_selected==number_vinyl and data=="price":
                        print(f"\tTOTAL: ${info}") 
                        cash_desk["Total billed"]+=info
            for total,value in cash_desk.items():
                if total=="Total billed":
                    print(f"*{total}: ${value}")
                else:
                    print(f"*{total}: {value}")
            for number_vinyl,info_vinyl in vinyls.items():
                    if vinyl_selected==number_vinyl:
                        vinyls[vinyl_selected]["stock"]-=1
                        vinyls[vinyl_selected]["sold"]+=1
        else:
            print("Have a nice day!")
            break
main()