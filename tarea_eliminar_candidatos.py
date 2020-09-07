import itertools
# General(Hipotesis)

G = ['?', '?', '?' ]

#Especifico(hipotesis)

S = [None, None, None]

# atributos
AV = [('Rojo','Azul','Verde','?'),('Cuadrado','Redondo','?'),('Grande','Pequeno','?')]

# Ejemplo:
#print(type(AV))
lista=[]
combinaciones = ("\n".join(" ".join(item) for item in itertools.product(*AV)))


lista = combinaciones.split('\n')

h=[]
for salida in lista:
	list_aux = salida.split(" ")
	h.append(list_aux)
#hace las 972 combinaciones con el vacio
D1 = [('Rojo','Cuadrado','Grande' ),('Verdadero')]
D2 = [('Azul', 'Cuadrado', 'Grande' ), ('Verdadero')]
D3 = [ ('Rojo','Redondo', 'Pequeno' ), ('Falso')]
D4 = [('Verde', 'Cuadrado','Pequeno' ), ('Falso')]
D = [D1 , D2 , D3 , D4]

consistente_general = 0
especifico_positivo = 0
clasifica_negativo = 0
generales = []
for entrenamiento in D:
	if(entrenamiento[1] == 'Verdadero'):
		for i in range(0,(len(G))):			
			if(entrenamiento[0][i] == G[i] or G[i] == '?'):
				consistente_general +=1
			if(S[i] == None):#siempre inconsistente
				S[i] = entrenamiento[0][i]
			elif(S[i] == entrenamiento[0][i] or S[i] == '?'):
				especifico_positivo +=1
			elif(S[i] != entrenamiento[0][i]):
				S[i] = '?'
	elif(entrenamiento[1] == 'Falso'): #problemas NO FUNCIONA
		for i in range(0,len(S)):
			if(S[i] != entrenamiento[0][i]):
				clasifica_negativo +=1
			if(G[i] == entrenamiento[0][i]):
				print(G[i])

print("Especifica",S)
#print("General",generales)
"""parametros_comparados_G = 0
terminado_G = []
finalizada_S = []
finalizada_S = h
print("\n\n\nVERDADEROS \n\n\n")
for final in h:
	#print(len(final))
	for i in range(0,len(G)):
		if(G[i] != '?'):
			if(final[i] == G[i]):
				parametros_comparados_G = parametros_comparados_G+1	
	if(parametros_comparados_G == parametros_definidos_G):
		final.append("Verdadero")
		terminado_G.append(final)
		#print(final)
	parametros_comparados_G = 0

#print(terminado_G)

print("\n\n\nFALSOS \n\n\n")
terminado_S = []
parametros_comparados_S = 0
for final in finalizada_S:
	for i in range(0,len(S)):
		if(final[i] == S[i]):
			parametros_comparados_S = parametros_comparados_S+1
	if(parametros_comparados_S > 1 and len(final)<7):
		final.append("Falso")
		terminado_S.append(final)
		#print(final)
	parametros_comparados_S = 0
#print(terminado_S)
"""
