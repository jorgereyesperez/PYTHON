import math

cantidad = 5
id = 34
precio = 50
descripcion = "Compra de {} piezas de producto con id {} a precio {:.2f} $"
print (descripcion.format(cantidad,id,precio))

while True:
    print("""
          welcome
          Elige una opción:
          1- Mostrar productos
          2- Buscar un producto
          salir- Salir del programa
          """)
    opcion = input("Introduce una opción: ")
    print(f"Has elegido la opción: {opcion}")
    if opcion == "salir":
        print("Hasta la proxima")
        break
print ("Fuera del bucle")

nombres = []

def guardar_nombre(nombre):
 nombres.append(nombre)
 print(f"Insertado {nombre} en la lista, ahora hay {len(nombres)} nombres.")


guardar_nombre("Patricia")
guardar_nombre("Jorge")
guardar_nombre("Pablo")

matriculas = ["1111AAA", "2222BBB", "3333CCC"]

def guardar_matriculas(matriculas_nuevas):
 matriculas.extend(matriculas_nuevas) # se van a fusionar las listas

guardar_matriculas(["4444DDD", "5555EEE"])
print(matriculas)