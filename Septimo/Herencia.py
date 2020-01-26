class Animales: 
	vidas=1
	padres=2
	muerte=1
	def nacer(self):
		return True
	def alimentarse(self):
		return True
	def reproducirse(self):
		return True

class Mamiferos(Animales):
	hermanos=2
	crias=3
	parejas=1 
	def amamantarse(self):
		return True
	def nacer_de_huevo(self):
		return False
	def carnivoro(self):
		print('Puede haber de ambos')

class Felinos(Mamiferos):
	patas=4
	garras=5
	cola=1
	def colmillos(self):
		return True
	def respirar_bajo_agua(self):
		return False
	def andar_4_patas(self):
		return True

class Gato(Felinos):
	orejas=2
	nariz=1
	hojos=2
	def maullar(self):
		return True
	def lamerse(self):
		return True
	def comer_ratones(self):
		return True
