import os 
#0.Crear carpeta principal e hijos
def crear_carpeta_principal():
    nom_carpeta = input("Ingrese el nombre de la carpeta principal: ")
    if not os.path.exists(nom_carpeta):
        os.makedirs(nom_carpeta)
        print(f"Carpeta '{nom_carpeta}' creada exitosamente.")
    else:
        print(f"La carpeta '{nom_carpeta}' ya existe.")
#1. Crear o añadir contenido a un archivo
def crear_o_añadir_archivo():
    N_arch=input("Ingrese el nombre del archivo (con extensión): ")
    if not os.path.exists(N_arch):
        with open(N_arch, 'w') as f:
            contenido = input("Ingrese el contenido del archivo: ")
            f.write(contenido)
    else:
        print ("El archivo ya existe. Desea añadir contenido? (s/n)")
        respuesta = input("Ingrese 's' para sí o 'n' para no: ")
        if respuesta.lower() == 's':
            with open(N_arch, 'a') as f:
                contenido = input("Ingrese el contenido a añadir: ")
                f.write(contenido)
#2. Listar archivos y carpetas del último nivel creado.
def listar_archivos_y_carpetas():
    ruta = os.getcwd()
 
    if os.path.exists(ruta):
        for item in os.listdir(ruta):
            print("Archivos y carpetas en el directorio:")
            print(item)
    else:
        print("La ruta especificada no existe.")
#3. Renombrar un archivo.
def renombrar_archivo():
    ruta = input("Ingrese la ruta del archivo a renombrar: ")
    if os.path.exists(ruta):
        nuevo_nombre = input("Ingrese el nuevo nombre del archivo (con extensión): ")
        os.rename(ruta, os.path.join(os.path.dirname(ruta), nuevo_nombre))
        print(f"Archivo renombrado a {nuevo_nombre}")
    else:
        print("El archivo especificado no existe.")
#4. Salir del programa.
def main():
    while True:
        print("\nOpciones:")
        print("1. Crear carpeta principal e hijos")
        print("2. Crear o añadir contenido a un archivo")
        print("3. Listar archivos y carpetas del último nivel creado")
        print("4. Renombrar un archivo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            crear_carpeta_principal()
        elif opcion == '2':
            crear_o_añadir_archivo()
        elif opcion == '3':
            listar_archivos_y_carpetas()
        elif opcion == '4':
            renombrar_archivo()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")
if __name__ == "__main__":
    main()
    