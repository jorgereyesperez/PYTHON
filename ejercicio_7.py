def dividir_numeros():
    try:

        # Solicitar al usuario que introduzca dos números
        numero1 = input("Introduce un numero cualquiera")
        numero2 = input("Introduce un numero cualquiera")
        # Convertir las entradas a números enteros
        numero_1 = int (numero1)
        numero_2 = int (numero2)
        # Realizar la división del primer número entre el segundo
        resultado = numero_1/numero_2
        # Devolver el resultado de la división
        print(f"El resultado de la división es: {resultado}")
        return resultado
    
    except ZeroDivisionError:
     print("Error: No es posible dividir entre cero.")
    except ValueError:
     print("Error: Debes introducir un número válido.")
    finally:
     print("Operación finalizada.")

# Llamada a la función
dividir_numeros()