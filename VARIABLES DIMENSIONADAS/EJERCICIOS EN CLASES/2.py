import funciones
shopping=[('Nuria Costa', 5, 1234.5,'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),('Paula Geier', 10, 954, 'Calle 6 - 985'),('Nuria Costa', 25, 3569,'Calle 1 - 456'),('Marta Rolon', 30, 3524,'Calle 7 - 653')]

print("DOMICILIOS")
for n in range(len(funciones.addresses(shopping))):
    print(f"{(funciones.clients(shopping))[n]} - {(funciones.addresses(shopping))[n]}")

