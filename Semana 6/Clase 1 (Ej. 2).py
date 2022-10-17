def get_wealth(accounts):
    max_wealth=0
    for lista in accounts:
        if sum(lista)>max_wealth:
            max_wealth=sum(lista)
    return max_wealth
def main():
    accounts=[
        [1,2,3],
        [1,2,3]
    ]
    wealth=get_wealth(accounts)
    print(f"The maximum wealth is {wealth}.")
main()