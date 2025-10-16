print("=== PROGRAMA: POLIMORFISMO CON VEHÍCULOS ===\n")

# Clase base Vehiculo
class Vehiculo:
    def desplazarse(self):
        print("El vehiculo se desplaza de un punto A a un punto B")
        # Implementar mensaje genérico de desplazamiento
        # Escribe aquí tu código
        

# Clase Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def desplazarse(self):
        print ("El coche va por la carretera")
        # Sobreescribir el método para mostrar cómo se desplaza un coche
        # Escribe aquí tu código
        

# Clase Barco que hereda de Vehiculo
class Barco(Vehiculo):
    def desplazarse(self):
        print("El barco zarpa desde el puerto")
        # Sobreescribir el método para mostrar cómo se desplaza un barco
        # Escribe aquí tu código
        

# Clase Avion que hereda de Vehiculo
class Avion(Vehiculo):
    def desplazarse(self):
        print("El avión despega desde el aeropuerto")
        # Sobreescribir el método para mostrar cómo se desplaza un avión
        # Escribe aquí tu código
        

# Función que demuestra polimorfismo
def iniciar_viaje(vehiculo):
    vehiculo.desplazarse()
    # Llamar al método desplazarse() del vehículo recibido
    # Escribe aquí tu código
    

# === CREACIÓN DE INSTANCIAS ===
print("=== CREANDO VEHÍCULOS ===")

# Crear una instancia de cada tipo de vehículo
# Escribe aquí tu código para crear el vehículo genérico
vehiculo_generico = Vehiculo()


# Escribe aquí tu código para crear el coche
coche = Coche()

# Escribe aquí tu código para crear el barco
barco = Barco()

# Escribe aquí tu código para crear el avión
avion = Avion()

print("✓ Vehículos creados exitosamente")

print("\n=== DEMOSTRANDO POLIMORFISMO ===")

# Crear una lista con todos los vehículos
# Escribe aquí tu código
Vehiculos = [vehiculo_generico, coche, barco, avion]

# Usar la función iniciar_viaje() con cada vehículo
# Escribe aquí tu código para iterar sobre los vehículos
for v in Vehiculos:
    iniciar_viaje (v)

print("\n=== PRUEBAS INDIVIDUALES ===")

# Llamar a iniciar_viaje() con cada vehículo individualmente
# Escribe aquí tu código
iniciar_viaje(coche)
iniciar_viaje(avion)
iniciar_viaje(barco)
iniciar_viaje(vehiculo_generico)