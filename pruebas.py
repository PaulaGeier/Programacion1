def validDni(num):
    if len(str(num)) == 7 or len(str(num)) == 8:
        return True
    else:  
        return False




while True:
    try:
        dni = int(input("Ingrese su DNI: "))
        print(validDni(dni))
        break
    except ValueError:
        print("Por favor ingrese un numero de DNI válido")