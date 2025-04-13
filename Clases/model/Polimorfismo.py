class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        pass

class Coche_6(Vehiculo):
    def acelerar(self):
        print(f"Coche a {self.velocidad + 40} km/h")

class Bicicleta_3(Vehiculo):
    def acelerar(self):
        print(f"Bicicleta a {self.velocidad + 5} km/h")
