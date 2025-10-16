print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        # Inicializar atributos básicos
        # Escribe aquí tu código
        
        
        
    
    def mostrar_info(self):
        return f"Producto: {self.nombre} {self.precio} {self.stock}"
        # Devolver información básica del producto
        # Escribe aquí tu código
        
    
    def hay_stock(self):
        return self.stock > 0
        # Verificar si hay unidades disponibles
        # Escribe aquí tu código
        

# Clase Alimento que hereda de Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        super().__init__(nombre, precio, stock)
        self.fecha_caducidad = fecha_caducidad
        # Llamar al constructor de la clase padre
        # Escribe aquí tu código
        
        # Inicializar atributo específico de Alimento
        # Escribe aquí tu código
        
    
    def mostrar_info(self):
        return f"Alimento: {self.nombre} {self.precio} {self.stock} {self.fecha_caducidad}"
        # Sobreescribir el método para incluir fecha de caducidad
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        


# Clase Electronico que hereda de Producto
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia = garantia
        # Llamar al constructor de la clase padre
        # Escribe aquí tu código
        
        # Inicializar atributo específico de Electronico
        # Escribe aquí tu código
        
    
    def mostrar_info(self):
        return f"Electronico: {self.nombre} {self.precio} {self.stock} {self.garantia}"
        # Sobreescribir el método para incluir información de garantía
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PRODUCTOS ===")

# Crear una instancia de Producto genérico
# Escribe aquí tu código
producto_generico = Producto("Genérico", 10.00, 5)

# Crear una instancia de Alimento
# Escribe aquí tu código
alimento = Alimento("Pan integral", 2.50, 12, "2025-11-01")

# Crear una instancia de Electronico
# Escribe aquí tu código
electronico = Electronico("Tablet 10\"", 199.99, 8, 18)

print("\n=== INFORMACIÓN DE PRODUCTOS ===")

# Mostrar información del producto genérico
# Escribe aquí tu código
print(producto_generico.mostrar_info())

# Mostrar información del alimento
# Escribe aquí tu código
print(alimento.mostrar_info())


# Mostrar información del electrónico
# Escribe aquí tu código
print(electronico.mostrar_info())

print("\n=== VERIFICANDO STOCK ===")

# Verificar stock de cada producto
# Escribe aquí tu código
print(f"{producto_generico.nombre} tiene stock?: {producto_generico.hay_stock()}")
print(f"{alimento.nombre} tiene stock?: {alimento.hay_stock()}")
print(f"{electronico.nombre} tiene stock?: {electronico.hay_stock()}")

