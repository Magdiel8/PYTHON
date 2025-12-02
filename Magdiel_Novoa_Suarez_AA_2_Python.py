
try:
    ip = input("ponga la ip: ")
    numPuerto = int(input("ponga el puerto: "))
    masc = input("ponga la mascara: ")
    lat = int(input("diga la latencia: "))
    ser = input("Es unservidor? (s/n): ")
except ValueError:
    print("Error en la entrada de datos")
    ip = "127.0.0.0"
    numPuerto = 0
    masc = "255.0.0.0"
    lat = 0
    ser = "n"

print("Datos ingresados son :", ip, numPuerto, masc, lat, "ms", ser)