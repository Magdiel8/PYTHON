class persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}")

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
 
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")
    
    def mostrar_info(self):
        print(f"Titular: {self.titular.nombre} {self.titular.apellido}, DNI: {self.titular.dni}, Saldo: {self.saldo}")
# Comprobamos el funcionamiento de las clases
persona1 = persona("Juan", "Pérez", "12345678A")
cuenta1 = CuentaBancaria(persona1, 1000)
cuenta1.mostrar_info()
cuenta1.depositar(500)  
cuenta1.retirar(200)
cuenta1.mostrar_info()
cuenta1.retirar(1500)
cuenta1.mostrar_info()

