""" Se define el diccionario que contiene las posibles ciudades, donde el nomdre de laciudad es la llave y los valores son las respectivas abreviaturas  """

posiblesCiudades = {"Arequipa": "AQP", "Barranquilla": "BAQ", "Bogota": "BOG", "Bucaramanga": "BGA",  "Cajamarca": "CJA", "Cartagena": "CTG", "Chiclayo": "CIX", "Cusco": "CUZ", "Cucuta" : "CUC,", "Iquitos": "IQT", "Jaen": "JAE", "Juliaca": "JUL", "Lima": "LIM", "Medellin": "MDE", "Miami": "MIA", "Monteria": "MTR", "Pereira": "PEI", "Piura": "PIU", "Rioacha": "RCH", "San Andres Islas": "ADZ", "Santa Marta": "SMR", "Tacna": "TCQ", "Talara": "TYl", "Tarapoto": "TPP", "Valledupar": "VUP"}


def generarPrefijo(pNombre):  #Se encarga de generar un prefijo especifico para cada una de las ciudades
	for a in posiblesCiudades.keys():
		if a == pNombre:
			return posiblesCiudades[a]

def buscarEnCiudad(pCiudad):   #Se introduce como parametreo la ciudad y se evalua con este metodo si existe
    encontrado = False

    for a in posiblesCiudades.keys():

        if a == pCiudad:
            encontrado = True

    return encontrado

def checkDate(pFecha):
	
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
	


""" Se define la función que permite modificar el url del sitio web de Viva Air en el cual se ingresan los datos del vuelo, como el destino, la ciudad de salida, la fecha y el numero de pasajeros y retorna el url modificado y listo para realizar la busqueda """

def modificacionLink(pCiudadSalida, pCiudadDestino, pFechaSalida, pNumeroDePersonas):

	if buscarEnCiudad(pCiudadDestino):

		if checkDate(pFechaSalida):
			
			url = "https://www.vivaair.com/co/es/vuelo?DepartureCity=" +posiblesCiudades[pCiudadSalida] +"&ArrivalCity="+posiblesCiudades[pCiudadDestino]+"&DepartureDate=" + pFechaSalida+ "&Adults=" + str(pNumeroDePersonas) +"&Currency=COP"
		else:	
			#pNumeroDePersonas <10, checkDate(pFechaSalida)
			url = None
	print(url)
	return url

	
