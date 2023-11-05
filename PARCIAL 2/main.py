import funciones 

while True:
    print("¿HUMANO O MUTANTE?")

    matrix_dna=[
        [],
        [],
        [],
        [],
        [],
        []
    ]
    
    #Llenar matriz con secuencia de ADN
    filled_lines=0
    dna_chain=[]
    while filled_lines<6:
        dna=input(f"Ingresar secuencia de DNA:").upper()
        if funciones.check_letters(dna)==True: #La funcion verifica si la secuencia de adn ingresada sea correcta
            for i in matrix_dna:
                if len(i)==0:
                    for letter in dna:
                        i.append(letter)
                    #i.append(dna_chain) #Si las letras del string y la longitud es correcta se añade a la matriz en la primera fila vacia que encuentre
                    filled_lines+=1
                    break
            for i in matrix_dna:
                print(i)

        else:
            print("INCONRRECTO. Debe ingresar las letras A,C,G o T y deben ser 6 letras")
    print("-----------------------------")


    #Imprimir secuencia de ADN
    print("ADN DEL HUMANO")
    for i in matrix_dna:
        print(i)
    print("------------------------------")


    #Verificar si es mutante
    if funciones.is_mutant(matrix_dna)==True:
        print("ES MUTANTE!")
    else:
        print("NO ES MUTANTE")
    
    #Salida
    exitt=input("Para ingresar otro ADN ingrese 0, sino ingrese cualquier otro valor:")

    if exitt!='0':
        print("BYE BYE")
        break