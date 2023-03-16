# Sumar argumentos variables

resultado: int = 0


def  multiplicarArgumentos(*valores) -> int:
    resultado = 1
    for valor in valores:
        resultado *= valor
    return resultado



print(multiplicarArgumentos(1, 2, 3, 4, 5, 6, 7))
