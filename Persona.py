#Creacion de la clase Persona
class Persona:
  def __init__(self, nom, apelli, age):
    self.nombre = nom
    self.apellido = apelli
    self.edad = age




#Creamos un objeto de esta clase
persona1 = Persona('Victor','Carmona', 45)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
#print(type(Persona))

persona2 = Persona('jorge','Perez',2515)
print(f'Objeto Persona 2:{persona2.nombre} {persona2.apellido} {persona2.edad}')
