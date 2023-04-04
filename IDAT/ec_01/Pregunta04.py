horas = int(input("Las horas trabajadas son: "))
tarifa = float(input("La tarifa horaria es: "))

sueldoB = horas * tarifa
esSalud= (sueldoB *11.5) / 100
onp= (sueldoB *12.5) / 100
descuentoTo = esSalud + onp
sueldoN = sueldoB - descuentoTo

print("El sueldo bruto es: " + str(sueldoB))
print("El descuento por EsSalud es: "+str(esSalud))
print("El descuento por ONP es: "+str(onp))
print("El descuento total es: "+str(descuentoTo))
print("El sueldo neto es: s/"+str(sueldoN))