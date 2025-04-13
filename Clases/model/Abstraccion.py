from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro dice: ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato dice: ¡Miau!")
