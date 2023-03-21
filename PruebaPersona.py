from Persona import Persona
#Si queremos importar todas las clases que se encuentran en un archivo lo hacemos de la forma
# from Persona import *

#Comporbar que estamos dentro de nuestra clase principal
if __name__ == '__main__':
    persona1 = Persona('Karla','gomez',30)
    persona1.mostrar_detalle()


print(__name__)