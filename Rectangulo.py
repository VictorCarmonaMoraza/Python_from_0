class Cubo:

    def __init__(self, b, h, p):
        self.ancho = b
        self.altura = h
        self.profundidad = p

    def mostra_detalles(self):
        return self.ancho * self.altura * self.profundidad




base  = int(input("Dame el ancho: "))
altura = int(input("Dame la altura: "))
profundidad = int(input("Dame la profundidad: "))
#Creamos el objeto
cubo1 = Cubo(base,altura, profundidad)
print(cubo1.mostra_detalles())

base2  = int(input("Dame la base: "))
altura2 = int(input("Dame la altura: "))
profundidad2 = int(input("Dame la profundidad: "))

cubo2 =Cubo(base2,altura2, profundidad2)
print(f'Area rectangulo2: {cubo2.mostra_detalles()}')