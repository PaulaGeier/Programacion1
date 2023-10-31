from Clases import Triangle, Count, Schedule
#EJERCICIO 2
c1 = Count("Thomas Muñoz", 38522.59)

c1.show_info()
c1.set_amount(2000.0)
c1.show_info()
c1.set_amount(-5000.0)
c1.show_info()
c1.entry_money(5)
c1.entry_money(-5)
c1.withdraw(6)
c1.withdraw(-6)

#-------------------------------------------------
#EJERCICIO 3
#instancia del objeto triangulo
triangle1 = Triangle(2,3,4)
triangle1.type_triangle()
print("- - - ")
triangle2 = Triangle(4,4,4)
triangle2.type_triangle()
print("- - - ")


triangle3 = Triangle(5,3,3)
triangle3.type_triangle()
print("- - - ")
#-------------------------------------------------
#EJERCICIO 4
schedule = Schedule()


while True:
    print('Bienvenido al menu de tu agenda, que quieres hacer?\n[1] Añadir contacto\n[2] Lista de contactos\n[3] Buscar contacto\n[4] Editar contacto\n[5] Cerrar agenda')
    op = input('Ingresa una opción valida: ')
    if op == '1':
        print('Crear contacto\n')
        name = input('Ingresa el nombre del nuevo contacto: ')
        phone = int(input('Ingresa el telefono del nuevo contacto: '))
        gmail = input('Ingresa el gmail del nuevo contacto: ')
        schedule.add_contact(name,phone,gmail)
        print('Contacto añadido')
    elif op == '2':
        print('Ver lista de contactos')
        schedule.show_contacts()
    elif op == '3':
        to_search = input('Ingresa el nombre del contacto que quieres buscar: ')
    elif op == '4':
        to_edit = input('Ingresa el nombre del contacto que deseas editar: ')
        new_name = input('Nuevo nombre: ')
        new_phone = int(input('Nuevo teléfono: '))
        new_gmail = input('Nuevo correo electrónico: ')
        schedule.edit_contact(to_edit, new_name, new_phone, new_gmail)
        schedule.search_contacts(to_search)
    elif op == '5':
        print('Cerrando agenda')
        break
