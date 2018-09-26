import math
import unittest
import potencia

class Test_Potencia(unittest.TestCase):
	def test_potencia(self):
		resultado = potencia.potencia(6)
		self.assertEqual(resultado,36)

if __name__=='__main__':
	unittest.main()