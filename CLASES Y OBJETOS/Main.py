from Motocicleta import Motocicleta

moto1=Motocicleta('Aqua','DSR456','10','2','Vespa','GTS SUPER 125','25/12/2019','120 km/h','144 Kg')

moto2=Motocicleta('Negro','KJH765','10','2','Honda','AX-100','25/12/2025','150 km/h','140 Kg')


moto1.turn_on()

moto1.price=850000

print(f"El valor de la motocicleta {moto1.brand},{moto1.model} es de: {moto1.price}")

moto1.read_price()
moto2.read_price()
