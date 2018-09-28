import vocales
import unittest


class Test_Vocales(unittest.TestCase):
	def test_voc(self):
		resultado = vocales.es_vocal("a")
		self.assertEqual(resultado,True)

if __name__=='__main__':
	unittest.main()