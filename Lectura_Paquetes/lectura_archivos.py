fo = open("hola.txt","wb")
fo.write("El mejor lenguaje es python")
fo.close()

fo2 = open("hola.txt","r+")
srti = fo2.read()
print srti
fo2.close()
