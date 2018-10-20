import random

def cargar():
	lista=[]
	for x in range(10):
		lista.append(random.randint(0, 1000))
	return lista


def imprimir(lista):
	print(lista)


def mezclar(lista):
	random.shuffle(lista)


#Main
lista=cargar()
print("Lista generada aleatoria mente")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar")
imprimir(lista)

