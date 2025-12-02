def suma(a, b):
    return a + b

def prueba_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    print("Todas las pruebas pasaron.")

if __name__ == "__main__":
    prueba_suma()