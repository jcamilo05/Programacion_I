class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        print(f"Acelerando a {self.velocidad} km/h")

class Coche_4(Vehiculo):
    def __init__(self, velocidad, marca):
        super().__init__(velocidad)
        self.marca = marca

    def info(self):
        print(f"Coche marca {self.marca}, velocidad {self.velocidad} km/h")

class Bicicleta(Vehiculo):
    def __init__(self, velocidad, tipo):
        super().__init__(velocidad)
        self.tipo = tipo

    def info(self):
        print(f"Bicicleta tipo {self.tipo}, velocidad {self.velocidad} km/h")
