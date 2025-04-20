class Coche_3:
    """Modelo de un Coche con constructor."""

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir(self):
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.año}")

