import random
import funciones 
list1=['manzana','naranja','sandia', 'frutilla', 'uva','melon']
attempts=5
secret_word=random.choice(list1)#Se elige una palabra de forma aleatoria 5
number_of_letters=len(secret_word)
print("ADIVINE LA PALABRA")
without_guessing=[]#Creacion de una lista para almacenar las letras en contradas y las faltantes por encontrar 
print("Tienes 5  intentos incorrectos")
for n in range(len(secret_word)):
    without_guessing.append("_")
print(" ".join(without_guessing)) #Se imprimen las letras a adivinar en forma de _ que fueron almacenadas en una lista y ahora para imprimir se pasaron a string
found_letters=0
while attempts>=0:
    if found_letters==len(secret_word): 
        print("FELICIDADES, PALABRA ENCONTRADA")
        print(secret_word)
        break #Si las letras encontradas son las misma cantidad que la longitud de la palabra a adivinar eso implica que la palabra fue encontrada por el jugador
    if attempts>0:
        tried=input("Ingresar una letra:")
        tried=tried.lower()
        if tried in secret_word: #Si la palabra ingresada esta en la palabra a adivinar 
            found_letters+=1
            
            if funciones.position_letter(tried,secret_word)==True:
                print("Letra encontrada")
                without_guessing[funciones.number_position(tried,secret_word)]=tried
            print(" ".join(without_guessing))
        else:
            print("No se encuentra, INTENTE DE NUEVO")
            attempts-=1
    else:
        print("GAME OVER")
        break