# Solicitar la edad al usuario
edad = input("Escriba su edad:")
# Convertir la entrada a entero
edad = int (edad)
# Evaluar la edad usando if-elif-else
if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
# Mostrar el mensaje correspondiente

# != es distinto o diferente