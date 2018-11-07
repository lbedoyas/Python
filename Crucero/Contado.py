import sqlite3

def Contado():

	

	
	print("****************************")
	print("Bienvenido al modulo de pago")
	print("Nota: Tenga encuenta el numero de cliente al cual va agregar los pagos")
	print("****************************")
	valorMes = 0
	mes = input("Ingrese el mes que se va realizar la compra......  ")
	if mes == "enero" or mes == "Enero" or mes == "ENERO":
		valorMes = 750
	elif mes == "febrero" or mes == "Febrero" or mes == "FEBRERO":
		valorMes = 788
	elif mes == "marzo" or mes == "Marzo" or mes == "MARZO":
		valorMes = 825
	elif mes == "abril" or mes == "Abril" or mes == "ABRIL":
		valorMes = 863
	elif mes == "mayo" or mes == "Mayo" or mes == "MAYO":
		valorMes = 900
	elif mes == "junio" or mes == "Junio" or mes == "JUNIO":
		valorMes = 938
	elif mes == "julio" or mes == "Julio" or mes == "JULIO":
		valorMes = 975
	elif mes == "agosto" or mes == "Agosto" or mes == "AGOSTO":
		valorMes = 1013
	elif mes == "septiembre" or mes == "Septiembre" or mes == "SEPTIMBRE":
		valorMes = 1050
	elif mes == "octubre" or mes == "Octubre" or mes == "OCTUBRE":
		valorMes = 1088
	elif mes == "noviembre" or mes == "Noviembre" or mes == "NOVIEMBRE":
		valorMes = 1125
	elif mes == "diciembre" or mes == "Diciembre" or mes == "DICIEMBRE":
		valorMes = 1163
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print("Su valor del mes es.....\n", valorMes)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

	#Decision de pago
	print("****************************")
	print("Por favor, Tenga encuenta el numero de cliente ")
	print("")
	print("")
	print("****************************")
	vcliente = 0	
	vcliente = input("Digite el codigo del cliente ..")
	print("Gracias por su compra")


	
	conexion = sqlite3.connect("Crucero1.sqlite")

 
	#Seleccionar el cursor para iniciar una consulta
	consulta = conexion.cursor()
 
	#Valor de los argumentos
	argumentos = (mes, valorMes, vcliente)
 
	#consulta SQL con argumentos ?, ?

	sql = """INSERT INTO Contado VALUES (null, ?, ?, ?)"""
 
	#Realizar la consulta
	if (consulta.execute(sql,argumentos)):
 		print("Registro guardado con éxito\n")
 		print("*************************************\n")
 		print("Redirigir a menu principal\n")
 		print("*************************************\n")
	else: print("Ha ocurrido un error al guardar los datos\n")

	#Cerrar la consulta
	consulta.close()
 
	#Guardar los cambios en la base de datos
	conexion.commit()
	conexion.close()


