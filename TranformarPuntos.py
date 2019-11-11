from datetime import datetime

def limpiarTextoHora(pTexto):
	#dado un texto de las horas se retorna este sin los caracteres no deseados [" ", "'", "[", ","]
	hora = pTexto.split(",")
	msg = hora[0]
	msg = msg.replace("[", "")
	msg = msg.replace("\'", "")
	msg = msg.replace(" ", "")
	return msg

def limpiadorPrecio(pTexto):
	#dado un texto con los precios se retorna sin los catarres deseados ["{", "\'", "COP", "OP", " ", ","]
	listaEliminar = ["{", "\'", "COP", "OP", " ", ","]
	for a in listaEliminar:
		pTexto = pTexto.replace(a, "")

	return pTexto
def convertirToPalabra(pLista):
	#dada una lista, retorna la lista como unsa string
	word = ""
	for a in pLista:
		word += a

	return word
def transformarHora(pHora):
	#dada una hora, la retorna en formato datetime
	
	hora1 = datetime.strptime(pHora + ":00", "%X").time()
	return hora1
def catalogador(pHora):
	#Se le entrega una hora y retorna si pertence a: a(manana), b(medio dia ), c(tarde)
	hora = transformarHora(pHora)
	#manana
	a = datetime.strptime("01:00:00", "%X").time()
	b = datetime.strptime("08:00:00", "%X").time()
	#medio dia
	c = datetime.strptime("08:01:00", "%X").time()
	d = datetime.strptime("16:00:00", "%X").time()
	#tarde
	e = datetime.strptime("16:01:00", "%X").time()
	f = datetime.strptime("23:59:00", "%X").time()
	if  hora >= a and hora <= b:
		return 1

	elif hora >= c and hora <= d:
		return 2
	elif hora >= e and hora <= f:
		return 3

def creadorEjex(pLista):
	
	listaEjex = []
	#En el eje x se cataloga la hora entre manana, medio dia y tard0
	contador = 0
	for lista in pLista:
		for a in lista:
			if contador %2 == 1:
				listaEjex.append(catalogador(limpiarTextoHora(a)))
			contador+= 1

	return listaEjex

def creadorEjey(pLista):
	listaEjey = []
	#en el eje y se encuentran los precios
	contador = 0
	for lista in pLista:
		for a in lista:
			if contador %2 == 0:
				listaEjey.append(int(limpiadorPrecio(a)))
			contador+= 1
	return listaEjey
		
	
def numCopToCop(pString):
	#dada una string se remplaza cualquier derivacion de 1,2,3..COP por COP
	msg = ""
	for a in range(20):
		msg = str(a) + "COP"
		pString = pString.replace(msg, "COP")

	return pString	
	
	

def main(pNombre):
	#Dado un nombre de ciudad, se retornan dos listas uno con los precios y otra con las horas 
	r = open(pNombre, "r")
	texto = r.readlines()
	diccionario = {}
	superLista = []
	for line in texto:
		if line[0:2]!= "{}":
			contador = 0
			listaIndices = []
			for letra in line:
				if letra == ":":
					listaIndices.append(contador)
				contador+= 1
			contador2 = 0
			palabra2List = list(line)
			for numero in listaIndices:
				if contador2 %3 == 0:
					palabra2List[numero] = "$"
				contador2 +=1

			palabraNueva = convertirToPalabra(palabra2List)
			palabraNueva = numCopToCop(palabraNueva)
			palabraNueva = palabraNueva.replace(", \'C", "$")
		
		
		
			ls = palabraNueva.split("$")
		
			superLista.append(ls)

	
	return creadorEjex(superLista), creadorEjey(superLista)

	
	

	


						
			
		
	
