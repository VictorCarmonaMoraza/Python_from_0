
# Argumentos variables en argumentos
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')


#listarTerminos(IDE='Interprete', PK='Primary key')
listarTerminos(IDE='Interprete', PK='Primary key')

