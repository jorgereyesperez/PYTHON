print("=== EJERCICIO: RELACIÓN EMPLEADO-TARJETA CORPORATIVA ===\n")

# 1. Crear la clase Empleado con los atributos: id, nombre, cargo, salario
# El atributo 'tarjeta' debe inicializarse como None
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.tarjeta = None
    
    def __str__(self):
        return f"Empleado: {self.nombre}, Cargo: {self.cargo}, Salario: {self.salario}, Tarjeta: {self.tarjeta.numero if self.tarjeta else 'Sin tarjeta'}"
        # Escribe aquí tu código

# 2. Crear la clase TarjetaCorporativa con los atributos: id, numero, fecha_emision, empleado_id
class TarjetaCorporativa:
    def __init__(self, id, numero, fecha_emision, empleado_id):
        self.id = id
        self.numero = numero
        self.fecha_emision = fecha_emision
        self.empleado_id = empleado_id
        self.empleado = None
    def __str__(self):
        return f"Tarjeta: {self.numero}, Emitida: {self.fecha_emision}, Asignada a: {self.empleado.nombre if self.empleado else 'Sin asignar'}"
    
        # Escribe aquí tu código

print("=== CREANDO OBJETOS ===")

# 3. Crear un empleado con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 45000
Empleado1 = Empleado(1,"Alba Motacilla","Desarrolladora",45000)

# 4. Crear una tarjeta corporativa con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
TarjetaCorporativa1 = TarjetaCorporativa(1,"TC001","2025-01-15",Empleado1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Asignar la tarjeta al empleado (relación one-to-one)
Empleado1.tarjeta = TarjetaCorporativa1
TarjetaCorporativa1.empleado = Empleado1



print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del empleado y su tarjeta
# Hay para mostrar:
# - Nombre del empleado
# - Número de tarjeta
# - Verificar que la relación es bidireccional
print(Empleado1)
print(TarjetaCorporativa1)

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-one
if Empleado1.tarjeta == TarjetaCorporativa1 and TarjetaCorporativa1.empleado == Empleado1:
    print(f" Relación one-to-one establecida correctamente entre {Empleado1.nombre} y la tarjeta {TarjetaCorporativa1.numero}.")
else:
    print(" La relación one-to-one no se ha establecido correctamente.")
