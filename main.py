# Sumar argumentos variables

resultado: int = 0


def sumarArgumentos(*valores) -> int:
    resultado = 0
    for valor in valores:
        resultado += valor
    return resultado


# sumarArgumentos(1, 2, 3, 4, 5, 6, 7)
print(sumarArgumentos(1, 2, 3, 4, 5, 6, 7))
