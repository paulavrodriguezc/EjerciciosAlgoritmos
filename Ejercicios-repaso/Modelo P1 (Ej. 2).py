def greet():
    print("¡Bienvenidos al sistema del Instituto Universitario!")
def get_info(num_aspirante,aspirantes):
    aspirantes[num_aspirante]={"Nombre":input("Por favor, introduzca el nombre completo del aspirante: ")}
    ci=input("Por favor, introduzca la cédula del aspirante (ej. 28327724): ")
    while not ci.isnumeric():
        print("Respuesta inválida.")
        ci=input("Por favor, introduzca la cédula del aspirante: ")
    promedio=input("Por favor, introduzca el promedio del aspirante: ")
    while not promedio.isnumeric():
        print("Respuesta inválida.")
        promedio=input("Por favor, introduzca el promedio del aspirante: ")
    aspirantes[num_aspirante]["CI"]=int(ci)
    aspirantes[num_aspirante]["Promedio"]=int(promedio)
    return aspirantes
def assign(aspirantes):
    for num_aspirantes,info_aspirante in aspirantes.items():
        for data,info in info_aspirante.items():
            if data=="Promedio":
                if info<=20 and info>=18:
                    aspirantes[num_aspirantes]["Status"]="Trimestre 2"
                    break
                elif info<18 and info>=12:
                    aspirantes[num_aspirantes]["Status"]="Trimestre 1"
                    break
                else:
                    aspirantes[num_aspirantes]["Status"]="Rechazado"
                    break
    return aspirantes 
def communicate(num_aspirante,aspirantes):
    for num_aspirantes,info_aspirante in aspirantes.items():
                if num_aspirante==num_aspirantes:
                    for data,info in info_aspirante.items():
                        if data=="Status":
                            if info=="Rechazado":
                                print(f"El aspirante ha sido rechazado.")
                            else:
                                print(f"El aspirante ha sido asignado a estudiar en el {info}.")    
def main():
    greet()
    num_aspirante=0
    aspirantes={}
    informacion_uni={"Total aspirantes":0,"Total alumnos":0,"Alumnos en T1":0,"Alumnos en T2":0,"Promedio T1":0,"Promedio T2":0,"Promedio general":0}
    accum=0
    accum_t1=0
    accum_t2=0
    while True:
        option=input("Seleccione la opción deseada: \n1. Registrar aspirante \n2. Ver estadísticas \n3. Salir \n---> ")
        while not option.isnumeric():
            print("Opción inválida.")
            option=input("Seleccione la opción deseada: \n1. Registrar aspirante \n2. Ver estadísticas \n3. Salir \n---> ")
        while int(option)<1 or int(option)>3:
            print("Opción inválida.")
            option=input("Seleccione la opción deseada: \n1. Registrar aspirante \n2. Ver estadísticas \n3. Salir \n---> ")
        if int(option)==1:
            num_aspirante+=1
            aspirantes=get_info(num_aspirante,aspirantes)
            aspirantes=assign(aspirantes)
            communicate(num_aspirante,aspirantes)
        elif int(option)==2:
            informacion_uni["Total aspirantes"]=num_aspirante                        
            for num_aspirantes,info_aspirante in aspirantes.items():
                for data,info in info_aspirante.items():
                    if data=="Status":
                        if info=="Trimestre 1":
                            informacion_uni["Total alumnos"]+=1
                            informacion_uni["Alumnos en T1"]+=1
                        elif info=="Trimestre 2":
                            informacion_uni["Total alumnos"]+=1
                            informacion_uni["Alumnos en T2"]+=1
            for num_aspirantes,info_aspirante in aspirantes.items():
                for data,info in info_aspirante.items():
                        if info=="Trimestre 1":
                            accum_t1+=info_aspirante.get("Promedio")
                            accum+=info_aspirante.get("Promedio")
                        elif info=="Trimestre 2":
                            accum_t2+=info_aspirante.get("Promedio")
                            accum+=info_aspirante.get("Promedio")
            if informacion_uni.get("Alumnos en T1")!=0:
                informacion_uni["Promedio T1"]=accum_t1/informacion_uni.get("Alumnos en T1")
            if informacion_uni.get("Alumnos en T2")!=0:
                informacion_uni["Promedio T2"]=accum_t2/informacion_uni.get("Alumnos en T2")
            informacion_uni["Promedio general"]=accum/informacion_uni.get("Total alumnos")
            print("Las estadísticas de este proceso de aplicación al Instituto Universitario son las siguientes: ")
            for key,value in informacion_uni.items():
                print(f"\t*{key} - {value}")
        else:
            print("¡Gracias por preferirnos!")
            break
main()