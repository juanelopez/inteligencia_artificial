#Alumno: Juan Emilio Lopez
#Materia : Inteligencia artificial

import itertools
# atributos
AV = [('Soleado','Lluvioso','Nublado','?'),('Templada','Fria','?'),('Normal','Alta','?'),('Fuerte','Debil','?'),('Templada','Fria','?'),('Igual','Cambio','?')]

lista=[]
combinaciones = ("\n".join(" ".join(item) for item in itertools.product(*AV))) #generamos las hipotesis por combinacion
lista = combinaciones.split('\n')
h=[]
for salida in lista: #armamos la lista para comparar luego
	list_aux = salida.split(" ")
	h.append(list_aux)
#Ejemplos de entrenamiento
D1 = [('Soleado','Templada','Normal', 'Fuerte','Templada','Igual' ),('Verdadero')]
D2 = [('Soleado', 'Templada', 'Alta', 'Fuerte','Templada','Igual' ), ('Verdadero')]
D3 = [ ('Lluvioso','Fria', 'Alta', 'Fuerte','Templada','Cambio'), ('Falso')]
D4 = [('Soleado', 'Templada','Alta', 'Fuerte','Fria','Cambio'), ('Verdadero')]
D = [D1 , D2 , D3 , D4] 
#Prueba de hipotesis
positivo_consistente = 0
negativo_consistente = 0
congruente_positivo = 0
congruente_negativo = 0
lista_consistencias = []
for hipotesis_probada in h:#recorre las hipotesis(972)
	for entrenamiento in D:		#recorre los 4 ejemplos
		for i in range(0,len(hipotesis_probada)): #recorre la hipotesis y el ejemplo
			if(entrenamiento[1] == "Verdadero"):
				if(hipotesis_probada[i] == entrenamiento[0][i] or hipotesis_probada[i] == '?'): #prueba de consistencia positiva a cada elemento (todos los valores deben ser los del ejemplo de entrenamiento o ?)
					positivo_consistente += 1
			elif(entrenamiento[1] == "Falso"):
				if(hipotesis_probada[i] != entrenamiento[0][i]):
					negativo_consistente += 1
		
		if(positivo_consistente == 6): #prueba de congruencia positiva (ejemplo ejemplo da como positiva la hipotesis)
			congruente_positivo +=1
		elif(negativo_consistente > 0): #prueba de congruencia negativa (ejemplo falso no da como negativa la hipotesis)(con que un valor difiera es suficiente)
			congruente_negativo +=1
		positivo_consistente = 0
		negativo_consistente = 0
	if(congruente_positivo+congruente_negativo == len(D)): #probamos si todos los ejemplos fueron bien tomados 
		lista_consistencias.append(hipotesis_probada) #se agrega la hipotesis a la lista de consistencias
	congruente_positivo = 0
	congruente_negativo = 0
print("Espacio de versiones")
for mostrar in lista_consistencias:
	print(mostrar)
