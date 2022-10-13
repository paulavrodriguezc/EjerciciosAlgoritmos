materias={}
evaluaciones_introducidas_mate={}
evaluaciones_introducidas_fisica={}
evaluaciones_introducidas_quimica={}
evaluaciones_introducidas_ingles={}
numero_evaluacion_mate=0
numero_evaluacion_fisica=0
numero_evaluacion_quimica=0
numero_evaluacion_ingles=0
puntos_accum_m=0
puntos_accum_f=0
puntos_accum_q=0
puntos_accum_i=0
while True:
    option=input("Por favor, escoja una opción dentro de las dadas: \n1. Registrar una evaluación \n2. Registrar una nota \n3. Ver evaluaciones hasta la fecha \n4. Salir \n--->")
    while not option.isnumeric():
        print("Caracter inválido.")
        option=input("Por favor, escoja una opción dentro de las dadas: \n1. Registrar una evaluación \n2. Registrar una nota \n3. Ver evaluaciones hasta la fecha \n4. Salir \n--->")
    while int(option)>4 or int(option)<1:
        print("Opción no disponible.")
        option=input("Por favor, escoja una opción dentro de las dadas: \n1. Registrar una evaluación \n2. Registrar una nota \n3. Ver evaluaciones hasta la fecha \n4. Salir \n--->")
    if int(option)==1:
        option_materia=input("Por favor, escoja una materia dentro de las dadas: \n1. Matemática \n2. Física \n3. Química \n4. Inglés \n--->")
        while not option_materia.isnumeric():
            print("Caracter inválido.")
            option_materia=input("Por favor, escoja una materia dentro de las dadas: \n1. Matemática \n2. Física \n3. Química \n4. Inglés \n--->")
        while int(option)>4 or int(option)<1:
            print("Opción no disponible.")
            option_materia=input("Por favor, escoja una materia dentro de las dadas: \n1. Matemática \n2. Física \n3. Química \n4. Inglés \n--->")
        if int(option_materia)==1:
            materia_elegida="Matemática"
            numero_evaluacion_mate+=1
            evaluaciones_introducidas_mate[numero_evaluacion_mate]={"evaluacion":input("Por favor introduzca el nombre de la evaluación: "),"fecha":input("Introduzca la fecha de la evaluación en el siguiente formato (dd/mm): "),"porcentaje":int(input("Por favor introduzca el peso de la evaluación (con valor numérico sin el %): ")),"nota":0, "puntos obtenidos":0}
            materias[materia_elegida]=evaluaciones_introducidas_mate
        elif int(option_materia)==2:
            materia_elegida="Física"
            numero_evaluacion_fisica+=1
            evaluaciones_introducidas_fisica[numero_evaluacion_fisica]={"evaluacion":input("Por favor introduzca el nombre de la evaluación: "),"fecha":input("Introduzca la fecha de la evaluación en el siguiente formato (dd/mm): "),"porcentaje":int(input("Por favor introduzca el peso de la evaluación (con valor numérico sin el %): ")),"nota":0, "puntos obtenidos":0}
            materias[materia_elegida]=evaluaciones_introducidas_fisica
        elif int(option_materia)==3:
            materia_elegida="Química"
            numero_evaluacion_quimica+=1
            evaluaciones_introducidas_quimica[numero_evaluacion_quimica]={"evaluacion":input("Por favor introduzca el nombre de la evaluación: "),"fecha":input("Introduzca la fecha de la evaluación en el siguiente formato (dd/mm): "),"porcentaje":int(input("Por favor introduzca el peso de la evaluación (con valor numérico sin el %): ")),"nota":0, "puntos obtenidos":0}
            materias[materia_elegida]=evaluaciones_introducidas_quimica
        else:
            materia_elegida="Inglés"
            numero_evaluacion_ingles+=1
            evaluaciones_introducidas_ingles[numero_evaluacion_ingles]={"evaluacion":input("Por favor introduzca el nombre de la evaluación: "),"fecha":input("Introduzca la fecha de la evaluación en el siguiente formato (dd/mm): "),"porcentaje":int(input("Por favor introduzca el peso de la evaluación (con valor numérico sin el %): ")),"nota":0, "puntos obtenidos":0}
            materias[materia_elegida]=evaluaciones_introducidas_ingles          
    elif int(option)==2:
        option_materia=input("Por favor, escoja una materia dentro de las dadas: \n1. Matemática \n2. Física \n3. Química \n4. Inglés \n--->")
        while not option_materia.isnumeric():
            print("Caracter inválido.")
            option_materia=input("Por favor, escoja una materia dentro de las dadas: \n1. Matemática \n2. Física \n3. Química \n4. Inglés \n--->")
        while int(option)>4 or int(option)<1:
            print("Opción no disponible.")
            option_materia=input("Por favor, escoja una materia dentro de las dadas: \n1. Matemática \n2. Física \n3. Química \n4. Inglés \n--->")
        if int(option_materia)==1:
            option_materia="Matemática"
        elif int(option_materia)==2:
            option_materia="Física"
        elif int(option_materia)==3:
            option_materia="Química"
        else:
            option_materia="Inglés"
        for materia,info_materias in materias.items():
            if materia==option_materia:
                for num_evaluacion,info_evaluacion in info_materias.items():
                    print(f"*{num_evaluacion} - {info_evaluacion}")
        evaluacion_agregar=int(input("Seleccione el número de la evaluación de la que desea agregar su calificación: "))
        for materia,info_materias in materias.items():
            if materia==option_materia:
                for num_evaluacion,info_evaluacion in info_materias.items():
                        if evaluacion_agregar==num_evaluacion:
                            for data,info in info_evaluacion.items():
                                info_evaluacion["nota"]=int(input("Por favor introduzca la calificación obtenida: "))
                                info_evaluacion["puntos obtenidos"]=(info_evaluacion.get("porcentaje")/100)*info_evaluacion.get("nota")
                                if materia=="Matemática":
                                    puntos_accum_m+=info_evaluacion.get("puntos obtenidos")
                                    if puntos_accum_m>=10:
                                        print(f"¡Ya has aprobado {materia.lower()}!\n")
                                    else:
                                        print(f"Todavía no has aprobado {materia.lower()}.\n")
                                elif materia=="Física":
                                    puntos_accum_f+=info_evaluacion.get("puntos obtenidos")
                                    if puntos_accum_f>=10:
                                        print(f"¡Ya has aprobado {materia.lower()}!\n")
                                    else:
                                        print(f"Todavía no has aprobado {materia.lower()}.\n")
                                elif materia=="Química":
                                    puntos_accum_q+=info_evaluacion.get("puntos obtenidos")
                                    if puntos_accum_q>=10:
                                        print(f"¡Ya has aprobado {materia.lower()}!\n")
                                    else:
                                        print(f"Todavía no has aprobado {materia.lower()}.\n")
                                else:
                                    puntos_accum_i+=info_evaluacion.get("puntos obtenidos")
                                    if puntos_accum_i>=10:
                                        print(f"¡Ya has aprobado {materia.lower()}!\n")
                                    else:
                                        print(f"Todavía no has aprobado {materia.lower()}.\n")
                                break
    elif int(option)==3:
        for materia,info_materias in materias.items():
            print(f"* {materia}: ")
            for num_evaluacion,info_evaluacion in info_materias.items():
                    print(f"\t* {num_evaluacion}: ")
                    for data,info in info_evaluacion.items():
                        print(f"\t\t* {data.title()} - {info}")
    else:
        for materia,info_materias in materias.items():
            print(f"* {materia}: ")
            if materia=="Matemática":
                print(f"\tTu nota final es {puntos_accum_m} puntos.")
                if puntos_accum_m>=10:
                    print(f"\t¡Felicitaciones! Has aprobado {materia.lower()}.\n")
                else:
                   print(f"\tNo has aprobado {materia.lower()}.\n") 
            elif materia=="Física":
                print(f"\tTu nota final es {puntos_accum_f} puntos.")
                if puntos_accum_f>=10:
                    print(f"\t¡Felicitaciones! Has aprobado {materia.lower()}.\n")
                else:
                   print(f"\tNo has aprobado {materia.lower()}.\n") 
            elif materia=="Química":
                print(f"\tTu nota final es {puntos_accum_q} puntos.")
                if puntos_accum_q>=10:
                    print(f"\t¡Felicitaciones! Has aprobado {materia.lower()}.\n")
                else:
                   print(f"\tNo has aprobado {materia.lower()}.\n") 
            else:
                print(f"\tTu nota final es {puntos_accum_i} puntos.")
                if puntos_accum_i>=10:
                    print(f"\t¡Felicitaciones! Has aprobado {materia.lower()}.\n")
                else:
                   print(f"\tNo has aprobado {materia.lower()}.\n") 
        print("Gracias por usar nuestra plataforma.")
        break