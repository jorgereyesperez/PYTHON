class Libro:
    def __init__(self, titulo, autor, paginas, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible
        """
        Constructor de la clase Libro
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """
    
    def prestar(self):
        if self.disponible:
         self.disponible = False
         return f"{self.titulo} {self.autor} ha sido prestado"
        return f"{self.titulo} {self.autor} no está disponible para prestar"
    def devolver(self):
        if not self.disponible:
         self.disponible = True
         return f"{self.titulo} {self.autor} ha sido devuelto"
        return f"{self.titulo} {self.autor} ya estaba en la biblioteca"
    def informacion(self):
        return (
        f"{'Título:':<5} {self.titulo}\n"
        f"{'Autor:':<5} {self.autor}\n"
        f"{'Páginas:':<6} {self.paginas}\n"
        f"{'Disponible:':<12} {self.disponible}"
        )


# Prueba de la clase Libro
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
    
    # Mostrar información inicial de los libros
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")
    
    # Prestar los libros
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")
    
    # Intentar prestar un libro ya prestado
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print("\n")
    
    # Mostrar información después del préstamo
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")
    
    # Devolver un libro
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")
    
    # Intentar devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")
    
    # Mostrar información final
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())


if __name__ == "__main__":
    main()