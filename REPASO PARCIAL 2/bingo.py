import random

numbers_list=[]

print("Ingresar 25 numeros entre 1 y 75")
while len(numbers_list)<25:
    same=False
    number=int(input("Ingresar numero:"))
    if (number <1 or number>75):
        print("Numero ingresado incorrecto, ingresar numeros del 1 al 75")
    else: 
        for n in numbers_list:
            if number==n:
                    same=True
                    break
        if same==False:
            numbers_list.append(number)
        else:
            print("Este numero ya fue ingresado")

print("------------------------------------")
#Llenar carton
numbers_matrix=[
    [],
    [],
    [],
    [],
    []
]
for n in numbers_matrix:
    i=0
    for j in range(5):
        n.append(numbers_list[j])
    while i<5:
        del numbers_list[0]
        i+=1

print("TU CARTON:")
for n in numbers_matrix:
    print(n)

print("-----------------------------------")

#Extraer bolas
print("COMIENZA EL JUEGO")

random_number:random.randrange(1,76)

for i in range(len(numbers_matrix)):
    for j in range(5):
        if numbers_matrix[i][j]==random_number:
            print(f"El numero {random_number} se encuentra en tu carton ")
            numbers_matrix[i][j]="X"
            

