#Impresion de una lista
print("Ejemplos de como hacer listas en Python")
lista =["Apple", "Google", "Facebook"]
print (lista) 

#Agregar elementos a la lista
print("Agregamos elementos a la listas")
lista.append("Tesla")
print(lista)

print("Ejemplo de una elemento en una posicion especifica")
lista.insert(0,"Motorola")
print(lista)

print("Elemento extend adiciona varios campos a una lista")
lista1 = ["Carrefour","Jumbo","Metro"]
lista.extend(lista1)
print(lista)

print("Busca una posicion en la lista y devuelve la ubicacion")
ej1= lista.index("Apple")
print(ej1)


