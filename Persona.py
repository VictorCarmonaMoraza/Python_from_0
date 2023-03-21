#Creacion de la clase Persona
class Persona:
  """

  """
  def __init__(self, nom, apelli, age):
    self._nombre = nom
    self.apellido = apelli
    self.edad = age

  @property
  def nombre(self):
    print('Llamando metodo get nombre')
    return self._nombre

  #@nombre.setter
  #def nombre(self, nombre):
  #  print('LLamando metodo set nombre', nombre)
  #  self._nombre = nombre

  #Metodo de nuestra clase
  def mostrar_detalle(self):
    print(f'Persona : {self._nombre} {self.apellido} {self.edad}')


#Creamos un objeto de esta clase
#Forma 1
persona1 = Persona('Adris','Garcia', 45)
#persona1.mostrar_detalle()
#LLamada al metodo getter
print(persona1.nombre)

#LLamada al metodo setter
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)



