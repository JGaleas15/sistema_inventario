class Inventario:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado correctamente.")
    def mostrar_todos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)
    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")
    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def actualizar_producto(self, id_producto, nueva_cantidad, nuevo_precio):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                producto.cantidad = nueva_cantidad
                producto.precio = nuevo_precio
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

