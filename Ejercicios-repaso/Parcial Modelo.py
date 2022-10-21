def greet_and_menu():
    print("¡Bienvenido a Samán Labs!")
    option=input("Por favor, seleccione una de las opciones dadas: \n1. Ver inventario \n2. Registrar compra \n3. Salir \n---> ")
    while not option.isnumeric() or not int(option) in [1,2,3]:
        print("Opción inválida.")
        option=input("Por favor, seleccione una de las opciones dadas: \n1. Ver inventario \n2. Registrar compra \n3. Salir \n---> ")
    return int(option)
def print_inventory(medications):
    print("Nuestro inventario actual es el siguiente: ")
    for prescripcion,info in medications.items():
        print(f"\t*{prescripcion.capitalize()}:")
        for types,data in info.items():
            print(f"\t\t*{types.capitalize()}:")
            for system_selected,products in data.items():
                print(f"\t\t\t*{system_selected.capitalize()}:")
                for medicine in products:
                    for key,value in medicine.items():
                        print(f"\t\t\t\t\t*{key.capitalize()} - {value}")
                    print("\n")
def register_purchase(clients,medications):
    client={}
    client["name"]=input("Por favor, introduzca su nombre y apellido: ")
    id=input("Por favor introduzca su número de cédula (ej. 28327724): ")
    while not id.isnumeric():
        print("Caractéres inválidos.")
        id=input("Por favor introduzca su número de cédula (ej. 28327724): ")
    client["id"]=int(id)
    print_inventory(medications)
    product_id=input("Por favor introduzca el número de identificación del producto: ")
    while not product_id.isnumeric():
        print("Caractéres inválidos.")
        product_id=input("Por favor introduzca el número de identificación del producto: ")
    product_confirmation=check_product(product_id,medications)
    if product_confirmation:
        client["product"]=int(product_id)
    else:
        print("Product not found.")
        while product_confirmation==False:
            product_id=input("Por favor introduzca el número de identificación del producto: ")
            product_confirmation=check_product(product_id,medications)
        client["product"]=int(product_id)
    get_total(medications,product_id,client)
    clients.append(client)
    print_receipt(client)
    return clients
def check_product(product_id,medications):
    product_confirmation=False
    for prescripcion,info in medications.items():
        for types,data in info.items():
            for system_selected,products in data.items():
                for medicine in products:
                    for key,value in medicine.items():
                        if key=="id" and value==int(product_id):
                            product_confirmation=True
    return product_confirmation
def get_total(product_id,medications,client):
    for prescripcion,info in medications.items():
        for types,data in info.items():
            for system_selected,products in data.items():
                for medicine in products:
                    for key,value in medicine.items():
                        if key=="id" and value==int(product_id):
                            total=medicine["price"]
    client["total"]=int(total)
def print_receipt(client):
    print("***RECIBO***")
    for key,value in client.items():
        print(f"*{key.capitalize()} - {value}")                  
def main():
    medications = {
            "prescription": {
                "antibiotics": {
                    "skin": [
                        {
                            "id": 1,
                            "name": "Clindamicine",
                            "price": 300
                        },
                        {
                            "id": 2,
                            "name": "Cefadroxil",
                            "price": 350
                        },
                        {
                            "id": 3,
                            "name": "Amoxicillin",
                            "price": 320
                        }
                    ],
                    "respiratory-system":[
                        {
                            "id": 4,
                            "name": "Citromicine",
                            "price": 380
                        },
                        {
                            "id": 5,
                            "name": "Levofloxacine",
                            "price": 125
                        },
                        {
                            "id": 6,
                            "name": "Azitromicine",
                            "price": 740
                        }
                    ]
                },
                "analgesic": {
                    "anti-inflammatories": [
                        {
                            "id": 7,
                            "name": "HYDROCODONE-IBUPROFEN",
                            "price": 150
                        },
                        {
                            "id": 8,
                            "name": "IBUDONE",
                            "price": 180
                        }
                    ]
                }
            },
            "non-prescription": {
                "analgesic": {
                    "general": [
                        {
                            "id": 9,
                            "name": "Acetaminophen",
                            "price": 15
                        },
                        {
                            "id": 10,
                            "name": "Ibuprofen",
                            "price": 20
                        }
                    ]
                },
                "antihistamine": {
                    "antiallergic": [
                        {
                            "id": 11,
                            "name": "Loratadine",
                            "price": 12
                        },
                        {
                            "id": 12,
                            "name": "Desler M",
                            "price": 8
                        },
                        {
                            "id": 13,
                            "name": "Allegra",
                            "price": 21
                        },
                        {
                            "id": 14,
                            "name": "Fexofenadine",
                            "price": 18
                        }
                    ]
                }
            }
        }
    clients=[]
    while True:
        option_selected=greet_and_menu()
        if option_selected==1:
            print_inventory(medications)
        elif option_selected==2:
            clients=register_purchase(clients,medications)
        else:
            print("¡Gracias por preferirnos! Que tengas un buen día.")
            break
main()