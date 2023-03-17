
pagoSinImpuestos = int(input("Ingrese pago sin impuestos:"))
montoDelInpuesto = int(input("Monto del inpuestos:"))

def calcular_total_pago(PagoSinInpuestosParam, MontoDelImpuestoParam):
    pagoTotal = pagoSinImpuestos + pagoSinImpuestos*(montoDelInpuesto/100)
    return pagoTotal


total = calcular_total_pago(pagoSinImpuestos,montoDelInpuesto)
print('Pago con impuesto: ',total)