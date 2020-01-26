from random import randint
def get_rand():
        num=randint(1,1000)
        return num
lista = []
for i in range(10):
	lista.append(get_rand())
print(f'orden inicial: {lista}')

aux=[]
#lista=[10,5,10,4,10,5,2,10,1,1]

for i in range(len(lista)-1,-1,-1):
	if lista[i] not in aux:
		aux.append(lista[i])
	else:
		aux.remove(lista[i])
		print(f'repetido: {lista[i]}')
aux=sorted(aux)
print(f'Orden final: {aux}')
