numero = int(input("Ingrese un número de 5 cifras: "))

dm = numero// 10000  
um= numero %10000 // 1000
c = numero// 100 % 10
d = numero %100//10
u = numero %100%10
nuevonum = (dm*1000)+(um*100)+(d*10)+u  

print("El nuevo número es: " + str(nuevonum))