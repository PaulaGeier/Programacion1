print("Ingresar dia de las semana y fecha en el siguiente formato:")
fecha=input('dia, DD/MM:')
dia_sem=str(fecha[0:fecha.find(',')])
dia=int(fecha[fecha.find(' ')+1:fecha.find('/')])
mes=int(fecha[fecha.find('/')+1:])
dia_sem_minus=dia_sem.lower()

if dia_sem_minus != "lunes" and dia_sem_minus != "martes" and dia_sem_minus != "miercoles" and dia_sem_minus != "jueves" and dia_sem_minus != "viernes" or dia>31 or  dia<1 or mes>12 or mes<1:
    print("DATOS INGRESADOS INCORRECTOS") 
elif dia_sem_minus=="lunes" or dia_sem_minus=="martes" or dia_sem_minus=="miercoles":
        examen=input(f'¿Hubo examen le dia {dia_sem_minus}? SI O NO:')
        examen=examen.lower()
        if examen=='si':
            alum_aprobados=int(input("Ingresar la cantidad de alumnos aprobados:"))
            alum_reprobados=int(input("Ingresar la cantidad de alumnos reaprobados:"))
            total_alumnos=alum_aprobados+alum_reprobados
            porcentaje_aprobados=(alum_aprobados*100)/total_alumnos
            print(f"Porcentaje de alumnos aprobados: {porcentaje_aprobados}%")  
        else:
            print(f'No hubo examen el dia {dia_sem_minus}')
elif dia_sem_minus=="jueves":
    asistencia_jueves=int(input("Ingresar el porcentaje de asistencia de la clase:"))
    if asistencia_jueves>50:
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")
elif dia_sem_minus=="viernes" and dia==1:
    if mes==1 or mes==7:
        print("Comienzo de nuevo ciclo")
        cantidad_alum=int(input("Infresar la cantidad de alumnos de este nuevo ciclo:"))
        arancel=int(input("Ingresar el aracel que abonaran los alumnos:$"))
        total_ingreso=cantidad_alum*arancel
        print(f"El ingreso total sera de:${total_ingreso}")