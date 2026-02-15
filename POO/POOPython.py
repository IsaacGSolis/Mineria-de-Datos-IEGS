#Creacion de clase coche
class coche:
    def __init__(self):
        self.marca="Honda"
        self.modelo="City"
        self.anio="2019"
        self.velocidad=0
    def acelerar(self, velocidad):
        if velocidad>0:
            self.velocidad+=velocidad
            print("El coche ha acelerado a", self.velocidad, "km/h")
        else:
            print("La velocidad debe ser un valor positivo.")
    def frenar(self, velocidad):
        if self.velocidad>0:
            self.velocidad-=velocidad
            if self.velocidad<0:
                self.velocidad=0
            print("El coche ha frenado a", self.velocidad, "km/h")
        else:
            print("El coche ya está detenido.")
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.anio}")
#Creacion de clase CuentaBancaria
class CuentaBancaria:
    def __init__(self):
        self.titular="Arturo Gonzalez"
        self.saldo=0
    def depositar(self, cantidad):
        if cantidad>0:
            self.saldo+=cantidad
            print("Has depositado:", cantidad)
        else:
            print("La cantidad a depositar debe ser un valor real positivo.")
    def retirar(self, cantidad):
        if cantidad>0:
            if self.saldo>=cantidad:
                self.saldo-=cantidad
                print("Has retirado: $", cantidad)
            else:
                print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            print("La cantidad a retirar debe ser un valor real positivo.")
    def mostrar_saldo(self):
        print(f"Titular de la cuenta: {self.titular}")
        print(f"El saldo actual es: ${self.saldo}")
#Creacion de clase Rectangulo
class Rectangulo:
    def __init__(self):
        self.base=0
        self.altura=0
    def calcular_area(self):
        return self.base*self.altura
    def calcular_perimetro(self):
        return 2*(self.base+self.altura)
    def mostrar_info(self):
        area=self.calcular_area()
        perimetro=self.calcular_perimetro()
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Area: {area}")
        print(f"Perimetro: {perimetro}")