partners={
    'Socio n°1':{
        'nombre':' Amanda Núñez',
        'ingreso':'17/03/2009',
        'estado_cuota':'al dia'
    },
    'Socio n°2':{
        'nombre':'Bárbara Molina',
        'ingreso':'17/03/2009',
        'estado_cuota':'al dia'
    },
    'Socio n°3':{
        'nombre':'Lautaro Campos',
        'ingreso':'17/03/20092',
        'estado_cuota':'al dia'
    }
}
option=0
while option!=7:

    print("MENU")
    print("1.Cargar informacion de los socios\n2.Cantidad de socios del club\n3.Registrar pago de cuotas\n4.Modificar fecha de ingreso de socios(ingresados el  13/03/2018, cambiar fecha al 14/03/2018) \n5.Eliminar socio\n6.Listado de socios\n7.Salir del programa")
    option=int(input("Ingresar el numero de la opcion que desea realizar: "))
    if option==1:    
        clue_dictionary=f'Socio n°{len(partners)+1}'
        partners[clue_dictionary]={}
        partners[clue_dictionary]['nombre']=input("Ingresar nombre y apellido del socio: ")
        partners[clue_dictionary]['ingreso']=input("Ingresar fecha de ingreso del socio (dd/mm/aaaa): ")
        partners[clue_dictionary]['estado_cuota']=input("Ingresar estado de la cuota del socio(adeuda/al dia): ") 
        print("Socio ingresado con exito!")
    elif option==2:
        print(f'La cantidad de socios son: {len(partners)}')
    elif option==3:
        membership_number=int(input("Ingresar el numero de socio: "))
        partners[f'Socio n°{membership_number}']['estado_cuota']='al dia'
        print(f'El socio n°{membership_number} ahora registra tiene sus cuotas al dia')
    elif option==4:
        for clue in range(len(partners)):
            if partners[f'Socio n°{clue}']['ingreso']=='13/03/2018':
                partners[f'Socio n°{clue}']['ingreso']='14/03/2018'
    elif option==5:
        partner_to_eliminate=input("Ingresar el numero  de socio que desea eliminar: ")
        del partners[f'Socio n°{partner_to_eliminate}']
        print(f'Socio n°{partner_to_eliminate} eliminado')
    elif option==6:
        for clave, socio in partners.items():
            print(f"-{clave},{socio['nombre']}, ingreso {socio['ingreso']}, cuota {socio['estado_cuota']}")
    elif option==7:
        print("Programa cerrado")
