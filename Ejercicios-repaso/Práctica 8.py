infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}
officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}
db={}
number_infractor=0
while True:
    option=input("Seleccione una acción a realizar: \n1. Ingresar multa e infractor al sistema \n2. Eliminar multa e infractor del sistema \n3. Mostrar multas e infractores existentes \n4. Salir \n--->")
    while not option.isnumeric():
        print("Opción inválida.")
        option=input("Seleccione una acción a realizar: \n1. Ingresar multa e infractor al sistema \n2. Eliminar multa e infractor del sistema \3. Mostrar multas e infractores existentes \n4. Salir \n--->")
    while int(option)>4 or int(option)<1:
        print("Opción no existente.")
        option=input("Seleccione una acción a realizar: \n1. Ingresar multa e infractor al sistema \n2. Eliminar multa e infractor del sistema \3. Mostrar multas e infractores existentes \n4. Salir \n--->")
    if int(option)==1:
        number_infractor+=1
        infractor={"name": input("Introduzca el nombre completo del infractor: "), "ci":int(input("Introduzca la cédula del infractor: ")), "infracción":0, "oficial encargado":0}
        infraction_commited=input("Seleccione la infracción cometida: \n1. Choque \n2. Pasó en semáforo en rojo \n3. Falta de documentos \n--->")
        while not infraction_commited.isnumeric():
            print("Opción inválida.")
            infraction_commited=input("Seleccione la infracción cometida: \n1. Choque \n2. Pasó en semáforo en rojo \n3. Falta de documentos \n--->")
        while int(infraction_commited)>3 or int(infraction_commited)<1:
            print("Opción no existente.")
            infraction_commited=input("Seleccione la infracción cometida: \n1. Choque \n2. Pasó en semáforo en rojo \n3. Falta de documentos \n--->")
        infraction_commited=int(infraction_commited)
        for number_infraction,info in infraction.items():
            if number_infraction==infraction_commited:
                infractor["infracción"]=info
        officer_charge=input("Seleccione el oficial encargado: \n1. Luis Bello \n2. José Quevedo \n3. Antonio Guerra \n--->")
        while not officer_charge.isnumeric():
            print("Opción inválida.")
            officer_charge=input("Seleccione el oficial encargado: \n1. Luis Bello \n2. José Quevedo \n3. Antonio Guerra \n--->")
        while int(officer_charge)>3 or int(officer_charge)<1:
            print("Opción no existente.")
            officer_charge=input("Seleccione el oficial encargado: \n1. Luis Bello \n2. José Quevedo \n3. Antonio Guerra \n--->")
        officer_charge=int(officer_charge)
        for number_officer,info in officers.items():
            if number_officer==officer_charge:
                infractor["oficial encargado"]=info
        db[number_infractor]=infractor
        print(db)
    elif int(option)==2:
        ci_infractor=int(input("Por favor, introduzca la cédula del infractor: "))
        key_x=0
        for number_infract,info_infract in db.items():
                if info_infract["ci"]==ci_infractor:
                    key_x=number_infract
        db.pop(key_x)
    elif int(option)==3:
        for number_infr,info in db.items():
            for data,info in info.items():
                print("\n")
                print(f"* {data} - {info}")
    else:
        print("Gracias.")
        break