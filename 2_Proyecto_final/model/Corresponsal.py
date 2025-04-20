from utils.base_datos import base_datos
from model.Usuario import Usuario
from model.Administrador import Administrador

class Corresponsal:
    """Clase corresponsal: puede inicializar el sistema, registrar usuarios, ver todos los usuarios y bloquear
    usuarios"""

    def __init__(self):
        self.usuarios = {}
        self.__inicializar_sistema()

    def __inicializar_sistema(self):
        admin = Administrador()
        self.usuarios["Admin"] = admin
        base_datos["usuarios"]["Admin"] = "Admin1234"

    def registrar_usuario(self, numero_cuenta, contraseña):
        if numero_cuenta.lower() == "admin":
            print("Error: Nombre reservado para administrador")
            return False
        if numero_cuenta in self.usuarios:
            print("Error: Cuenta ya existe")
            return False
        self.usuarios[numero_cuenta] = Usuario(numero_cuenta, contraseña)
        base_datos["usuarios"][numero_cuenta] = contraseña
        print(f"Usuario {numero_cuenta} registrado exitosamente")
        return True

    def login(self, numero_cuenta, contraseña):
        usuario = self.usuarios.get(numero_cuenta)
        if not usuario:
            print("Error: Cuenta no existe")
            return None
        if usuario.bloqueado:
            print("Error: Cuenta bloqueada")
            return None
        if usuario.contraseña != contraseña:
            usuario.aumentar_intentos()
            print(f"Error: Contraseña incorrecta (Intentos: {usuario.intentos_fallidos}/3)")
            if usuario.intentos_fallidos >= 3:
                usuario.bloquear()
                print("¡Cuenta bloqueada por seguridad!")
            return None
        usuario.resetear_intentos()
        print(f"Bienvenido, {numero_cuenta}!")
        return usuario

    def ver_todos_los_usuarios(self, requester):
        if requester.numero_cuenta != "Admin":
            print("Error: Solo para administradores")
            return
        print("\n=== USUARIOS REGISTRADOS ===")
        print(f"{'Cuenta':<10} {'Saldo':<10} {'Estado':<10}")
        for cuenta, usuario in self.usuarios.items():
            estado = "BLOQUEADO" if usuario.bloqueado else "ACTIVO"
            print(f"{cuenta:<10} ${usuario.saldo:<9.2f} {estado:<10}")

    def bloquear_usuario(self, admin, numero_cuenta):
        if admin.numero_cuenta != "Admin":
            print("Error: Sin privilegios")
            return False
        usuario = self.usuarios.get(numero_cuenta)
        if not usuario:
            print("Error: Usuario no existe")
            return False
        usuario.bloquear()
        print(f"Usuario {numero_cuenta} bloqueado")
        return True