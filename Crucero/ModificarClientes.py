import sqlite3

def ModCliente():
	print("****************************")
	print("Bienvenido al modulo de modificacion de clientes")
	print("Nota: Tenga encuenta el numero de cliente para hacer cambios")
	print("****************************")
	id_Cliente = input("Ingrese el numero del cliente")
	if not id_Cliente:
		print("Id del cliente no existe")
		exit()


	bd = sqlite3.connect("Crucero1.sqlite")

	cursor = bd.cursor()

	nombre = input("\nNuevo nombre: ")
	apellido = input("\nNuevo apellido: ")
	telefono = input("\nNuevo telefono: ")
 
	#Sentencia para actualizar
	sentencia = "UPDATE Cliente SET nombre = ?, apellido = ?, telefono = ? WHERE rowid = ?;"

	cursor.execute(sentencia, [nombre, apellido, telefono, id_Cliente])
	bd.commit()
	print("Datos Actualizados")
 






