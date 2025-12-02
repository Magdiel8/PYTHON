import os

dirP=input("Introduce el nombre del directorio principal a crear: ")
os.mkdir(dirP, exist_ok=True)
print("Directorio principal " ,dirP, "creado.")

while True:
    print("\nOpciones:")
  
    