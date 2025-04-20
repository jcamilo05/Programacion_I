from model.Usuario import Usuario
from utils.base_datos import base_datos

class Administrador(Usuario):
    def __init__(self):
        super().__init__("Admin", "Admin1234")
        self.__acceso_autorizado = False  # Inicialmente no autorizado

    def autorizar_acceso(self, metodo):
        """Autoriza el acceso administrativo"""
        if metodo.lower() in ["tarjeta", "codigo"]:
            self.__acceso_autorizado = True
            return True
        return False

    def cambiar_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres")
            return False
        self.contraseña = nueva_contraseña
        base_datos["usuarios"]["Admin"] = nueva_contraseña
        print("Contraseña actualizada exitosamente")
        return True

    def ver_todos_los_usuarios(self, usuarios):
        """Muestra todos los usuarios (requiere acceso autorizado)"""
        if not self.__acceso_autorizado:
            print("Error: Primero debe autorizar su acceso como administrador")
            return
        
        print("\n=== LISTA COMPLETA DE USUARIOS ===")
        print(f"{'Cuenta':<15} {'Saldo':<10} {'Estado':<10}")
        print("-" * 35)
        for cuenta, usuario in usuarios.items():
            estado = "BLOQUEADO" if usuario.bloqueado else "ACTIVO"
            print(f"{cuenta:<15} ${usuario.saldo:<9.2f} {estado:<10}")

    def ver_logs(self, numero_cuenta):
        """Muestra los logs de un usuario (requiere acceso autorizado)"""
        if not self.__acceso_autorizado:
            print("Error: Primero debe autorizar su acceso como administrador")
            return
        
        print(f"\nHistorial de {numero_cuenta}:")
        for log in base_datos["logs"].get(numero_cuenta, []):
            print(" ", log)