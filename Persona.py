#Creacion de la clase Persona
class Persona:
  """

  """
  def __init__(self, nom, apelli, age):
    self.__nombre = nom
    self.apellido = apelli
    self.edad = age

  #Metodo de nuestra clase
  def mostrar_detalle(self):
    print(f'Persona : {self.__nombre} {self.apellido} {self.edad}')


#Creamos un objeto de esta clase
#Forma 1
persona1 = Persona('Adris','Garcia', 45)
persona1.mostrar_detalle()


