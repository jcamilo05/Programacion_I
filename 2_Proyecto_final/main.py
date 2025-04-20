from model.Corresponsal import Corresponsal
from model.Administrador import Administrador
from utils.base_datos import base_datos

def mostrar_menu_principal():
    print("\n=== CORRESPONSAL BANCARIO ===")
    print("1. Administrador")
    print("2. Usuario")
    print("3. Salir")
    return input("Seleccione una opción: ")

def menu_administrador():
    print("\n=== MENÚ ADMINISTRADOR ===")
    print("1. Ver todos los usuarios")
    print("2. Ver logs de usuarios")
    print("3. Cambiar contraseña")
    print("4. Volver al menú principal")
    return input("Seleccione una opción: ")

def menu_usuario_no_autenticado():
    print("\n=== MENÚ USUARIO ===")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Volver al menú principal")
    return input("Seleccione una opción: ")

def menu_usuario_autenticado():
    print("\n=== SERVICIOS BANCARIOS ===")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Ver información")
    print("4. Ver historial")
    print("5. Cerrar sesión")
    return input("Seleccione una opción: ")

def autenticar_admin():
    print("\n--- INICIO DE SESIÓN ADMINISTRADOR ---")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == "Admin" and contraseña == "Admin1234":
        return Administrador()
    print("\nCredenciales incorrectas")
    return None

def main():
    corresponsal = Corresponsal()
    
    while True:
        opcion_principal = mostrar_menu_principal()
        
        if opcion_principal == "1":  # Administrador
            print("\n--- INICIO DE SESIÓN ADMINISTRADOR ---")
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            
            if usuario == "Admin" and contraseña == "Admin1234":
                admin = corresponsal.buscar_usuario("Admin")
                metodo = input("Método de autenticación (tarjeta/codigo): ")
                
                if admin.autorizar_acceso(metodo):
                    print("\n¡Autenticación exitosa!")
                    while True:
                        opcion_admin = menu_administrador()
                        
                        if opcion_admin == "1":
                            admin.ver_todos_los_usuarios(corresponsal.usuarios)
                        elif opcion_admin == "2":
                            cuenta = input("Ingrese número de cuenta: ")
                            admin.ver_logs(cuenta)
                        elif opcion_admin == "3":
                            nueva_contraseña = input("Nueva contraseña: ")
                            admin.cambiar_contraseña(nueva_contraseña)
                        elif opcion_admin == "4":
                            admin._Administrador__acceso_autorizado = False  # Resetear autorización
                            print("Cerrando sesión administrativa...")
                            break
                        else:
                            print("Opción no válida")
                else:
                    print("Método de autenticación inválido")
            else:
                print("Credenciales incorrectas")
        
        elif opcion_principal == "2":  # Usuario
            while True:
                opcion_usuario = menu_usuario_no_autenticado()
                
                if opcion_usuario == "1":  # Registrar usuario
                    print("\n--- REGISTRO DE USUARIO ---")
                    cuenta = input("Ingrese número de cuenta: ")
                    if cuenta.lower() == "admin":
                        print("No puede usar 'admin' como número de cuenta")
                        continue
                    contraseña = input("Ingrese contraseña: ")
                    corresponsal.registrar_usuario(cuenta, contraseña)
                
                elif opcion_usuario == "2":  # Iniciar sesión
                    print("\n--- INICIO DE SESIÓN ---")
                    cuenta = input("Número de cuenta: ")
                    contraseña = input("Contraseña: ")
                    usuario = corresponsal.login(cuenta, contraseña)
                    
                    if usuario:
                        while True:
                            opcion_autenticado = menu_usuario_autenticado()
                            
                            if opcion_autenticado == "1":  # Ingresar dinero
                                monto = input("Monto a ingresar: ")
                                usuario.ingresar_dinero(monto)
                            elif opcion_autenticado == "2":  # Retirar dinero
                                monto = input("Monto a retirar: ")
                                usuario.sacar_dinero(monto)
                            elif opcion_autenticado == "3":  # Ver información
                                usuario.ver_info()
                            elif opcion_autenticado == "4":  # Ver historial
                                print("\nHistorial de operaciones:")
                                for log in base_datos["logs"].get(usuario.numero_cuenta, []):
                                    print(" ", log)
                            elif opcion_autenticado == "5":  # Cerrar sesión
                                print("Cerrando sesión...")
                                break
                            else:
                                print("\nOpción no válida")
                
                elif opcion_usuario == "3":  # Volver al menú principal
                    break
                else:
                    print("\nOpción no válida")
        
        elif opcion_principal == "3":  # Salir
            print("\nGracias por usar nuestro corresponsal bancario. ¡Hasta pronto!")
            break
        
        else:
            print("\nOpción no válida, por favor intente nuevamente")

if __name__ == "__main__":
    main()