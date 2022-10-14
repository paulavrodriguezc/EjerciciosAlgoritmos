vehiculos={'S':
          [{'Marca': 'Toyota', 'Modelo': "Corolla", 'Año': 2005, 'Placa': 'AA521PB'},
          {'Marca': 'Chevrolet', 'Modelo': "Cruze", 'Año': 2011, 'Placa': 'AP203KS'} ],
          'A': 
          [{"Marca": 'Volkswagen', 'Modelo': "Fox", 'Año': 2009, 'Placa': 'CG458LP'}]}
db={}
num_alumno=0
while True:
    option=input("Por favor, seleccione una opción de las dadas: \n1. Registrar un alumno \n2. Salir del sistema \n--->")
    while not option.isnumeric():
        print("Caracter inválido.")
        option=input("Por favor, seleccione una opción de las dadas: \n1. Registrar un alumno \n2. Salir del sistema \n--->")
    while int(option)<1 or int(option)>2:
        print("Opción no existente.")
        option=input("Por favor, seleccione una opción de las dadas: \n1. Registrar un alumno \n2. Salir del sistema \n--->")
    if int(option)==1:
        num_alumno+=1
        db[num_alumno]={"Nombre completo":input("Por favor, introduzca el nombre completo del alumno: "),"Cédula":input("Por favor, introduzca el número de cédula del alumno: "),"Horas":int(input("Por favor, introduzca la cantidad de horas que cursará el alumno: ")),"Placa":0,"Total":0}
        tipo_escogido=input("Por favor, seleccione el tipo de vehículo que el alumno desea conducir: \nS: Sincrónico \nA: Automático \n--->").capitalize()
        for tipo_vehiculo, informacion_tipo in vehiculos.items():
            if tipo_escogido==tipo_vehiculo:
                if tipo_vehiculo=="A":
                        print("Su vehículo ya ha sido asignado.")
                        for vehiculo in informacion_tipo:
                            for data,info in vehiculo.items():
                                db[num_alumno]["Tarifa por hora"]=25
                                db[num_alumno]["Placa"]=vehiculo.get("Placa")
                                db[num_alumno]["Total"]=db.get(num_alumno).get("Horas")*db.get(num_alumno).get("Tarifa por hora")
                else:
                    db[num_alumno]["Tarifa por hora"]=15
                    db[num_alumno]["Total"]=db.get(num_alumno).get("Horas")*db.get(num_alumno).get("Tarifa por hora")
                    print("Los vehículos disponibles son:")
                    for vehiculo in informacion_tipo:
                        print(f"* {vehiculo}")
                    vehiculo_elegido=input("Seleccione el vehículo a asignar (1 o 2): ")
                    while not vehiculo_elegido.isnumeric():
                        print("Caracter inválido.")
                        vehiculo_elegido=input("Seleccione el vehículo a asignar (1 o 2): ")
                    while int(option)<1 or int(option)>2:
                        print("Opción no existente.")
                        vehiculo_elegido=input("Seleccione el vehículo a asignar (1 o 2): ")
                    for vehiculo in informacion_tipo:
                        for data,info in vehiculo.items():
                            if int(vehiculo_elegido)==1:
                                db[num_alumno]["Placa"]=informacion_tipo[0].get("Placa")
                            else:
                                db[num_alumno]["Placa"]=informacion_tipo[1].get("Placa")
        if db[num_alumno]["Horas"]>3:
            descuento=0.1
            db[num_alumno]["Total"]=db[num_alumno]["Total"]-(db[num_alumno]["Total"]*descuento)
        print("***RECIBO DE PAGO***")
        for num_cliente,info_cliente in db.items():
            if num_alumno==num_cliente:
                for dato,informacion in info_cliente.items():
                    if dato!="Tarifa por hora":
                        print(f"- {dato}: {informacion}")
    else:
        final_dia={"Total de horas de clase impartidas":0,"Alumnos en el vehículo de placa AA521PB":0,"Alumnos en el vehículo de placa AP203KS":0,"Alumnos en el vehículo de placa CG458LP":0,"Total facturado":0}
        for num_cliente,info_cliente in db.items():
            final_dia["Total de horas de clase impartidas"]+=db[num_cliente]["Horas"]
            final_dia["Total facturado"]+=db[num_cliente]["Total"]
            for dato,informacion in info_cliente.items():
                if dato=="Placa":
                    if informacion=="AA521PB":
                        final_dia["Alumnos en el vehículo de placa AA521PB"]+=1
                    elif informacion=="AP203KS":
                        final_dia["Alumnos en el vehículo de placa AP203KS"]+=1
                    else:
                        final_dia["Alumnos en el vehículo de placa CG458LP"]+=1
        print("***CIERRE DE CAJA***")
        for total,numero in final_dia.items():
            if numero!=0:
                print(f"* {total} - {numero}")
        break