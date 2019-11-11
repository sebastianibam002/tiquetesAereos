""" Se crea un diccionario con las posibles ciudades, donde el nombre de la ciudad es la llave y la abreviación es el valor """
posiblesCiudades = {"Arequipa": "AQP", "Barranquilla": "BAQ", "Bogota": "BOG", "Bucaramanga": "BGA",  "Cajamarca": "CJA", "Cartagena": "CTG", "Chiclayo": "CIX", "Cusco": "CUZ", "Cucuta" : "CUC,", "Iquitos": "IQT", "Jaen": "JAE", "Juliaca": "JUL", "Lima": "LIM", "Medellin": "MDE", "Miami": "MIA", "Monteria": "MTR", "Pereira": "PEI", "Piura": "PIU", "Rioacha": "RCH", "San Andres Islas": "ADZ", "Santa Marta": "SMR", "Tacna": "TCQ", "Talara": "TYl", "Tarapoto": "TPP", "Valledupar": "VUP"}


def generarPrefijo(pNombre):  # Se encarga de generar un prefijo especifico para cada una de las ciudades
	for a in posiblesCiudades.keys():
		if a == pNombre:
			return posiblesCiudades[a]

def buscarEnCiudad(pCiudad):  # Se introduce como parametreo la ciudas y se evalua con este metodo si existe
	
    encontrado = False

    for a in posiblesCiudades.keys():

        if a == pCiudad:
            encontrado = True

    return encontrado

def checkDate(pFecha):  # Revisa si la fecha se ingresó correctamente
	
	
	anOk = False
	mesOk = False
	diaOk = False
	# La fecha debe tener el siguiente formato AAAA-MM-DD
	listaPartes = pFecha.split("-")
	ano = int(listaPartes[0])
	mes = int(listaPartes[1])
	dia = int(listaPartes[2])

	if ano >= 2019:
		anOk = True
	if mes > 0 and mes < 13:
		mesOk = True
	
	if dia > 0 and dia < 32:
		diaOk = True

	if anOk and mesOk and diaOk:
		return True
	else:
		return anOk, mesOk, diaOk
	



def modificacionLink(pCiudadSalida, pCiudadDestino, pFechaSalida, pNumeroDePersonas):  # modifica el link se Viva Air para realizar la busqueda de los datos ingresados

	if buscarEnCiudad(pCiudadDestino):

		if checkDate(pFechaSalida):
			
		
			url = "https://www.vivaair.com/co/es/vuelo?DepartureCity=" +posiblesCiudades[pCiudadSalida] +"&ArrivalCity="+posiblesCiudades[pCiudadDestino]+"&DepartureDate=" + pFechaSalida+ "&Adults=" + str(pNumeroDePersonas) +"&Currency=COP"
		else:	
			#pNumeroDePersonas <10, checkDate(pFechaSalida)
			url = None
	print(url)
	return url



