#Creacion de la clase Persona
class Persona:
  def __init__(self, nom, apelli, age):
    self.nombre = nom
    self.apellido = apelli
    self.edad = age

  #Metodo de nuestra clase
  def mostrar_detalle(self):
    print(f'Persona : {self.nombre} {self.apellido} {self.edad}')


#Creamos un objeto de esta clase
persona1 = Persona('Victor','Carmona', 45)
persona1.mostrar_detalle()

persona2 = Persona('jorge','Perez',2515)
persona2.mostrar_detalle()

