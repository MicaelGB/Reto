lista = []
class Invertir():
	def __init__(self):
		self.my_str=input("Ingrese un string: ")
	def inversion(self):
		self.my_str=list(self.my_str)
		for i in range(len(self.my_str)):
			lista.append(self.my_str[len(self.my_str)-1-i])
		print("".join(lista))
string=Invertir()
string.inversion()

#my_str=input("Ingrese un string: ")
#my_str=list(my_str)


#for i in range(len(my_str)):
	#print(my_str[len(my_str)-1-i])
