#Creacion de la clase Persona
class Persona:
  """

  """
  def __init__(self, nom, apelli, age, *valores, **terminos):
    self.nombre = nom
    self.apellido = apelli
    self.edad = age
    self.valores =valores
    self.terminos = terminos

  #Metodo de nuestra clase
  def mostrar_detalle(self):
    print(f'Persona : {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


#Creamos un objeto de esta clase
#Forma 1
persona1 = Persona('Victor','Carmona', 45, 2,3,5, m='manzana', p='pera')
persona1.mostrar_detalle()



#Forma 2
persona2 = Persona('jorge','Perez',2515)
persona2.mostrar_detalle()

