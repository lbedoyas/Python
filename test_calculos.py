import unittest
import calculos

#crear casos de prueba para funciones para esto se debe crear una clase

class TestCalculos(unittest.TestCase):
	def test_suma(self):
		result = calculos.suma(5,8)
		self.assertEqual(result,13)

if __name__=='__main__':
	unittest.main()