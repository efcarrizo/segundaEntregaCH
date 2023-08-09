class Cliente():
    def __init__(self, nombre, email, direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.carrito = []
        
    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
            
    def eliminar_del_carrito(self, producto):
        if producto in self.carrito:
            self.carrito.remove(producto)
            
    def vaciar_carrito(self):
        self.carrito = []
                
    def mostrar_carrito(self):
        print(f"Carrito de {self.nombre}: ")
        for producto in self.carrito:
                print(f"- {producto}")
        if self.carrito == []:
                print("No tienen ningun producto en el carrito")
                
    def realizar_compra(self):
        if len(self.carrito) > 0:
            print(f"{self.nombre} ha realizado una compra con exito.")
            self.vaciar_carrito()    
        else:
             print("El carrito esta vacio. No se pudo realizar la compra")
            
    def __str__(self):
        return f"Cliente: {self.nombre}"