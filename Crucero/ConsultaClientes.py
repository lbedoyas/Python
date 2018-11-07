import sqlite3

def ConsultarC():
	conexion = sqlite3.connect("Crucero1.sqlite")

	consulta = conexion.cursor()


	#Extrayendo todas las filas
	sql = "SELECT * FROM Cliente"
	consulta.execute(sql)

	for i in consulta.fetchall():
		print("Codigo de cliente",i[0])
		print("Nombre", i[1])
		print("Apellido", i[2])
		print("Telefono", i[3],"\n")	

	consulta.close()
