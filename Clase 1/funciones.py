def Presentacion():
	print("Programa para hacer operaciones matematicas")
	print("*************")


def IntroducirDatos():
	global valor1
	global valor2
	valor1=int(input("Ingrese el primer valor ....."))
	valor2=int(input("Ingrese el segundo valor ...."))

def suma():
	suma=valor1+valor2
	print("La suma de los 2 valores es: ", suma)

def resta():
	resta=valor1-valor2
	print("La resta de los dos valores es: " ,resta)


def Finalizacion():
	print("***************")
	print("Gracias")



Presentacion()
IntroducirDatos()
suma()
resta()
Finalizacion()