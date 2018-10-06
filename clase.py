class Estudiante:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def hola(self):
		return "Mi nombre es %s. \n" % self.nombre


e = Estudiante("Lucho", 32)
e1 = Estudiante("Lucia", 28)
e2 = Estudiante("Diana", 15)
print (e.hola(),e1.hola(),e2.hola())
