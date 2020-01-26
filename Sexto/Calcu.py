
class calculadora():
	def __init__(self):
		self.a = float(input("introduzca primer número: "))
		self.b = float(input("introduzca segundo número: "))
		self.op = input("introduzca operación (s para suma, m para multiplicación o d para división): ")
		
class process():
	aux = calculadora()
	op = aux.op
	a = aux.a 
	b = aux.b
	def calc(self):
		if (self.op=='s'):
			self.suma()
		if (self.op=='m'):
			self.multiplicacion()
		if (self.op=='d'):
			self.division()
	def suma(self):
		self.s = self.a + self.b
		print(f'la suma es: {self.s}')
	def multiplicacion(self):
		self.m=self.a * self.b
		print(f'la multiplicación es: {self.m}')
	def division(self):
		self.d=self.a / self.b
		print(f'la división es: {self.d}')

x=process()
x.calc()
