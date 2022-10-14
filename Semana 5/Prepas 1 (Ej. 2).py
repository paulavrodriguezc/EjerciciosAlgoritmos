import random
def tickets_generated():
    quantity=input("Please enter the number of tickets you wish to have in the lottery: ")
    while True:
        try:
            quantity=int(quantity)
            if quantity==0:
                raise Exception
            break
        except:
            print("Invalid input.")
    return quantity
def ticket_generator(quantity):
    tickets=[]
    while len(tickets)<quantity:
        ticket=random.randint(10000000,99999999)
        # el randint elige números al azar entre el rango dado, el cual va desde el menor número con 8 dígitos hasta el mayor
        if not ticket in tickets:
            tickets.append(ticket)
    return tickets
def winner_ticket(tickets):
    return random.choice(tickets)
    # choice elige un elemento al azar de un rango dado (en este caso, la lista de tickets)
def main():
    quantity=tickets_generated()
    tickets=ticket_generator(quantity)
    print(f"The tickets numbers are: {tickets}.")
    winner=winner_ticket(tickets)
    print(f"The winner is the ticket number {winner}.")
main()