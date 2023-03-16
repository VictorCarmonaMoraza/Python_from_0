#la flecha indica el tipo que va a devolver
def sumar(a:int=0, b:int=3) ->int:
    return a+b


resultado = sumar()
print(resultado)
print(f'Resultado sumar: {sumar(2,8)}')