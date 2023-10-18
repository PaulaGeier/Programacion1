import funciones 
passenger_data=[('Paula Geier', 44593085, 'Rio De Janeiro'), ('Rodrigo Zapata', 47805624, 'Cordoba'),('Thomas Muñoz', 94219667, 'Vancuver')]
country_belonging=[('Brasil','Rio De Janeiro'),('Argentina','Cordoba'),('Canada','Vancuver'),('Brasil','Bahia')]
salida=False
while salida==False:
    print('MENU\n1.Agregar pasajeros a la lista de viajeros\n2.Agregar ciudades a la lista de ciudades\n3.Dado el DNI de un pasajero, ver a qué ciudad viaja\n4.Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad\n5.Dado el DNI de un pasajero, ver a qué país viaja\n6.Dado un país, mostrar cuántos pasajeros viajan a ese país\n7.Salir del programa')
    option=int((input("Ingresar el NUMERO de opcion:")))
    if option==1:
        new_name=input("Nombre y apellido del pasajero:")
        new_dni=int(input("DNI del pasajero:"))
        new_city=input('Ciudad de destino:')
        new_country=input("Pais de destino:")
        passenger_data.append((new_name,new_dni,new_city))
        country_belonging.append((new_country,new_city))
        #Agregar pasar las primeras letras en mayusculas y el resto en minuscula
        print(f"Nuevo pasajero:{(passenger_data[-1])[1]}")
        print(f"DNI:{(passenger_data[-1])[0]}")
        print(f"Ciudad de destino:{(passenger_data[-1])[2]}")
    elif option==2:
        print("Ciudades existentes:")
        for n in range(len(country_belonging)):
            print(f"{n+1}_{(country_belonging[n])[0]},{(country_belonging[n])[1]} ")
        new_city=input('Ingresar ciudad nueva:')
        new_country=input('Ingresar pais de la ciudad:')
        country_belonging.append((new_city,new_country))
        print("Ciudad agregada")
    elif option==3:
        search_dni=int(input('Ingresar el DNI del pasajero:'))
        for n in range(len(passenger_data)):
            if search_dni in passenger_data[n]:
                print(f"{(passenger_data[n])[0]} viaja con destino a {(passenger_data[n])[2]}")
    elif option==4:
        number_of_passengers=0
        print("Seleccionar el numero de la ciudad:")
        for n in range(len(country_belonging)):
            print(f"{n+1}_{(country_belonging[n])[0]},{(country_belonging[n])[1]}")
        chosen_city=int(input())
        for n in range(len(passenger_data)):
            if (country_belonging[chosen_city-1][1]) in passenger_data[n]:
                number_of_passengers+=1
        print(f"Cantidad de pasajeros que viajan a {country_belonging[chosen_city-1]}: {number_of_passengers}")
    elif option==5:
        search_dni=int(input('Ingresar el DNI del pasajero:'))
        for n in range(len(passenger_data)):
            if search_dni in passenger_data[n]:
                destination_city=(passenger_data[n])[2]
                for n in range(len(country_belonging)):
                    if destination_city in country_belonging[n]:
                        print(f"{(passenger_data[n])[0]} viaja con destino a {(country_belonging[n])[0]}")
    elif option==6: 
        number_of_passengers=0
        print("Seleccionar el numero del pais:")
        for n in range(len(country_belonging)):
            print(f"{n+1}_{(country_belonging[n])[0]}")
            #Hacer una sola lista de paises sin que estos se repitan si hay mas de un pasajero que viaja alli
        chosen_country=input()
        for c in country_belonging:
            if chosen_country==c[0]:
                ax=c[1]
                for p in passenger_data:
                    if ax==p[2]:
                        number_of_passengers+=1
        print(f"Los pasajeros que viajan a {chosen_country} son: {number_of_passengers}")
    elif option==7:
        print("VUELVA PRONTO :)")
        break

