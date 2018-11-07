import sqlite3

def DeleteCliente():
	print("****************************")
	print("Bienvenido al modulo de Eliminacion de clientes")
	print("Nota: Tenga encuenta el numero de cliente para hacer cambios")
	print("****************************")
	id_Cliente = input("Ingrese el numero del cliente \n => ")
	if not id_Cliente:
		print("Id del cliente no existe")
		exit()

	bd = sqlite3.connect("Crucero1.sqlite")

	cursor = bd.cursor()

	sentencia = "DELETE FROM Cliente WHERE rowid = ?;"
 
	#Eliminar el libro
	cursor.execute(sentencia, [id_Cliente])
	bd.commit()
	print("Eliminado con éxito")
