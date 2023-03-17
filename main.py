

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

#Itera todos los elementos
nombres = ['Juan','Carla','Guillermo']
desplegarNombres(nombres)

#Itera todas las letras del nombre cuando solo es una variable
desplegarNombres('Carlos')
#Tupla
desplegarNombres((10, 11))
#Lista
desplegarNombres([10, 11])