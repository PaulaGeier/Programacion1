import math
operacion=input("desea saer el area de un triangulo(t) o de un circulo(c) ").lower()   #b*a/2
if (operacion == "c"):
    r=int(input("escriba el radio del circulo"))
    print("el area del circulo es de: ", math.pi*r**2)
elif(operacion=="t"):
    h=int(input("ingrese la altura del triangulo "))
    b=int(input("ingrese la base del triangulo "))
    print("el area del triangul es de: ", b*h/2)
else:
    print("valor ingresado no valido ")
