def filtrar_mayores(lista, umbral):

    resultado = []
    
    for num in lista:
        if num > umbral:
            resultado.append(num)
    
    return resultado


if __name__ == "__main__":
    numeros1 = [5, 10, 15, 20]
    numeros2 = [1, 2, 3]
    print(filtrar_mayores(numeros1, 12))
    print(filtrar_mayores(numeros2, 5))    
    
#def filtrar_mayores(lista, umbral):
    #"""Devuelve una nueva lista con los números mayores que el umbral."""
    #return [num for num in lista if num > umbral]