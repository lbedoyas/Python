nota1=int(input("Ingrese primera nota"))
nota2=int(input("Ingrese la segunda nota"))
nota3=int(input("Ingrese la tercera nota"))
prom=(nota1+nota2+nota3)/3
print("Su promedio es .... " + str(prom))
if prom>=7:
	print("Promocionado")
else:
	if prom<=4:
		print("Regular")
	else:
		print("Reprobado")