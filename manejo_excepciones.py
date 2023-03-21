resultado = None

a = 10
b = 0

try:
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrio un error ZeroDivisionError {e}, {type(e)}')
except TypeError as te:
    print(f'Ocurrio un error TypeError {te}, {type(te)}')
except Exception as ex:
    print(f'Ocurrio un error Exception {ex}, {type(ex)}')


print(f'Resultado: {resultado}')
print('Continuamos...')