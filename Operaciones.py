print "Datos de la primera persona"

nombre1=input("Ingrese nombre del producto: ")
precio1=int(input("Ingrese el precio: "))

nombre2=input("Ingrese nombre del producto: ")
precio2=int(input("Ingrese el precio: "))

#Las constantes se escriben en mayusculas
BONIFICACION = 20

#sumas
precio_compra_total = precio1 + precio2
#Comparacion
comparar=precio1>=precio2

logico=(precio1<precio2 and precio1==precio2)

#Ejemplo de concanetacion
cabecera = "Resultados del producto {0}. y del producto {1}. :"
print(cabecera.format(nombre1, nombre2))

print "El precio del primer valor es mayor o igual a el precio del segundo:"
print(comparar)

#con el signo + tambien se pueden realizar concanetaciones
print("la suma de los productos es: " + str(precio_compra_total))
print("precio1 < precio2 and precio1 == precio2")
print(logico)

#Asignacion
precio_compra_total += BONIFICACION
print ("al precio total le incrementamos su valor que tiene la constante" + str(precio_compra_total))


