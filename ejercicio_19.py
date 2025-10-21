print("=== EJERCICIO: RELACIÓN CARPETA-ARCHIVOS ===\n")

# 1. Crear la clase Carpeta con los atributos: id, nombre, fecha_creacion
# El atributo 'archivos' debe inicializarse como una lista vacía
class Carpeta:
    def __init__(self, id, nombre, fecha_creacion):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.archivos = []
    def __str__(self):
        archivos_info = ', '.join([archivo.nombre for archivo in self.archivos]) if self.archivos else 'Sin archivos'
        return f"id: {self.id}, Carpeta: {self.nombre}, Fecha de creacion: {self.fecha_creacion}, Archivos: {archivos_info}"
        # Escribe aquí tu código

# 2. Crear la clase Archivo con los atributos: id, nombre, extension, tamaño, carpeta_id
class Archivo:
    def __init__(self, id, nombre, extension, tamaño, carpeta_id):
        self.id = id
        self.nombre = nombre
        self.extension = extension
        self.tamaño = tamaño
        self.carpeta_id = carpeta_id
        self.carpeta = None
    def __str__(self):
        return f"id: {self.id}, Nombre: {self.nombre}, Extension: {self.extension}, Tamaño: {self.tamaño}, id carpeta: {self.carpeta_id}, Carpeta: {self.carpeta.nombre if self.carpeta else 'Sin carpeta'}"
        # Escribe aquí tu código

print("=== CREANDO OBJETOS ===")

# 3. Crear una carpeta con id: 1, nombre: Proyecto Aviberico, fecha de creación: 2025-01-15
Carpeta1 = Carpeta(1, "Proyecto Aviberico", "2025-01-15")

# 4. Crear tres archivos:
# - id: 1, nombre: main, extensión: py, tamaño: 1024, id de carpeta: 1
# - id: 2, nombre: config, extensión: json, tamaño: 512, id de carpeta: 1
# - id: 3, nombre: readme, extensión: md, tamaño: 256, id de carpeta: 1
Archivo1 = Archivo(1, "main", "py", 1024, 1)
Archivo2 = Archivo(2, "config", "json", 512, 1)
Archivo3 = Archivo(3, "readme", "md", 256, 1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Agregar los archivos a la carpeta (relación one-to-many)
Archivo1.carpeta = Carpeta1
Archivo2.carpeta = Carpeta1
Archivo3.carpeta = Carpeta1
Carpeta1.archivos.extend([Archivo1, Archivo2, Archivo3])

#Carpeta1.archivos.append(Archivo1)
#Carpeta1.archivos.append(Archivo2)
#Carpeta1.archivos.append(Archivo3)

print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información de la carpeta y sus archivos
# Hay que mostrar:
# - Nombre de la carpeta
# - Número total de archivos
# - Lista de archivos con sus detalles
# - Verificar que la relación es bidireccional
print(Carpeta1)
print(Archivo1)
print(Archivo2)
print(Archivo3)
for archivo in Carpeta1.archivos:
    print (f"{Archivo.nombre}| {Archivo.extension}|{Archivo.tamaño} bytes")

print("\n=== RESULTADO FINAL ===")
if Archivo1.carpeta == Carpeta1 and Archivo2.carpeta == Carpeta1 and Archivo3.carpeta == Carpeta1:
    print(f" Relación many-to-one establecida correctamente entre la carpeta {Carpeta1.nombre} y los archivos.")
else:
    print(" La relación one-to-many no se ha establecido correctamente.")
# 7. Mostrar un mensaje confirmando la relación one-to-many