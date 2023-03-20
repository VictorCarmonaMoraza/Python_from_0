class Aritmetica:
    """
    Clase aritmetica opara realizar las operaciones de sumar, restar, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operA = operandoA
        self.operB = operandoB

    def sumar(self):
        return self.operA + self.operB

    def restar(self):
        return self.operA - self.operB

    def multiplicar(self):
        return self.operA * self.operB

    def dividir(self):
        return self.operA/self.operB


aritmetica1 = Aritmetica(1,3)
#Aritmetica.sumar(r_suma)
print(aritmetica1.sumar())
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(aritmetica1.dividir())

print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicacion: {aritmetica1.multiplicar()}')
#Mostramos que solo queremos dos digitos decimales
print(f'Division: {aritmetica1.dividir():.2f}')

