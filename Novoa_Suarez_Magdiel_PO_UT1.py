import subprocess       

coma =input("Ingrese el comando que va a usar: ")

try:
    p= subprocess.run(
        coma,check=True,capture_output=True, text=True,shell=True
    )
    
    print("Salida del comando:", p.stdout)


except Exception as e:
    print("Error en la ejecucion del comando:", e)
    print("Errores del comando:", p.stderr)
