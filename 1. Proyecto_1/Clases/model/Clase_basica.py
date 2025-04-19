class Coche:
    """ clase que crea un modelo de un Coche."""

    def __init__(self, marca, modelo, año):
        """Atributos marca, modelo y año."""
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir(self):
        """Metodo describir, muestra la información del coche."""
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.año}")


