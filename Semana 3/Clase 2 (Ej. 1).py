currency_dict={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
selection=input("Please select a currency: ").capitalize()
print(currency_dict.get(selection, "Currency NOT found."))