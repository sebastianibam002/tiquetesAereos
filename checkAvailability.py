
posiblesCiudades = {"Arequipa": "AQP", "Barranquilla": "BAQ", "Bogota": "BOG", "Bucaramanga": "BGA",  "Cajamarca": "CJA", "Cartagena": "CTG", "Chiclayo": "CIX", "Cusco": "CUZ", "Cucuta" : "CUC,", "Iquitos": "IQT", "Jaen": "JAE", "Juliaca": "JUL", "Lima": "LIM", "Medellin": "MDE", "Miami": "MIA", "Monteria": "MTR", "Pereira": "PEI", "Piura": "PIU", "Rioacha": "RCH", "San Andres Islas": "ADZ", "Santa Marta": "SMR", "Tacna": "TCQ", "Talara": "TYl", "Tarapoto": "TPP", "Valledupar": "VUP"}



def buscarEnCiudad(pCiudad):

    #se introduce como parametreo la ciudad y se evalua con este metodo si existe
    encontrado = False

    for a in posiblesCiudades.keys():

        if a == pCiudad:
            encontrado = True



    return encontrado

def checkDate(pFecha):
	
	
	anOk = False
	mesOk = False
	diaOk = False
	#la fecha debe tener el siguiente formato 2019-10-25
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
	



def modificacionLink(pCiudadSalida, pCiudadDestino, pFechaSalida, pNumeroDePersonas):

	if buscarEnCiudad(pCiudadSalida) and buscarEnCiudad(pCiudadDestino):

		if checkDate(pFechaSalida) and pNumeroDePersonas < 10:
			
		
			url = "https://www.vivaair.com/co/es/vuelo?DepartureCity=" +posiblesCiudades[pCiudadSalida] +"&ArrivalCity="+posiblesCiudades[pCiudadDestino]+"&DepartureDate=" + pFechaSalida+ "&Adults=" + str(pNumeroDePersonas) +"&Currency=COP"
		else:	
			#pNumeroDePersonas <10, checkDate(pFechaSalida)
			url = None
	return url




	
