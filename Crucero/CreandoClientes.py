import sqlite3

def Insertar():
	print ("**** Por favor ingresar datos de los clientes ****")
	nombre = input("Introduzca el nombre del cliente: ")
	apellido = input("Introduzca el apellido del cliente: ")
	telefono = input("Introduzca el numero telefonico: ")

	conexion = sqlite3.connect("Crucero1.sqlite")
 
	#Seleccionar el cursor para iniciar una consulta
	consulta = conexion.cursor()
 
	#Valor de los argumentos
	argumentos = (nombre, apellido, telefono)
 
	#consulta SQL con argumentos ?, ?

	sql = """INSERT INTO cliente(nombre, apellido, telefono) VALUES (?, ?, ?)"""
 
	#Realizar la consulta
	if (consulta.execute(sql, argumentos)):
 		print("Registro guardado con éxito\n")
 		print("*************************************\n")
 		print("Redirigir a menu principal\n")
 		print("*************************************\n")
	else: print("Ha ocurrido un error al guardar los datos\n")

	#Cerrar la consulta
	consulta.close()
 
	#Guardar los cambios en la base de datos
	conexion.commit()
 
