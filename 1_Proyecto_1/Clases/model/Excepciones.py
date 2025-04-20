class ExcesoVelocidadException(Exception):
    pass

class Coche_8:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad

    def incrementar_velocidad(self, incremento):
        nueva_velocidad = self.velocidad + incremento
        if nueva_velocidad > 200:
            raise ExcesoVelocidadException(f"¡Exceso de velocidad! ({nueva_velocidad} km/h)")
        self.velocidad = nueva_velocidad
        print(f"{self.marca} va ahora a {self.velocidad} km/h")
