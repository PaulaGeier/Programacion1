def position_letter(tried,secret_word):
    position_found=-1
    for l in secret_word: #bucle para analizar las posiciones en las que se encuentra la letra ingresada en la palabra a adivinar
        position_found+=1
        if l==tried: #si la letra que estasiendo analizada en el bucle es igual a la ingresada  cambiar el _ por la letra en la lista previamente creada
            return True
        
def number_position(tried,secret_word):
    position_found=-1
    for l in secret_word: #bucle para analizar las posiciones en las que se encuentra la letra ingresada en la palabra a adivinar
        position_found+=1
        if l==tried: #si la letra que estasiendo analizada en el bucle es igual a la ingresada  cambiar el _ por la letra en la lista previamente creada
            return position_found