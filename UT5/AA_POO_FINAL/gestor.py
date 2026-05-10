import os
import shutil
from utilidades import simular_espera
from archivo_info import InfoArchivo

class GestorArchivos:
    def __init__(self):
        # Atributo protegido: Ruta donde opera el gestor
        self._directorio_base = os.getcwd() 

    def crear_carpeta(self, nombre):
        """Justificación: 'os.makedirs' asegura la creación incluso de rutas anidadas."""
        try:
            os.makedirs(nombre, exist_ok=True)
            print(f"Carpeta '{nombre}' creada con éxito.")
        except Exception as e:
            print(f"Error al crear carpeta: {e}")

    def listar_contenido(self):
        """Justificación: 'os.listdir' es fundamental para visualizar el árbol de directorios."""
        elementos = os.listdir(self._directorio_base)
        print(f"\nContenido en {self._directorio_base}:")
        for item in elementos:
            tipo = "[DIR]" if os.path.isdir(item) else "[FILE]"
            print(f" {tipo} {item}")

    def eliminar_elemento(self, nombre):
        """Justificación: Se usa 'shutil' para carpetas y 'os' para archivos individuales."""
        simular_espera(2, f"Eliminando {nombre}")
        if os.path.isdir(nombre):
            shutil.rmtree(nombre)
        elif os.path.isfile(nombre):
            os.remove(nombre)
        else:
            print("El elemento no existe.")

    def mostrar_info(self, nombre):
        info = InfoArchivo(nombre)
        print(info.obtener_detalles())