donacion = float(input("El importe recibido es: "))

talleres = donacion * 0.20
biblioteca = donacion * 0.25
investigacion = biblioteca * 0.45
becas = (talleres + investigacion) *0.75
deportes = donacion - talleres - biblioteca - investigacion - becas

print("Programa de Talleres recibe: " +str(talleres))
print("Programa de Biblioteca recibe: " +str(biblioteca))
print("Programa de Investigación recibe: " +str(investigacion))
print("Programa de Becas recibe: " +str(becas))
print("Programa de Deportes recibe: " +str(deportes))
