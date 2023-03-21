#Creacion de la clase Persona
class Persona:
  """

  """
  def __init__(self, nom, apelli, age):
    self._nombre = nom
    self._apellido = apelli
    self._edad = age


  #Getter
  @property
  def nombre(self):
    print('Llamando metodo get nombre')
    return self._nombre

  #Setter
  @nombre.setter
  def nombre(self, nombre):
    print('LLamando metodo set nombre', nombre)
    self._nombre = nombre

  #Getter
  @property
  def apellido(self):
    return self._apellido

  #Setter
  @apellido.setter
  def apellido(self, apellido):
    self._apellido = apellido

  #Getter
  @property
  def edad(self):
    return self._edad

  #Setter
  @edad.setter
  def edad(self, edad):
    self._edad = edad

  #Metodo de nuestra clase
  def mostrar_detalle(self):
    print(f'Persona : {self._nombre} {self._apellido} {self._edad}')


#Creamos un objeto de esta clase
#Forma 1
persona1 = Persona('Adris','Garcia', 45)
persona1.nombre = 'Juan Carlos'
#print(persona1.nombre)
persona1.apellido = 'Lara'
persona1.edad = 30
persona1.mostrar_detalle()

#LLamada al metodo setter
#persona1.nombre = 'Juan Carlos'
print(persona1.nombre)



