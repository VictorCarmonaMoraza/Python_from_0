
#Funciones recursivas
def numerosDescendentes(numero):
    if numero >=1:
        print(numero)
        numerosDescendentes(numero -1)
    elif numero == 0:
        return
    elif numero <0:
        print('Valor incorrecto...')

resultado = numerosDescendentes(5)

print(resultado)
