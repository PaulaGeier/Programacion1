name = input("INGRESE SU NOMBRE:")
print(f"Bienvenid@ {name}")
print("JUEGOS")
print("1) Juego de números")
print("2) Juego de palabras")

while True:  # Bucle hasta que se ingrese una opción válida (1 o 2)
    game = input("Ingrese el juego que le gustaría jugar (1 o 2):")
    
    if game.isdigit():  # Verifica si la entrada es un dígito numérico
        game = int(game)
        if game == 1 or game == 2:
            break  # Sale del bucle si se ingresó una opción válida
        else:
            print(f"{name}, ingresa 1 o 2 para seleccionar un juego válido.")
    else:
        print("Error: Debes ingresar un número entero para seleccionar un juego. Intenta de nuevo.")

if game == 1:
    addiction = 0
    counter = 0
    num = 1
    greatest_even_number = 0
    print("Ingrese los números enteros que desee y cuando no quiera ingresar más números ingrese 0")
    while num != 0:
        num = input() #El usuario ingresa un numero 
        if num.isdigit(): #Se verifica si es un entero y si lo es continua el codigo 
            num = int(num)
            if num % 2 == 0 and num > greatest_even_number: #Este condicional verifica si el numero es par y mayor a la variable previamente inicializada para asi obtener el numero mayor en cada vuelta 
                greatest_even_number = num
            elif num % 2 != 0:
                counter += 1
                addiction += num
        else:
            print("Ingresar solamente números enteros")
    print(f"{name} estos son los resultados del juego:")
    if counter != 0:
        print(f"PROMEDIO DE NUMERO IMPARES: {addiction / counter}")
    else:
        print("No se ingresaron números impares")
    if greatest_even_number != 0:
        print(f"MAYOR NUMERO PAR: {greatest_even_number}")
    else:
        print("No se ingresaron números pares")
    
elif game == 2:
    phrase = input(f"{name} ingrese una frase:") 
    phrase = phrase.lower()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for l in phrase: #Este for recorre letra por letra la frase buscando las vocales y sumando la cantidad en las variables anteriores 
        if l == "a":
            a += 1
        elif l == "e":
            e += 1
        elif l == "i":
            i += 1
        elif l == "o":
            o += 1
        elif l == "u":
            u += 1
    print(f"La cantidad de vocales ingresadas fueron:\na={a}\ne={e}\ni={i}\no={o}\nu={u}")
