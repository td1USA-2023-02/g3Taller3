class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"

class Almacen:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto):
       
        for p in self.inventario:
            if p.nombre == producto.nombre:
                print(f"El producto '{producto.nombre}' ya existe en el almacén.")
                return

        
        self.inventario.append(producto)
        print(f"Producto '{producto.nombre}' agregado al almacén.")

    def actualizar_stock(self, nombre, cantidad):
        
        for producto in self.inventario:
            if producto.nombre == nombre:
                producto.stock += cantidad
                print(f"Stock del producto '{nombre}' actualizado. Stock actual: {producto.stock}")
                return

        
        print(f"El producto '{nombre}' no existe en el almacén.")


almacen = Almacen()

while True:
    print("\nOpciones:")
    print("1. Agregar Producto")
    print("2. Actualizar Stock")
    print("3. Mostrar Inventario")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        stock = int(input("Cantidad en stock: "))
        nuevo_producto = Producto(nombre, precio, stock)
        almacen.agregar_producto(nuevo_producto)

    elif opcion == "2":
        nombre = input("Nombre del producto a actualizar: ")
        cantidad = int(input("Cantidad a agregar (positiva) o quitar (negativa): "))
        almacen.actualizar_stock(nombre, cantidad)

    elif opcion == "3":
        if len(almacen.inventario) == 0:
            print("El almacén está vacío.")
        else:
            print("Inventario del almacén:")
            for producto in almacen.inventario:
                print(producto)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")