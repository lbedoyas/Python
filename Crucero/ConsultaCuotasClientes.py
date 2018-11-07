import sqlite3

def ConsCuotas():
	conexion = sqlite3.connect("Crucero1.sqlite")

	consulta = conexion.cursor()


	#Extrayendo todas las filas
	sql = "select * from Cliente inner join Financiado on Financiado.idFinanciado = Cliente.idCliente"
	consulta.execute(sql)

	for i in consulta.fetchall():
		print("Codigo de cliente",i[0])
		print("nombre",i[1])
		print("apellido",i[2])
		print("Telefono",i[3])
		print("IdFin",i[6])
		print("Enero",i[7])
		print("Febrero",i[8])
		print("Marzo",i[9])
		print("Abril",i[10])
		print("Mayo",i[11])
		print("Junio",i[12])
		print("Julio",i[13])
		print("Agosto",i[14])
		print("Septiembre",i[15])
		print("Octubre",i[16])
		print("Noviembre",i[17])
		print("Diciembre",i[18],"\n")

			

	consulta.close()