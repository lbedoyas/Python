#Establecer la dimension de la matriz

x = 3
y = 3
matriz=[]
for i in range(x):
	matriz.append([0]*y)
print (matriz)


# rellenar la matriz
contador = 1
for i in range(x):
	for j in range(y):
		matriz[i][j]=contador
		contador+=1




# Imprimir la matriz
print(matriz)

for i in matriz:
	for j in i:
		print (j),
	print (i)
	