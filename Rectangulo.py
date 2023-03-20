class Rectangulo:

    def __init__(self, b, h):
        self.base = b
        self.altura = h

    def mostra_detalles(self):
        return self.base * self.altura




base  = int(input("Dame la base: "))
altura = int(input("Dame la altura: "))
#Creamos el objeto
rectangulo1 = Rectangulo(base,altura)
print(rectangulo1.mostra_detalles())

base2  = int(input("Dame la base: "))
altura2 = int(input("Dame la altura: "))

rectangulo2 =Rectangulo(base2,altura2)
print(f'Area rectangulo2: {rectangulo2.mostra_detalles()}')