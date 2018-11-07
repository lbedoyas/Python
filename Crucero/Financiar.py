import sqlite3

def Financiado():
	print("****************************")
	print("Bienvenido al modulo de pago Financiado")
	print("Nota: Tenga encuenta el numero de cliente al cual va agregar los pagos")
	print("****************************")
	print("Digite el numero de cliente al que se le va cargar la financiacion")
	vcliente = 0	
	vcliente = input("Digite el codigo del cliente ..")
	valorMes = 0
	mes = input("Ingrese el mes que se va realizar la compra......  ")
	if mes == "enero" or mes == "Enero" or mes == "ENERO":
		valorMes = 750
		ValorCuotas = valorMes/12	

		ValorEnero = ValorCuotas
		ValorFebrero = ValorCuotas
		ValorMarzo = ValorCuotas
		ValorAbril = ValorCuotas
		ValorMayo = ValorCuotas
		ValorJunio = ValorCuotas
		ValorJulio = ValorCuotas
		ValorAgosto = ValorCuotas
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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




	elif mes == "febrero" or mes == "Febrero" or mes == "FEBRERO":
		valorMes = 788

		ValorCuotas = valorMes/11	

		ValorEnero = 0
		ValorFebrero = ValorCuotas
		ValorMarzo = ValorCuotas
		ValorAbril = ValorCuotas
		ValorMayo = ValorCuotas
		ValorJunio = ValorCuotas
		ValorJulio = ValorCuotas
		ValorAgosto = ValorCuotas
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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


	elif mes == "marzo" or mes == "Marzo" or mes == "MARZO":
		valorMes = 825

		ValorCuotas = valorMes/10	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = ValorCuotas
		ValorAbril = ValorCuotas
		ValorMayo = ValorCuotas
		ValorJunio = ValorCuotas
		ValorJulio = ValorCuotas
		ValorAgosto = ValorCuotas
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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


	elif mes == "abril" or mes == "Abril" or mes == "ABRIL":
		valorMes = 863

		ValorCuotas = valorMes/9	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = ValorCuotas
		ValorMayo = ValorCuotas
		ValorJunio = ValorCuotas
		ValorJulio = ValorCuotas
		ValorAgosto = ValorCuotas
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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


	elif mes == "mayo" or mes == "Mayo" or mes == "MAYO":
		valorMes = 900

		ValorCuotas = valorMes/8	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = 0
		ValorMayo = ValorCuotas
		ValorJunio = ValorCuotas
		ValorJulio = ValorCuotas
		ValorAgosto = ValorCuotas
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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


	elif mes == "junio" or mes == "Junio" or mes == "JUNIO":
		valorMes = 938

		ValorCuotas = valorMes/7	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = 0
		ValorMayo = 0
		ValorJunio = ValorCuotas
		ValorJulio = ValorCuotas
		ValorAgosto = ValorCuotas
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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


	elif mes == "julio" or mes == "Julio" or mes == "JULIO":
		valorMes = 975


		ValorCuotas = valorMes/6	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = 0
		ValorMayo = 0
		ValorJunio = 0
		ValorJulio = ValorCuotas
		ValorAgosto = ValorCuotas
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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

	elif mes == "agosto" or mes == "Agosto" or mes == "AGOSTO":
		valorMes = 1013

		ValorCuotas = valorMes/5	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = 0
		ValorMayo = 0
		ValorJunio = 0
		ValorJulio = 0
		ValorAgosto = ValorCuotas
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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



	elif mes == "septiembre" or mes == "Septiembre" or mes == "SEPTIMBRE":
		valorMes = 1050

		ValorCuotas = valorMes/5	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = 0
		ValorMayo = 0
		ValorJunio = 0
		ValorJulio = 0
		ValorAgosto = 0
		ValorSeptiembre = ValorCuotas
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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


	elif mes == "octubre" or mes == "Octubre" or mes == "OCTUBRE":
		valorMes = 1088

		ValorCuotas = valorMes/5	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = 0
		ValorMayo = 0
		ValorJunio = 0
		ValorJulio = 0
		ValorAgosto = 0
		ValorSeptiembre = 0
		ValorOctubre = ValorCuotas
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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


	elif mes == "noviembre" or mes == "Noviembre" or mes == "NOVIEMBRE":
		valorMes = 1125

		ValorCuotas = valorMes/5	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = 0
		ValorMayo = 0
		ValorJunio = 0
		ValorJulio = 0
		ValorAgosto = 0
		ValorSeptiembre = 0
		ValorOctubre = 0
		ValorNoviembre = ValorCuotas
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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

	elif mes == "diciembre" or mes == "Diciembre" or mes == "DICIEMBRE":
		valorMes = 1163

		ValorCuotas = valorMes/5	

		ValorEnero = 0
		ValorFebrero = 0
		ValorMarzo = 0
		ValorAbril = 0
		ValorMayo = 0
		ValorJunio = 0
		ValorJulio = 0
		ValorAgosto = 0
		ValorSeptiembre = 0
		ValorOctubre = 0
		ValorNoviembre = 0
		ValorDiciembre = ValorCuotas

		conexion = sqlite3.connect("Crucero1.sqlite") 
		consulta = conexion.cursor()

		argumentos = (ValorEnero, ValorFebrero, ValorMarzo, ValorAbril, ValorMayo, ValorJunio, ValorJulio, ValorAgosto, ValorSeptiembre, ValorOctubre, ValorNoviembre, ValorDiciembre, vcliente) 
		sql = """INSERT INTO Financiado VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""" 
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



