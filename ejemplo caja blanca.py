def suma(a, b):
    return a + b

def test_suma():
    resultado1 = suma(3, 4)
    print(f"Resultado de la suma de 3 y 4: {resultado1}")

    resultado2 = suma(5, 0)
    print(f"Resultado de la suma de 5 y 0: {resultado2}")

    resultado3 = suma(-2, -3)
    print(f"Resultado de la suma de -2 y -3: {resultado3}")

test_suma()
