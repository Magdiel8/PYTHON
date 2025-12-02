import os
import platform
#Mostrar información del sistema operativo
def mostrar_info_sistema():
    sistema = platform.system()
    version = platform.version()
    print(f"Sistema Operativo: {sistema}")
    print(f"Versión del Sistema Operativo: {version}")
#Guardar y mostrar el directorio de trabajo actual.
def mostrar_directorio_actual():
    directorio_actual = os.getcwd()
    print(f"Directorio de trabajo actual: {directorio_actual}")
#Crear un directorio principal llamado "proyecto".
def crear_directorio():
    os.makedirs("proyecto", exist_ok=True)
    print("Directorio 'proyecto' creado.")
#Entrar al directorio "proyecto" y mostrar la nueva ruta actual.
#Dentro de "proyecto" crear dos subdirectorios:◦ "docs"◦ "src"
#Entrar en "src" y crear un subdirectorio llamado "modulos".
#Volver al directorio original desde donde se ejecutó el programa.
#Realizar un listado recursivo del directorio "proyecto", usando:◦ dir /s en Windows◦ ls -lR en Linux o macOS

