import psycopg2

#Creamos la variable conexion que recibira el objeto conexion
conexion = psycopg2.connect(
    user='postgres',
    password='Vcarmona32',
    host = '127.0.0.1',
    port='5432',
    database ='test_db'
)

#Comporbamos que estamos conectandono bien a la BBDD
#print(conexion)

#Crear un cursor
cursor =  conexion.cursor()
sentencia = 'Select * from persona'
#Ejecutamos la sentencia
cursor.execute(sentencia)
#Recuperamos los registros de la base de datos
registros = cursor.fetchall()
#Imprimimos los registros de nuestra tabla
print(registros)

#Crerramos cursor
cursor.close()
#Cerramos conexion
conexion.close()