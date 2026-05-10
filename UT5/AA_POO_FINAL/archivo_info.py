import os
import time

class InfoArchivo:
    def __init__(self, ruta):
        self.__ruta = ruta # Atributo privado (Encapsulamiento)
        
    def obtener_detalles(self):
        """Justificación: 'os.path' permite obtener metadatos reales del disco."""
        if not os.path.exists(self.__ruta):
            return "El archivo no existe."
            
        stats = os.stat(self.__ruta)
        tamaño = stats.st_size
        # Justificación: 'time.ctime' convierte segundos de sistema en fechas legibles
        fecha_mod = time.ctime(stats.st_mtime)
        
        return f"Tamaño: {tamaño} bytes | Última modificación: {fecha_mod}"