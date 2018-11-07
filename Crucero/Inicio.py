import CreandoClientes
import Contado
import ConsultaClientes
import Financiar
import ModificarClientes
import EliminarCliente
import ConsultaCuotasClientes
import ClientesNotCuotas


class Crucero:
	def __init__(self):
		self.dato = 1
	def menu(self):

		while self.dato:
			print('Bienvenido al Trabajo Final de Tendencias !!!! \n')
			print('Eliga una de las opciones \n')
			seleccion = input('\n 1. Ingresar Clientes\n 2. Consutar datos de Clientes \n 3. Ingreso de pagos de contado \n 4. Ingreso de pagos Financiados \n 5. Modificar Clientes \n 6. Eliminar Clientes \n 7. Consultar Cuotas de cada cliente \n 8. Clientes que no deben cuotas \n \n =>')

			if seleccion == '1':
				CreandoClientes.Insertar()
			elif seleccion =='2':
				ConsultaClientes.ConsultarC()
			elif seleccion =='3':
				Contado.Contado()
			elif seleccion == '4':
				Financiar.Financiado()
			elif seleccion == '5':
				ModificarClientes.ModCliente()
			elif seleccion == '6':
				EliminarCliente.DeleteCliente()
			elif seleccion == '7':
				ConsultaCuotasClientes.ConsCuotas()
			elif seleccion == '8':
				ClientesNotCuotas.ConsCuotas()




			else:
				print('\n Eleccion Invalida')

session1 = Crucero()
session1.menu()