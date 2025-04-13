class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        print(f"Velocidad actual: {self.velocidad} km/h")

class Coche_5(Vehiculo):
    def acelerar(self):
        print(f"Coche acelerando rápidamente a {self.velocidad + 50} km/h")

class Bicicleta_2(Vehiculo):
    def acelerar(self):
        print(f"Bicicleta acelerando suavemente a {self.velocidad + 5} km/h")
