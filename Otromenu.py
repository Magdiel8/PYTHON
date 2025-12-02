#eleccion de explorador

try:
    el=input("elige explorador (1 chrome, 2 firefox, 3 edge, 4 Safari): ")
    if el.isdigit():
     el=int(el)
     match el:
            case 1:
                     print("haz elegido chrome")
                     input("que deseas buscar: ")
                     print("buscando...")
            case 2:
                     print("haz elegido firefox")
                     input("que deseas buscar: ")
                     print("buscando...")
            case 3:
                 print("haz elegido edge")
                 input("que deseas buscar: ")
                 print("buscando...")
            case 4:
                 print("haz elegido Safari")
                 input("que deseas buscar: ")
                 print("buscando...")
            case _:
                 print("explorador no reconocido")
    else:   print("debes ingresar un numero del 1 al 4 Ejemplo 1 2 3 4 ")

except Exception as e:
    print("ha ocurrido un error:", e)