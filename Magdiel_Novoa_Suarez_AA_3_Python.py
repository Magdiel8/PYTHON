
try:
    nomRed = input("ingrese el nombre de la red: ")
    ancho = float(input("ingrese el ancho de banda(MHz):  "))
    tipo_seguridad = input("ingrese el tipo de seguridad(WPA2,3 o abierta): ")
    conex = input("esta conectado el equipo a la red? (si/no): ")
except ValueError:
    print("Error en la entrada de datos")
    nomRed = "desconocida"
    ancho = 0.0
    tipo_seguridad = "indefinida"
    conex = "no"

print("Datos ingresados son :\nNombre de la wifi: ", nomRed,"\nAncho de banda: ", ancho,"MHz", "\ntipo seguridad: ",tipo_seguridad,"\nconecatado a una red: ", conex)

