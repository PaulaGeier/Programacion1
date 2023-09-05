objective=int(input('Ingresar el dinero que desea ahorrar: '))
receive=0
while receive<objective:
    money=int(input('Dinero ingresado:'))
    if money>0:
        receive+=money
print(f'Felicitaciones, alcanzo su objetivo. Su dinero ahorrado es de {receive}')