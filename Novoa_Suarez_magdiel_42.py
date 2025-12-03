import os
import platform

def mostrar_info_sistema():
    sistema = platform.system()
    version = platform.version()
    print(f"Sistema Operativo: {sistema}")
    print(f"Versión del Sistema Operativo: {version}")

def mostrar_directorio_actual():
    directorio_actual = os.getcwd()
    print(f"Directorio de trabajo actual: {directorio_actual}")

def crear_directorio():
    os.makedirs("proyecto", exist_ok=True)
    print("Directorio 'proyecto' creado.")

def entrar_directorio():
    os.chdir("proyecto")
    print(f"Entrado al directorio: {os.getcwd()}")

def crear_subdirectorios():
    os.makedirs("docs", exist_ok=True)
    os.makedirs("src", exist_ok=True)
    print("Subdirectorios 'docs' y 'src' creados en 'proyecto'.")

def crear_modulos():
    os.chdir("src")
    os.makedirs("modulos", exist_ok=True)
    print("Subdirectorio 'modulos' creado en 'src'.")

def volver_directorio():
    os.chdir("..")  
    print(f"Volviendo al directorio: {os.getcwd()}")

def listar_directorio():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("dir /s")
    else:
        os.system("ls -lR")    
def main():
    mostrar_info_sistema()
    mostrar_directorio_actual()
    crear_directorio()
    entrar_directorio()
    crear_subdirectorios()
    crear_modulos()
    volver_directorio()
    listar_directorio()
if __name__ == "__main__":
    main()