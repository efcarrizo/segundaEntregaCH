def registrar_usuario(usuario, contraseña, base_de_datos):
    if usuario in base_de_datos:
        print("El usuario ya existe")
    else:
        base_de_datos[usuario] = contraseña
        print(f"Usuario '{usuario}' registrado exitosamente.")

def mostrar_informacion(base_de_datos):
    print("Usuarios registrados:")
    for usuario, contraseña in base_de_datos.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

def login(usuario, contraseña, base_de_datos):
    if usuario in base_de_datos and base_de_datos[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Usuario o contraseña incorrectos.")

def main():
    base_de_datos = {}
    
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Registrar usuario")
        print("2. Mostrar información")
        print("3. Login de usuario")
        print("4. Salir")
        
        opcion = input("Ingresa el número de opción: ")
        
        if opcion == "1":
            usuario = input("Ingresa el nombre de usuario: ")
            contraseña = input("Ingresa la contraseña: ")
            registrar_usuario(usuario, contraseña, base_de_datos)
        elif opcion == "2":
            mostrar_informacion(base_de_datos)
        elif opcion == "3":
            usuario = input("Ingresa el nombre de usuario: ")
            contraseña = input("Ingresa la contraseña: ")
            login(usuario, contraseña, base_de_datos)
        elif opcion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()