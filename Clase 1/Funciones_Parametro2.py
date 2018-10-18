def Retorno_Superficie(lado):
	sup=lado*lado
	return sup
va=int(input("Introduce el valor del cuadrado:  "))
superficie=Retorno_Superficie(va)
print("Algoritmo del cuadrado es:  ",superficie)