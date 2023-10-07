
#Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.
def purchase_total(prices_percentages):
    prices=list(prices_percentages.keys())
    percentages=list(prices_percentages.values())
    total=0
    for n in range(len(prices)):
        calculation=prices[n]*(1-percentages[n])
        total+=calculation
    return total


prices_percentages={
    2500:0.15,
    3000:0.20,
    1500:0.05,
    2600:0.30,
    6740:0.25,
    2000:0.10 
}
print(f"El total de la compra con los respectivos descuentos es de: {purchase_total(prices_percentages)}")
