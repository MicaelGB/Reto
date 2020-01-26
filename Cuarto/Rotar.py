class spin():
	def rotar(self):
		self.t=[]
		self.matriz=[[1,2,3],
					 [1,2,3],
					 [1,2,3]]
		for i in range(len(self.matriz[0])):
			self.t.append([])
			for j in range(len(self.matriz)):
				self.t[i].append(self.matriz[j][i])
		print(self.matriz)
		print(self.t)

rotacion=spin()
rotacion.rotar()
