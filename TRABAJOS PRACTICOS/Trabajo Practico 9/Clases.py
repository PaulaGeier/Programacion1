#EJERCICIO 1
class Persona:
    def __init__(self, name = '', age = 0, DNI = 0) -> None:
        self.name = name
        self.age = age
        self.DNI = DNI






# Definicion de getters
    @property
    def get_name(self):
        return self.name
    @property
    def get_age(self):
        return self.age
    @property
    def get_DNI(self):
        return self.DNI

# Definicion de setters

    def set_name(self, new_name):
        if type(new_name) == str:
            self.name = new_name
        else:
            print('El nombre debe ser una cadena de texto')


    def set_age(self, new_age):
        if type(new_age) == int:
            self.age = new_age
        else:
            print('La edad debe ser un valor entero')


    def set_DNI(self, new_DNI):
        if type(new_DNI) == str:
            self.DNI = new_DNI
        else:
            print('El DNI debe ser un valor entero')


    def mostrar(self):
        print(self.name)
        print(self.age)
        print(self.DNI)


    def es_mayor_edad(self):
        if self.age >= 18:
            return True
        else:
            return False

#EJERCICIO 2
class Count:


#constructor
    def __init__(self, owner, amount = 0.0):
        self.owner = owner
        self.amount = amount




    #Definicion de getters
    @property
    def get_owner(self):
        return self.owner


    @property
    def get_amount(self):
        return self.amount




#Definiendo setters
   
    def set_owner(self, new_owner):
        self.owner = new_owner


    def set_amount(self, pre_balance):
        self.amount += pre_balance






    ###   Métodos   ###


    #Mostrar los datos de la cuenta
    def show_info(self):
        print(f"Titular de la cuenta: {self.owner}.\nCantidad: {self.amount}")


    #Ingresar dinero
    def entry_money(self, quanty):
        if quanty >= 0:
            self.amount += quanty
            print(f"Saldo actual: {self.amount}")
        else:
            print("Ingreso de dinero inválido")


    #Retirar dinero
    def withdraw(self, quanty):
        if quanty >= 0:
            self.amount -= quanty
            print(f"Saldo actual: {self.amount}")
        else:
            print("Retiro de dinero inválido")

#EJERCICIO 3
#clase
class Triangle:
    #creamos el constructor de la clase triangulo, donde luego se van a cargar los lados de un triangulo
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


    #Esta es la funcion que me va a decir, según sus lados, el tipo de triángulo
    def type_triangle(self):
        #evalua si son todos iguales
        if (self.side1 == self.side2) and (self.side2 == self.side3):
            print("Según sus lados, el triangulo ingresado es un triangulo equilatero.")
        #si no, evalua si son todos distintos
        elif (self.side1 != self.side2) and (self.side2 != self.side3):
            #evalua que el lado 1 sea el mayor
            if (self.side1 > self.side2) and (self.side1 > self.side3):
                print("Según sus lados, el triangulo ingresado es un triangulo escaleno. ")
                print (f"El lado con un mayor tamaño es: {self.side1}")
            #evalua que el lado 2 sea el mayor
            elif (self.side2 > self.side1) and (self.side2 > self.side3):
                print("Según sus lados, el triangulo ingresado es un triangulo escaleno. ")
                print (f"El lado con un mayor tamaño es: {self.side2}")
            #condicion que toma por descarte el lado 3
            else:
                print("Según sus lados, el triangulo ingresado es un triangulo escaleno. ")
                print (f"El lado con un mayor tamaño es: {self.side3}")
        else:
            print("Según sus lados, el triángulo ingresado es un triángulo isósceles ")
#EJERCICIO 4
class Schedule():
    def __init__(self) -> None:
        self.contacts = []

    def add_contact(self, name, phone, gmail):
        contact = {
            'name': name,
            'phone': phone,
            'gmail': gmail
        }
        self.contacts.append(contact)
    def show_contacts(self):
        if len(self.contacts) != 0:
            for contact in self.contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Gmail: {contact['gmail']}")
                print()
        else:
            print('No tienes contactos para mostrar.')
    def search_contacts(self, to_search):
        contact_found = False
        for contact in self.contacts:
            if to_search.lower() == contact['name'].lower():
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Gmail: {contact['gmail']}")
                contact_found = True
        if not contact_found:
            print('El contacto no existe')
    def edit_contact(self, to_edit, new_name, new_phone, new_gmail):
        contact_found = False
        for contact in self.contacts:
            if to_edit.lower() == contact['name'].lower():
                contact['name'] = new_name
                contact['phone'] = new_phone
                contact['gmail'] = new_gmail
                print('Contacto editado con éxito')
                contact_found = True
        if not contact_found:
            print('El contacto no existe')
