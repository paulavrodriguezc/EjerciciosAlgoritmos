def prime(rif):
    count=0
    number=int(rif[-1])
    for x in range(1,number+1):
        if number%x==0:
            count+=1
    if count==2 and number>1:
        return True
    else:
        return False
def main():
    products={
        "Q":{
            "description": "Químico",
            "cost": 1000
        },
        "F":{
            "description": "Farmacéutico",
            "cost": 2500
        },
        "B":{
            "description": "Biológico",
            "cost": 4000
        }
    }
    rif=input("Please enter your RIF: ")
    product_code=input("Please select the type of product you wish to purchase: \n1. Químico \2. Farmacéutico \3. Biológico \n---> ")
    payment_method=input("Please select the method of payment: \nC. Contado \nR. Crédito \n---> ")
    gross_amount=products.get(product_code.get("cost"))
    discount=0
    recharge=0
    tax=0
    clients_q=0
    clients_f=0
    clients_b=0
    discount_q=0
    discount_f=0
    discount_b=0
    max_purchase=0
    rif_max_purchase=0
    total_day=0
    while True:
        if payment_method=="C":
            discount+=gross_amount*0.03
        if gross_amount%2==0:
            discount+=gross_amount*0.02
        if prime(rif):
            discount+=gross_amount*0.05
        if payment_method=="R":
            recharge+=gross_amount*0.10
        if product_code!="F":
            tax+=gross_amount*0.12
        total=gross_amount+recharge-discount+tax
        print("***RECEIPT***")
        print(f"\tRIF: {rif}")
        print("\tProduct: ", products.get(product_code.get("description")))
        print(f"\tPayment method: {payment_method}")
        print(f"\Discounted: {discount}")
        print(f"\tTaxes: {tax}")
        print(f"\TOTAL: {total}")
        total_day+=total
        if product_code=="F":
            clients_q+=1
            discount_f+=discount
        elif product_code=="Q":
            clients_q+=1
            discount_q+=discount
        else:
            clients_b+=1
            discount_b+=discount
        if total>max_purchase:
            rif_max_purchase=rif
            max_purchase=total
        if input("Do you wish to continue: \nY for yes \nN for no \n---> ").capitalize()=="N":
            break
    print("***END OF DAY***")
    print(f"\tClients Q: {clients_q}")
    print(f"\tClients F: {clients_f}")
    print(f"\tClients B: {clients_b}")
    print(f"\tDiscounts for Q: {discount_q}")
    print(f"\tDiscounts for F: {discount_f}")
    print(f"\tDiscounts for B: {discount_b}")
    print(f"\tMax purchase for the day: {max_purchase}")
    print(f"\tRIF of the max purchase for the day: {rif_max_purchase}")
    print(f"\tTOTAL: {total_day}")
main()