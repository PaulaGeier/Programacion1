class Motocicleta:

    #Atributo de clase
    state='Nueva' #estado
    engine=False #motor
    def __init__(self, color='', tuition='', fuel_liters='',number_wheels='',brand='',model='',fabrication_date='',ortip_speed='',weight=''):
        self.color=color
        self.tuition=tuition #matricula
        self.fuel_liters=fuel_liters #combustible_litros
        self.number_wheels=number_wheels #numero_ruedas
        self.brand=brand #marca
        self.model=model
        self.fabrication_date=fabrication_date
        self.ortip_speed=ortip_speed #velocidad_punta
        self.weight=weight #peso
    
    #Metodos inteligentes
    
    #  Arrancar
    def turn_on(self):
        if self.engine:
            print('El motor ya estaba arrancado')
        else:
            self.engine=True
            print('El motor fue arrancado')
    
    #  Detener
    def turn_off(self):
        if self.engine:
            print('El motor fue detenido')
        else:
            print('El motor fue detenido')



    #Consultar precio
    def read_price(self):
        print(f"El valor de la motocicleta {self.brand}, {self.model} es de: {self.price}")

