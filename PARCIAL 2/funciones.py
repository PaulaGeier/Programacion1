#FUNCION BOOLEANA QUE VERIFICARA SI LAS CADENAS DE ADN INGRESADAS SON LAS CORRECTAS
def check_letters(word):
    ax=0
    for i in word:
        if i!="A" and i!="C" and i!="G" and i!="T": #Verifica que las letras ingresadas sean A,C,G O T
            ax+=1
    if ax>0 or len(word)!=6: #Ademas de que las letras sean las correctas se verifica que sean 6
        return False
    else:
        return True
        
#---------------------------------------------------------
#FUNCION QUE ANALIZARA LAS REPETICIONES EN LAS CADENAS DE ADN
def repeated_dna(dna_chain):
    counter=1
    for i in range(1,len(dna_chain)):
        if (dna_chain[i]==dna_chain[i-1]) and counter<4:
            counter+=1 #Si hay secuencias de valores iguales el contador nos dara cuantos valores iguales hay secuencualmente
        elif counter==4:
            break
        else:
            counter=1
    return counter 
    
#---------------------------------------------------------
#FUNCION BOOLEANA QUE DEVOLVERA SI EL HUMANO ES MUTANTE O NO (TRUE O FALSE)
def is_mutant(dna):

    #DIAGONALES IZQUIERDAS

    #DIAGONAL PRINCIPAL 
    dna_chain=[] 
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i==j:
                dna_chain.append(dna[i][j]) #Almacena los valores de la diagonal principal en una lista
    if repeated_dna(dna_chain)==4: #Se llama a la funcion que analizara y contara las repeticiones continuas de la diagonal
        return True 
    
    #DIAGONAL DE LA POSICION 1,0
    dna_chain=[]
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i==j+1:
                dna_chain.append(dna[i][j])

    if repeated_dna(dna_chain)==4:
        return True 
    
    #DIAGONAL DE LA POSICION 0,1
    dna_chain=[]
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i==j-1:
                dna_chain.append(dna[i][j])

    if repeated_dna(dna_chain)==4:
        return True 
    

    #DIAGONAL DE LA POSICION 2,0
    dna_chain=[]
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i==j+2:
                dna_chain.append(dna[i][j])

    if repeated_dna(dna_chain)==4:
        return True 
    
    #DIAGONAL DE LA POSICION 0,2
    dna_chain=[]
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i==j-2:
                dna_chain.append(dna[i][j])
    
    
    if repeated_dna(dna_chain)==4:
        return True 
    
    #-------------------
    #DIAGONALES DERECHAS

    #DIAGONAL SECUNDARIA
    dna_chain=[]
    for i in range(len(dna)):
        dna_chain.append(dna[i][5-i])
    
    if repeated_dna(dna_chain)==4:
        return True 
    
    #DIAGONAL DE LA POSICION 0,4
    dna_chain=[]
    for i in range(len(dna)):
            if i<=4:
                dna_chain.append(dna[i][4-i])
    
    if repeated_dna(dna_chain)==4:
        return True 
    
    #DIAGONAL DE LA POSICION 0,3
        dna_chain=[]
    for i in range(len(dna)):
        if i<=3:
            dna_chain.append(dna[i][3-i])
    
    if repeated_dna(dna_chain)==4:
        return True 

    #DIAGONAL DE LA POSICION 1,5
    dna_chain=[]
    for i in range(len(dna)): 
        if i>0:
            dna_chain.append(dna[i][6-i])
    
    if repeated_dna(dna_chain)==4:
        return True 
    
    #DIAGONAL DE LA POSICION 2,5
    dna_chain=[]
    for i in range(len(dna)): 
        if i>1:
            dna_chain.append(dna[i][7-i])
    
    if repeated_dna(dna_chain)==4:
        return True 

    #-------------------
    #FILAS
    dna_chain=[]
    row=0 #Fila que se analizara.Dentro del bucle aumentara su valor y analizara todas las filas
    while row<6:
        for j in range(len(dna)):
            dna_chain.append(dna[row][j])
        if repeated_dna(dna_chain)==4:
            return True
        else:
            row+=1

    #COLUMNAS
    dna_chain=[]
    column=0 #Columna que se analizara. Dentro del bucle aumentara su valor y analizara todas las columnas
    while column<6:
        for i in range(len(dna)):
            dna_chain.append(dna[i][column])
        if repeated_dna(dna_chain)==4:
            return True
        else:
            column+=1

    return False


