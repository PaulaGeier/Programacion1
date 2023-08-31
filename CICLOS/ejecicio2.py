num=int(input('Ingresar un numero positivo:'))
numeros=[]
impares=0
pares=0
while num!=0:
    numeros.append(num)
    proceso=num;
    while proceso>0:
        digito=proceso%10
        if digito%2==0:
            pares+=1
        else:
            impares+=1
        proceso=int(proceso/10)
    num=int(input('Ingresar otro numero positivo o 0 para terminar:'))

print(f'Numeros ingresados:{numeros}')
print(f'Digitos pares ingresa:{pares}')
print(f'Digitos impares ingresa:{impares}')