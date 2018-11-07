import sqlite3

def ConsCuotas():
	conexion = sqlite3.connect("Crucero1.sqlite")

	consulta = conexion.cursor()


	#Extrayendo todas las filas
	sql = "select * from Cliente inner join Contado on Contado.idCliente = Cliente.idCliente"
	consulta.execute(sql)

	for i in consulta.fetchall():
		print("Codigo de cliente",i[0])
		print("Nombre",i[1])
		print("Apellido",i[2])
		print("Mes",i[7])
		print("Valor Pagado",i[8],"\n")

			

	consulta.close()