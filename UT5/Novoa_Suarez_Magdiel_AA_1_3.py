class libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrar_info(self):
        estado = "prestado" if self.prestado else "disponible"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Estado: {estado}")

    def cambiar_autor(self, nuevo_autor):
        self.autor = nuevo_autor
        print(f"El autor del libro '{self.titulo}' ha sido cambiado a {nuevo_autor}.")
#Comprobamos los funcionamientos de la clases 
libro1 = libro("The lord of the rings", "J.R.R. Tolkien")
libro2 = libro("Decameron", "Giovanni Boccaccio")
libro3 = libro("Metamorphosis", "Franz Kafka")

#prestamos simple 
libro1.prestar()
libro1.mostrar_info()

#prestamos el mismo libro
libro1.prestar()
libro1.mostrar_info()

#devolver
libro1.devolver()
libro1.mostrar_info()

#cambiar autor
libro2.mostrar_info()
libro2.cambiar_autor("Dante Alighieri")
libro2.mostrar_info()
