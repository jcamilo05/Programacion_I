class Coche_2:
    """Modelo de un Coche con encapsulamiento."""

    def __init__(self, marca, modelo, año):
        """Atributos privados marca, modelo y año."""
        self._marca = marca
        self._modelo = modelo
        self._año = año

    # Métodos get
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_año(self):
        return self._año

    # Métodos set
    def set_marca(self, nueva_marca):
        self._marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    def set_año(self, nuevo_año):
        self._año = nuevo_año

    def describir(self):
        """Información del coche."""
        print(f"Coche: {self._marca} {self._modelo}, Año: {self._año}")


coche1 = Coche_2("Renault", "Kwid", 2024)
coche2 = Coche_2("Renault", "Duster", 2016)
coche3 = Coche_2("Toyota", "Hylux", 2025)

# Método describir()
coche1.describir()
print("---")
coche2.describir()
print("---")
coche3.describir()