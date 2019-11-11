import time
from requests_html import HTMLSession




def webScrapping (pUrl):
	#requiere como parametro un url y retorna el codigo html de este url

	try:
		session = HTMLSession()
		resp = session.get(pUrl)
		resp.html.render()
		return resp.html.html
	except:
		print("Revisar Conexion")
	
	
	


def AlmacenarTexto(pUrl, pNombreCiudad):
	#crea un archivo de texto con el nombre de la ciudad que se paso por parametro y se guarda en esta el codigo html de la pagina de codigo url
	nombreTexto = pNombreCiudad + ".txt"

	with open(nombreTexto, "w") as texto:
		texto.write(webScrapping(pUrl))

def limpiarTexto(pString):
    #dado una string, se retorna esta sin los caracteres no deseados 

    pString= pString.replace("\n", "")
    pString = pString.replace(">", "")
    pString = pString.replace("          ", "")
    pString = pString.replace(" ", "")
    return pString


def BuscadorTexto(pNombreCiudad, pStringBusqueda):

    #dado un nombre de una ciudad, se procede a abrir este archivo y a buscar en esta una string determinada, retorna una lista con los datos de la string buscada
    archivo  = open (str(pNombreCiudad) + ".txt", "r")
    textoArchivo = archivo.read()
    lsIndicesI = []
    lsIndicesF = []
    lsPrecios = []
    contador = 0
    
    encontrado = True


    if pStringBusqueda == "from-price":
        
        consLenPString = pStringBusqueda.__len__()

        lsIndicesI.append(textoArchivo.find(pStringBusqueda) + consLenPString)
        lsIndicesF.append(textoArchivo.find("<",  lsIndicesI[0]))
    
        
    
        while encontrado:
            if textoArchivo.find(pStringBusqueda, lsIndicesI[contador] + consLenPString) != -1:

                lsIndicesI.append(textoArchivo.find(pStringBusqueda, lsIndicesI[contador]) + consLenPString)
                lsIndicesF.append(textoArchivo.find("<", lsIndicesI[contador + 1]))
                contador += 1

                #lsPrecios.append(textoArchivo[lsIndicesI[contador] + 2: lsIndicesF[contador]])

            else:

                #se ejecuta cuando no hay mas precios
                break
        
        contador2 = 0
        for a in lsIndicesI:
            lsPrecios.append(textoArchivo[a + 2: lsIndicesF[contador2]])
            contador2 += 1

   
        
        return lsPrecios

    else:

        consLenPString = pStringBusqueda.__len__()

        lsIndicesI.append(textoArchivo.find(pStringBusqueda) + consLenPString)
        lsIndicesF.append(textoArchivo.find("<",  lsIndicesI[0]))
    
    

    
        while encontrado:
            if textoArchivo.find(pStringBusqueda, lsIndicesI[contador] + consLenPString) != -1:

                lsIndicesI.append(textoArchivo.find(pStringBusqueda, lsIndicesI[contador]) + consLenPString)
                lsIndicesF.append(textoArchivo.find("<", lsIndicesI[contador + 1]))
                

                
                contador += 1
            else:

                #se ejecuta cuando no hay mas precios
                break
    
        contador2 = 0
        texto = ""
        for a in lsIndicesI:
            
            texto = textoArchivo[a: lsIndicesF[contador2]]
            lsPrecios.append(limpiarTexto(texto))
            
            contador2 += 1
            
    
        return lsPrecios



    archivo.close()

def organizadorFechaPrecio(pNombreCiudad):
		#dado el nombre de una ciudad, abre el archivo con el nombre de esta y retorna un siccionario con los precios de los tiquetes de avion como llaves y las horas como tupla
		ListaTiempos = BuscadorTexto(pNombreCiudad, "class=\"time\"")
		contador = 0
		diccionarioPrecios = {}
		
		for a in BuscadorTexto(pNombreCiudad, "from-price"):
			
			if a in diccionarioPrecios.keys():
				a = str(contador) + a
			try:
				diccionarioPrecios[a] = [ListaTiempos[contador * 2], ListaTiempos[(contador*2) +1]]
				contador += 1

			except:
				
				print("ErrorI")
				break


		return diccionarioPrecios

def almacenarHorasPrecios(pDiccionarioHorasPrecios, pCiudad):
	#genera una archivo de tipo texto si no existe ya (en cuyo caso solo anade) con ewl nombre de la ciudad dada como parametro y no retorna nada

	#Se alamacena el valor dado en un documento especifico, no retorna nada
	msg = ""
	with open("Resultados" + pCiudad + ".txt", "a+") as archivo:

		msg = str(pDiccionarioHorasPrecios) +"\n"
		archivo.write(msg)
	
	
	


				
	
	
	






