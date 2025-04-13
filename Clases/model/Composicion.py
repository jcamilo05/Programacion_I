class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def describir(self):
        return f"Motor {self.tipo} de {self.potencia} HP"

class Coche_7:
    def __init__(self, marca, modelo, potencia, tipo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(potencia, tipo)

    def describir(self):
        print(f"{self.marca} {self.modelo} con {self.motor.describir()}")

