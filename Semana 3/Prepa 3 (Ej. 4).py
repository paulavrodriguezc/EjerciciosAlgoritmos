infraction={1:{"name":"Choque", "cost":50}, 2:{"name":"Semáforo", "cost":30}, 3:{"name":"Falta de documentos", "cost":100}}
officers={1:{"name":"Luis","last name":"Bello","CI":13452224}, 2:{"name":"José","last name":"Quevedo","CI":44235611}, 3:{"name":"Antonio","last name":"Guerra","CI":12345678}}
option=input("Por favor, introduzca una de las siguientes opciones: \n1. Ingresar un infractor a la base de datos. \n2. Eliminar un infractor de la base de datos. \n3. Mostrar multas registradas en el sistema. \n4. Salir del sistema. \n->")
data_base={}
while not option.isnumeric():
    print("Opción inválida. Por favor, introduzca un valor numérico dentro de las opciones dadas.")
    option=input("Por favor, introduzca una de las siguientes opciones: \n1. Ingresar un infractor a la base de datos. \n2. Eliminar un infractor de la base de datos. \n3. Mostrar multas registradas en el sistema. \n4. Salir del sistema. \n->")
    if int(option)>4 or int(option)<1:
        print("Opción inválida. Por favor, introduzca una opción entre las dadas.")
        option=input("Por favor, introduzca una de las siguientes opciones: \n1. Ingresar un infractor a la base de datos. \n2. Eliminar un infractor de la base de datos. \n3. Mostrar multas registradas en el sistema. \n4. Salir del sistema. \n->")
if int(option)==1:
    name=input("Por favor, introduzca el nombre del infractor: ")
    data_base["Nombre del infractor"]=name
    last_name=input("Por favor, introduzca el apellido del infractor: ")
    data_base["Apellido del infractor"]=last_name
    ci=input("Por favor, introduzca el número de cédula del infractor. Ej: 25648971. \n->")
    data_base["Cédula del infractor"]=ci
    officer_inv=input("Por favor, introduzca el oficial encargado: \n1. Luis Bello \n2. José Quevedo \n3. Antonio Guerra \n->")
    while not option.isnumeric():
        print("Opción inválida. Por favor, introduzca un valor numérico dentro de las opciones dadas.")
        officer_inv=input("Por favor, introduzca el oficial encargado: \n1. Luis Bello \n2.José Quevedo \n3. Antonio Guerra \n->")
        if int(option)>3 or int(option)<1:
            print("Opción inválida. Por favor, introduzca una opción entre las dadas.")
            officer_inv=input("Por favor, introduzca el oficial encargado: \n1. Luis Bello \n2.José Quevedo \n3. Antonio Guerra \n->")
    if int(officer_inv)==1:
        data_base[3]=officers[1]
    elif int(officer_inv)==2:
        data_base[3]=officers[2]
    else:
        data_base[3]=officers[3]
    infraction_inv=input("Por favor, introduzca el tipo de infracción cometida: \n1. Choque \n2. Semáforo \n3. Falta de documentos \n->")
    if int(infraction_inv)==1:
        data_base[4]=infraction[1]
    elif int(infraction_inv)==2:
        data_base[4]=infraction[2]
    else:
        data_base[4]=infraction[3]