import datetime
from utils.base_datos import base_datos

class Usuario:
    """Clase usuario crea un usuario generico que puede tener mas permisos de administrador:
    
    Parametros de entrada constructor: 
    * numero cunta 
    * Contraseña
    * saldo
    
    Ademas tiene los metdos 
    * Ingresar dinero
    * sacar dinero
    Ambos metodos validan que el valor usado sea un valor positivo
    *Ver_info: Muestra el estado de la cuenta, el saldo y la cuenta
    * log_operaciones: lee el diccionario base_datos para ver que operacion a realiazado el ususario

    """
    def __init__(self, numero_cuenta, contraseña, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__contraseña = contraseña
        self.__saldo = saldo
        self.__intentos_fallidos = 0
        self.__bloqueado = False
        if numero_cuenta not in base_datos["logs"]:
            base_datos["logs"][numero_cuenta] = []

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña
        base_datos["usuarios"][self.__numero_cuenta] = nueva_contraseña

    @property
    def saldo(self):
        return self.__saldo

    @property
    def bloqueado(self):
        return self.__bloqueado

    @property
    def intentos_fallidos(self):
        return self.__intentos_fallidos

    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    def bloquear(self):
        self.__bloqueado = True

    def desbloquear(self):
        self.__bloqueado = False
        self.__intentos_fallidos = 0

    def resetear_intentos(self):
        self.__intentos_fallidos = 0

    def aumentar_intentos(self):
        self.__intentos_fallidos += 1

    def ingresar_dinero(self, monto):
        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto debe ser positivo")
            self.__saldo += monto
            self.log_operacion(f"Ingreso: +${monto:.2f}")
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo:.2f}")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def sacar_dinero(self, monto):
        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto debe ser positivo")
            if monto > self.__saldo:
                raise ValueError("Fondos insuficientes")
            self.__saldo -= monto
            self.log_operacion(f"Retiro: -${monto:.2f}")
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo:.2f}")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def ver_info(self):
        estado = "BLOQUEADO" if self.__bloqueado else "ACTIVO"
        print(f"Cuenta: {self.__numero_cuenta} | Saldo: ${self.__saldo:.2f} | Estado: {estado}")

    def log_operacion(self, mensaje):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        base_datos["logs"][self.__numero_cuenta].append(f"[{timestamp}] {mensaje}")