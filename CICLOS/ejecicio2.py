num=int(input('Ingresar un numero positivo:'))
numeros={}
while num!=0:
    impares=0
    pares=0 
    numeros.append(num)
    proceso=num;
    while proceso>0:
        digito=proceso%10
        if digito%2 ==0:
            pares+=1
        else:
            impares+=1
        proceso=int(proceso/10)
    print(f'Digitos pares:{pares}')
    print(f'Digitos impares:{impares}')
    num=int(input('Ingresar otro numero positivo o 0 para terminar:'))


