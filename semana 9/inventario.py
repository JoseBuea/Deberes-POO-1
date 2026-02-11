from producto import Producto

class Inventario:
    def __init__(self):
        # Lista que almacenará los productos
        self.productos = []

    # Añadir producto
    def agregar_producto(self, producto):
        # Verificar que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print("✅ Producto agregado correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

        if encontrados:
            for p in encontrados:
                p.mostrar()
        else:
            print("❌ No se encontraron productos.")

    # Mostrar todos los productos
    def mostrar_inventario(self):
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        for p in self.productos:
            p.mostrar()
