#Esta pendiente por analizar 

def vocales(letra):
	print("Digite una letra")
	letra = input("Por favor escribe la letra en minuscula .. ")
	print(letra)
	if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
		return True
	else:
		return False
	


vocales('letra')
