type=int(input("Please enter a valid option: \n1. Vegetarian.\n2. Non-vegetarian.\n->"))
if type==1:
    ingredient=int(input("Please choose the ingredient of your liking: \n1. Bell pepper.\n2. Tofu.\n->"))
    if ingredient==1:
        ingredient="bell pepper"
    if ingredient==2:
        ingredient="tofu"
    print(f"The ordered pizza is vegetarian and its ingredients are tomato, mozzarella and {ingredient}.")
elif type==2:
    ingredient=int(input("Please choose the ingredient of your liking: \n1. Pepperoni.\n2. Ham.\n3. Salmon.\n->"))
    if ingredient==1:
        ingredient="pepperoni"
    elif ingredient==2:
        ingredient="ham"
    else:
        ingredient="salmon"
    print(f"The ordered pizza is non-vegetarian and its ingredients are tomato, mozzarella and {ingredient}.")
else:
    print("Invalid option.")