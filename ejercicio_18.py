print("=== EJERCICIO: RELACIÓN HABITACIONES-HOTEL ===\n")

# 1. Crear la clase Hotel con los atributos: id, nombre, direccion, estrellas
# El atributo 'habitaciones' debe inicializarse como una lista vacía
class Hotel:
    def __init__(self, id, nombre, direccion, estrellas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.estrellas = estrellas
        self.habitaciones = []  # Lista para almacenar las habitaciones

    def __str__(self):
        habitaciones_info = ', '.join([str(habitacion.numero) for habitacion in self.habitaciones]) if self.habitaciones else 'Sin habitaciones'
        return f"id: {self.id}, Hotel: {self.nombre}, Dirección: {self.direccion}, Estrellas: {self.estrellas}, Habitaciones: {habitaciones_info}"

# 2. Crear la clase Habitacion con los atributos: id, numero, tipo, precio, hotel_id
class Habitacion:
    def __init__(self, id, numero, tipo, precio, hotel_id):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.hotel_id = hotel_id
        self.hotel = None  # Relación inversa con el hotel

    def __str__(self):
        return f"id: {self.id}, Habitacion: {self.numero}, Tipo: {self.tipo}, Precio: {self.precio}, Hotel: {self.hotel.nombre if self.hotel else 'Sin hotel'}"

print("=== CREANDO OBJETOS ===")

# 3. Crear un hotel con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4
Hotel1 = Hotel(1, "Hotel Carbonero", "Plaza Parus Mayor 123", 4)

# 4. Crear tres habitaciones
Habitacion1 = Habitacion(1, 101, "Individual", 80, 1)
Habitacion2 = Habitacion(2, 102, "Doble", 120, 1)
Habitacion3 = Habitacion(3, 103, "Suite", 200, 1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Agregar las habitaciones al hotel (relación many-to-one)
Habitacion1.hotel = Hotel1
Habitacion2.hotel = Hotel1
Habitacion3.hotel = Hotel1

Hotel1.habitaciones.append(Habitacion1)
Hotel1.habitaciones.append(Habitacion2)
Hotel1.habitaciones.append(Habitacion3)

print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del hotel y sus habitaciones
print(Hotel1)
print(Habitacion1)
print(Habitacion2)
print(Habitacion3)

print("\n=== RESULTADO FINAL ===")

# 7. Confirmar la relación many-to-one
if Habitacion1.hotel == Hotel1 and Habitacion2.hotel == Hotel1 and Habitacion3.hotel == Hotel1:
    print(f" Relación many-to-one establecida correctamente entre el hotel {Hotel1.nombre} y las habitaciones.")
else:
    print(" La relación many-to-one no se ha establecido correctamente.")
