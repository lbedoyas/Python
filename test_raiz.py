import math
import unittest
import raiz

class Test_Raiz(unittest.TestCase):
	def test_raizc(self):
		resultado = raiz.RaizC(4)
		self.assertEqual(resultado,2.0)


if __name__=='__main__':
	unittest.main()