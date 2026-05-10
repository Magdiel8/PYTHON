import time

def simular_espera(segundos, mensaje="Procesando"):
    """Justificación: Se usa 'time' para simular latencia en operaciones de sistema."""
    print(f"{mensaje}", end="", flush=True)
    for _ in range(segundos):
        time.sleep(1) # Detiene la ejecución un segundo
        print(".", end="", flush=True)
    print("\n¡Operación completada!")