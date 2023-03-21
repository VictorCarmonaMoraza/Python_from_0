from Persona import Persona
#Si queremos importar todas las clases que se encuentran en un archivo lo hacemos de la forma
# from Persona import *


print('Creacion de objetos'.center(50,'-'))
persona1 = Persona('Karla','gomez',30)
persona1.mostrar_detalle()

print(__name__)
print('Eliminacion de objetos'.center(30,'-'))
#Eliminacion de objeto
del persona1

