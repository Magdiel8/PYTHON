#creando app para modificar ip
import subprocess

try:
    sis = input("Indica el sistema operativo (windows/linux): ")
    ip = input("Indica  dirección IP: ")             
    mascara = input("Indica la máscara de subred: ")
    gateway = input("Indica la puerta de enlace predeterminada: ")
    if (sis=="windows") 
        subprocess.run(["cmd","/c","netsh","interface","ip","set","address","name=\"Ethernet\"","static",ip,mascara,gateway], shell=True)
        resulW=subprocess.run(["cmd","/c","ipconfig","/all"], capture_output=True, text=True)
        print(resulW.stdout)
    elif (sis=="linux") subprocess.run(["sudo","ifconfig","eth0",ip,"netmask",mascara], shell=True)
     resltl=subprocess.run(["ifconfig"], capture_output=True, text=True)
        print(resltl.stdout)
   
    else: print("Sistema operativo no soportado")
except ValueError: