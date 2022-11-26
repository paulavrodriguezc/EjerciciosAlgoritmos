import random
def nervioso(cards: list, count=0):
    if len(cards)==0:
        print("You have lost the game.")
    else:
        count+=1
        card_selected=random.choice(cards)
        print(f"The count is {count} and the card is {card_selected}.")
        if count!=card_selected:
            cards.remove(card_selected)
            nervioso(cards,count)
        else:
            print("You have won the game! The count number and the card in question are the same.")
def main():
    cards=[2,3,4,5,6,7,8,9,10]
    nervioso(cards)
main()