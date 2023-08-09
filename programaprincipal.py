from clientes.cliente import Cliente

def main():
    
    print("Bienvenido a la plataforma, lo primero que necesitamos son sus datos para realizar la compra")
    nombre = input("Ingresa el nombre: ")
    email = input("Ingresa su email: ")
    direccion = input("Ingrese su dirección: ")
    cliente1 = Cliente(nombre, email, direccion)
    print(cliente1)
        
    while True:
        print(f"\nBienvenido {nombre}, que desea hacer?")
        print("1. Ver mis datos")
        print("2. Ingresar productos")
        print("3. Mostrar carrito de compras")
        print("4. Comprar productos")
        print("5. Salir")
            
        opcion = input("Ingresa el número de opción: ")
            
        if opcion == "1":
            print(f"Cliente: {cliente1.nombre}, email: {cliente1.email}, direccion: {cliente1.direccion}")
        elif opcion == "2":
            producto = input("Ingrese un nuevo producto o 'terminar' para salir: ")
            while producto.lower() != "terminar":
                cliente1.agregar_al_carrito(producto)
                producto = input("Ingrese un nuevo producto o 'terminar' para salir: ")
            else: 
                print("Usted ha ingresado")
                cliente1.mostrar_carrito()
        elif opcion == "3":
            cliente1.mostrar_carrito()
        elif opcion == "4":
            cliente1.realizar_compra()
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()