import funciones
num= int(input('Numero a procesar: '))
while num!=0:
    print(f'Suma: {funciones.add_diggits(num)}')
    num= int(input('Numero a procesar: '))
