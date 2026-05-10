from gestor import GestorArchivos

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN POO ---")
    print("1. Crear carpeta")
    print("2. Listar contenido")
    print("3. Eliminar archivo/carpeta")
    print("4. Ver información detallada")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")

def main():
    gestor = GestorArchivos()
    
    # Inicializamos la variable vacía antes de entrar al bucle
    opcion = ""  
    
    # El bucle se repite siempre y cuando la opción NO sea "5"
    while opcion != "5":
        opcion = mostrar_menu()
        
        match opcion:
            case "1":
                nombre = input("Nombre de la nueva carpeta: ")
                gestor.crear_carpeta(nombre)
            case "2":
                gestor.listar_contenido()
            case "3":
                nombre = input("Nombre del elemento a eliminar: ")
                gestor.eliminar_elemento(nombre)
            case "4":
                nombre = input("Nombre del archivo para ver info: ")
                gestor.mostrar_info(nombre)
            case "5":
                print("Cerrando el gestor de archivos. ¡Hasta luego!")
                # Al ser "5", el match-case termina aquí, y al volver arriba,
                # el while evalúa que opcion ya es "5", por lo que el bucle finaliza solo.
            case _:
                print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()