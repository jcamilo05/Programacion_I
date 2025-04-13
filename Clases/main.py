from model.Clase_basica import Coche
from model.Encapsulamiento import Coche_2
from model.Constructores import Coche_3
from model.Herencia import Coche_4, Bicicleta
from model.Sobreescritura import Coche_5, Bicicleta_2
from model.Polimorfismo import Coche_6, Bicicleta_3
from model.Abstraccion import Perro, Gato
from model.Interfaz import Pajaro, Avion
from model.Composicion import Coche_7
from model.Excepciones import Coche_8,ExcesoVelocidadException


print("-----------------------------Ejercicio 1 - Clase basica --------------------------------------")

# Objetos de la clase Coche
coche1 = Coche("Renault", "Kwid", 2024)
coche2 = Coche("Renault", "Duster", 2016)

# Método describir()
coche1.describir()
print("---")
coche2.describir()

print("-----------------------------Ejercicio 2 Encapsulamiento ------------------------------------")
# Objetos de la clase Coche
coche1 = Coche_2("Renault", "Kwid", 2024)
coche2 = Coche_2("Renault", "Duster", 2016)
coche3 = Coche_2("Toyota", "Hylux", 2025)

# Método describir()
coche1.describir()
print("---")
coche2.describir()
print("---")
coche3.describir()

print("-----------------------------Ejercicio 3 Constructor ----------------------------------------")
# Objetos creados usando constructor
coche1 = Coche_3("Mazda", "3", 2022)
coche2 = Coche_3("Chevrolet", "Onix", 2020)
coche3 = Coche_3("Kia", "Sportage", 2023)

coche1.describir()
print("---")
coche2.describir()
print("---")
coche3.describir()

print("-----------------------------Ejercicio 4 Herencia -----------------------------------------")
coche = Coche_4(120, "Ford")
bici = Bicicleta(25, "Montaña")

coche.info()
coche.acelerar()
print("---")
bici.info()
bici.acelerar()

print("-----------------------------Ejercicio 5 Sobrescritura -----------------------------------------")
coche = Coche_5(100)
bici = Bicicleta_2(15)

coche.acelerar()
print("---")
bici.acelerar()

print("-----------------------------Ejercicio 6 Polimorfismo -----------------------------------------")

#crea la instancias de bicicleta y coches con diferentes velocidades 
vehiculos = [Coche_6(80), Bicicleta_3(20), Coche_6(100), Bicicleta_3(10)]

#Aplica el mismo metodo acelerar a todos los vehiculos creados en la lista anterior
for v in vehiculos:
    v.acelerar()
    print("---")


print("-----------------------------Ejercicio 7 Abstraccion ----------------------------------------")

animales = [Perro(), Gato()]

for animal in animales:
    animal.hacer_sonido()
    print("---")


print("-----------------------------Ejercicio 8 Interfaz ----------------------------------------")

voladores = [Pajaro(), Avion()]

for v in voladores:
    v.volar()
    print("---")


print("-----------------------------Ejercicio 9 Composicion -------------------------------------")

coche1 = Coche_7("Toyota", "Hilux",120, "Gasolina")
coche2 = Coche_7("Ford", "Ranger", 200, "Diesel")

coche1.describir()
print("---")
coche2.describir()

print("-----------------------------Ejercicio 10 Excepciones ----------------------------------")

coche = Coche_8("Audi")

try:
    coche.incrementar_velocidad(150)
    print("---")
    coche.incrementar_velocidad(60)
except ExcesoVelocidadException as e:
    print("Excepción capturada:", e)