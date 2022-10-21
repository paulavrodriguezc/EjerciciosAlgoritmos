def calculator(accounts:list):
    wealthiest=0
    index_wealthiest=0
    for cliente in accounts:
        total_client=sum(cliente)
        if total_client>wealthiest:
            wealthiest=total_client
            index_wealthiest=accounts.index(cliente)
    print(f"The client with the most money in their accounts is the one with index {index_wealthiest} and has a total of ${wealthiest}.")
# puedes definir la clase de variable que vas a tomar en la función poniendo "variable": clase (int, str, float, etc) 
# puedes definir la clase de dato retornado: al finalizar el paréntesis de los parámetros: -> clase (int, str, float, list, etc)
def main():
    accounts=[]
    more_clients=True
    while more_clients:
        more_accounts=True
        client=[]
        while more_accounts:
            account_total=input("Please enter the total of the account: ")
            while not account_total.isnumeric():
                account_total=input("Invalid input, you must enter a number. Please enter the total of the account: ")
            client.append(int(account_total))
            option=input("Do you wish to add another account to this client? \n-1 for yes \n-2 for no \n---> ")
            while not option in ["1","2"]:
                option=input("Invalid option. Do you wish to add another account to this client? \n-1 for yes \n-2 for no \n---> ")
            if option=="2":
                more_accounts=False
        option_2=input("Do you wish to add another client? \n-1 for yes \n-2 for no \n---> ")
        while not option_2 in ["1","2"]:
                option=input("Invalid option. Do you wish to add another client? \n-1 for yes \n-2 for no \n---> ")
        if option_2=="2":
            more_clients=False
        accounts.append(client)
    calculator(accounts)
main()