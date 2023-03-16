#No sabemos la cantidad de parametros que vamos a recibir
def listarNombre(*nombres):
    for nombre in nombres:
        print((nombre))


#Es una tupla y recordar que las tuplas son inmutables por lo que no se pueden modifcar

listarNombre('juan','Pedro','Lucia','Jorge','Mario')