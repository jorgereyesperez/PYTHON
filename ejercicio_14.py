#Crea una clase CuentaBancaria que implemente el concepto de encapsulación. 
#La clase debe tener los siguientes atributos privados: _titular (string) y _saldo (float). 
# Implementa propiedades para acceder y modificar estos atributos de forma controlada:

#La propiedad titular debe permitir obtener el valor pero no modificarlo (solo lectura).
#La propiedad saldo debe permitir obtener el valor y modificarlo, 
# pero con la restricción de que no se pueda establecer un saldo negativo 
# (debe lanzar un ValueError con el mensaje "El saldo no puede ser negativo").
#Añade un método depositar(cantidad) que incremente el saldo solo si la cantidad es positiva, 
#devolviendo True si la operación fue exitosa o False en caso contrario.
#Añade un método retirar(cantidad) que disminuya el saldo 
# solo si hay suficiente dinero, devolviendo True si la operación fue exitosa o False 
# en caso contrario.
#La clase debe inicializarse con un titular y un saldo inicial (que por defecto será 0).

print("=== PROGRAMA: SISTEMA DE CUENTA BANCARIA ===\n")

class CuentaBancaria:
    # Constructor de la clase
    def __init__(self, titular, saldo=0.0):
        self._titular = titular
        self._saldo = saldo
        # Inicializar atributos privados
        # Escribe aquí tu código para _titular
        # Escribe aquí tu código para _saldo (usa la propiedad setter)

    
    # Propiedad para el titular (solo lectura)
    @property
    def titular(self):
       return self._titular
        # Escribe aquí tu código para retornar el titular
        
    
    # Propiedad getter para el saldo
    @property
    def saldo(self):
        return self._saldo
        # Escribe aquí tu código para retornar el saldo
        
    
    # Propiedad setter para el saldo (con validación)
    @saldo.setter
    def saldo(self, nuevo_saldo):
         if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo
         else:
            raise ValueError("El saldo no puede ser negativo")
        # Verificar que el saldo no sea negativo
        # Escribe aquí tu código para la validación
        
        # Si es válido, asignar el nuevo saldo
        # Escribe aquí tu código
        
    
    # Método para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False
        # Verificar que la cantidad sea positiva
        # Escribe aquí tu código para la validación
        
            # Incrementar el saldo
            # Escribe aquí tu código
            
            # Retornar True indicando éxito
            # Escribe aquí tu código
            
        # Si la cantidad no es válida, retornar False
        # Escribe aquí tu código
        
    
    # Método para retirar dinero
    def retirar(self, cantidad):
        # Verificar que la cantidad sea positiva y que haya suficiente saldo
        # Escribe aquí tu código para las validaciones
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False
            # Disminuir el saldo
            # Escribe aquí tu código
            
            # Retornar True indicando éxito
            # Escribe aquí tu código
            
        # Si no se puede retirar, retornar False
        # Escribe aquí tu código
        

# === PRUEBAS DE LA CLASE ===
print("=== CREANDO CUENTA BANCARIA ===")
# Crear una cuenta bancaria
# Escribe aquí tu código
cuenta = CuentaBancaria("Juan Pérez", 1000.0)

print(f"Titular: {cuenta.titular}")
print(f"Saldo inicial: ${cuenta.saldo}")

print("\n=== PROBANDO DEPÓSITOS ===")
# Probar depósito válido
# Escribe aquí tu código
cuenta.depositar(500)
print(cuenta.saldo)

# Probar depósito inválido
# Escribe aquí tu código
cuenta.depositar(-500)
print(cuenta.saldo)

print(f"Saldo después de operaciones: ${cuenta.saldo}")

print("\n=== PROBANDO RETIROS ===")
# Probar retiro válido
# Escribe aquí tu código
cuenta.retirar(1000)
print(cuenta.saldo)
# Probar retiro que excede el saldo
# Escribe aquí tu código
cuenta.retirar(2000)
print(cuenta.saldo)


print(f"Saldo final: ${cuenta.saldo}")

print("\n=== PROBANDO VALIDACIONES ===")
# Intentar establecer un saldo negativo
try:
   cuenta.saldo = -100
   print("Error: No se lanzó una excepción al asignar saldo negativo.")
   # Escribe aquí tu código para probar saldo negativo
    
except ValueError as e:
    print(f"Error capturado: {e}")