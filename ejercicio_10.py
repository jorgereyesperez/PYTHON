print("=== PROGRAMA: GESTIÓN DE CALIFICACIONES ===\n")

# Estructura inicial del diccionario
estudiantes = {
    "Ana": [8, 9, 7],
    "Carlos": [6, 8, 9],
    "Elena": [9, 9, 8]
}

print("=== DICCIONARIO INICIAL ===")
print("Estudiantes y sus calificaciones:")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificaciones}")

print("\n=== OPERACIÓN 1: AÑADIR NUEVO ESTUDIANTE ===")
# 1. Añade un nuevo estudiante con sus calificaciones al diccionario
# Escribe aquí tu código
estudiantes["Jorge"] = [9,9,9]

print("Diccionario actualizado:")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificaciones}")

print("\n=== OPERACIÓN 2: CALCULAR PROMEDIOS ===")
# 2. Calcula y muestra el promedio de calificaciones de cada estudiante
# Escribe aquí tu código
promedios = {}
for nombre, calificaciones in estudiantes.items():
   promedio = sum(calificaciones) / len(calificaciones)
   promedios[nombre] = promedio
   print(f"{nombre}: {promedio:.2f}")



print("\n=== OPERACIÓN 3: ENCONTRAR MEJOR ESTUDIANTE ===")
# 3. Identifica y muestra el nombre del estudiante con el promedio más alto
# Escribe aquí tu código
mejor_estudiante = max(promedios, key=promedios.get)
mejor_promedio = promedios[mejor_estudiante]
print(f"El estudiante con el promedio más alto es {mejor_estudiante} con un promedio de {mejor_promedio:.2f}")
