from Products import Product
from Purchases import Purchase
def validate_option(option: str):
    while not option.isnumeric() or not option in ["1","2","3"]:
        option=input("Opción inválida. Seleccione una de las opciones dadas: \n1. Módulo administrativo \n2. Módulo de distribución de inventario \n3. Salir del sistema \n---> ")
    return int(option)
def greet_and_menu():
    print("¡Bienvenido a nuestro sistema!")
    option=input("Seleccione una de las opciones dadas: \n1. Módulo administrativo \n2. Módulo de distribución de inventario \n3. Salir del sistema \n---> ")
    option=validate_option(option)
    return option
def transform_products(products: list, products_updated: list):
    for product in products:
        for key,value in product.items():
            if key=="id":
                id=value
            elif key=="name":
                name=value
            elif key=="type":
                type=value
            elif key=="stock":
                stock=value
            else: 
                colors=value
        product=Product(id,name,type,stock,colors)
        products_updated.append(product)
    return products_updated
def print_stock(products_updated: list):
    for product in products_updated:
        product.print_information()
def transform_purchases(vendor_1: list, vendor_2: list, purchases: list):
    for purchase in vendor_1:
        for key,value in purchase.items():
            if key=="product_id":
                product_id=value
            elif key=="customer_id":
                customer_id=value
            elif key=="amnt":
                amnt=value
        purchase=Purchase(product_id,customer_id,amnt)
        purchases.append(purchase)
    for purchase in vendor_2:
        for key,value in purchase.items():
            if key=="product_id":
                product_id=value
            elif key=="customer_id":
                customer_id=value
            elif key=="amnt":
                amnt=value
        purchase=Purchase(product_id,customer_id,amnt)
        purchases.append(purchase)
    return purchases
def order_list(purchases: list):
    for x in range(len(purchases)):
        for y in range(x+1,len(purchases)):
            if purchases[y].amount<purchases[x].amount:
                purchases[x],purchases[y]=purchases[y],purchases[x]
def update_stock(purchases:list, products_updated: list):
    for product in products_updated:
        for purchase in purchases:
            if purchase.product_id==product.id:
                product.stock=product.stock-purchase.amount
    return products_updated
def main():
    products = [{"id": 1, "name": "Rose", "type": "flower", "stock": 160, "colors": ["red", "white", "pink"]},
{ "id": 2, "name": "Tulip", "type": "flower", "stock": 34, "colors": ["white", "yellow"] },
{ "id": 3, "name": "Sunflower seeds", "type": "seeds", "stock": 50 },
{ "id": 4, "name": "Sunflower", "type": "flower", "stock": 77, "colors": ["yellow"] },
{ "id": 5, "name": "Lavender seeds", "type": "seeds", "stock": 100, "colors": ["purple"] },
{ "id": 6, "name": "Carnation", "type": "flower", "stock": 89, "colors": ["yellow", "burgundy", "purple", "pink", "red", "white"] },
]
    vendor_1 = [
    { "product_id": 5, "customer_id": 333, "amnt": 1 },
    { "product_id": 5, "customer_id": 1010, "amnt": 2 },
    { "product_id": 3, "customer_id": 1111, "amnt": 3 },
    { "product_id": 2, "customer_id": 222, "amnt": 6 },
    { "product_id": 6, "customer_id": 444, "amnt": 7 },
    { "product_id": 1, "customer_id": 1111, "amnt": 20 },
    ]
    vendor_2 = [
    { "product_id": 6, "customer_id": 888, "amnt": 10 },
    { "product_id": 1, "customer_id": 123, "amnt": 5 },
    { "product_id": 2, "customer_id": 321, "amnt": 4 },
    { "product_id": 4, "customer_id": 555, "amnt": 2 },
    { "product_id": 1, "customer_id": 777, "amnt": 1 },
    ]
    products_updated=[]
    purchases=[]
    option=greet_and_menu()
    products_updated=transform_products(products, products_updated)
    if option==1:
        print(f"The inventory available is as follows: ")
        print_stock(products_updated)
    if option==2:
        purchases=transform_purchases(vendor_1, vendor_2, purchases)
        order_list(purchases)
        update_stock(purchases, products_updated)
        print_stock(products_updated)
    else:
        print("¡Gracias por preferirnos! Tenga un feliz día.")
main()