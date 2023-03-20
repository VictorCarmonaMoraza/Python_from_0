#Convertidor de temperatudas
#Convierte de Celcius a Farenheit
def gradosCelciusA_Farenheit(gradoCelcius):
    temperaturaFarenheit = (gradoCelcius *1.8) +32
    return temperaturaFarenheit


#Convierte de Farenheit a Celcius
def gradosFarenheitToCelcius(gradosFarenheit):
    temperaturaCelcius =gradosFarenheit-32/1.8
    return temperaturaCelcius

def comprobar(mensajeEntrada):
    if mensajeEntrada == 1:
         grados =float(input("Dame los grados que quieres pasar: "))
         gradosFarenheitToCelcius(grados)
         print("{:.2f} C".format(gradosFarenheitToCelcius(grados)))
    elif mensajeEntrada ==2:
        grados = float(input("Dame los grados que quieres pasar: "))
        gradosCelciusA_Farenheit(grados)
        print("{:.2f} F".format( gradosCelciusA_Farenheit(grados)))
    elif mensajeEntrada !=1 and mensajeEntrada !=2:
        print("no has seleccionado ninguna opcion valida")


print("¿Como quiere saber la temperatura?, escriba 1 o 2")
print("1-Celsius")
print("2-Farenheit")
mensajeEntrada = int(input("Seleccione: "))
comprobar(mensajeEntrada)
