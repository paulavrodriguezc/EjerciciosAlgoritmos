translate_dict={}
inicial_info=input("Por favor, introduzca palabras en inglés seguidas de su traducción al español separadas por comas de la siguiente manera: 'palabra:traducción'\n ----> ")
couple_words=inicial_info.split(",")
print(couple_words)
for i in couple_words:
    values_list=i.split(":")
    translate_key=values_list[0]
    translate_values=values_list[1]
    translate_dict[translate_key]=translate_values
print(translate_dict)