import subprocess

try:
    pre = input("elige sistema operativo: ")


    match pre:
          case "1":
                print ("sistema operativo windows")
                coma =input("Ingrese el comando que va a usar: ")
                p= subprocess.run( coma,check=True,capture_output=True, text=True,shell=True )
                print("Salida del comando:", p.stdout)

          case "2":
                   print ("sistema operativo linux")
                   coma =input("Ingrese el comando que va a usar: ")
                   print("Salida del comando: Satisfactorio")


            
          case "3":
            print ("sistema operativo mac")
            coma =input("Ingrese el comando que va a usar: ")
            print("Salida del comando: Satisfactorio")

           
          case _:
            print("sistema operativo no reconocido")
except Exception as e:
 print("Error en la ejecucion del comando:", e)
