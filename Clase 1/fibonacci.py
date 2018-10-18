def fib(n):
	resultado = []
	a, b = 0, 1
	while a <n:
		print(a)
		a, b = b, a+b
	return resultado

fib(2000)