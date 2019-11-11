import time
from requests_html import HTMLSession


def webScrapping (pUrl): # Requiere como parametro un url y retorna el codigo html de este url

	try:
		session = HTMLSession()
		resp = session.get(pUrl)
		resp.html.render()
		return resp.html.html
	except:
		print("Revisar Conexion")


def AlmacenarTexto(pUrl, pNombreCiudad): # Crea un archivo de texto ".txt" con el nombre de la ciudad y guarda el codigo html
	
	nombreTexto = pNombreCiudad + ".txt"

	with open(nombreTexto, "w") as texto:
		texto.write(webScrapping(pUrl))


def limpiarTexto(pString):   # Elimina los caracteres innecesarios


    pString= pString.replace("\n", "")
    pString = pString.replace(">", "")
    pString = pString.replace("          ", "")
    pString = pString.replace(" ", "")
    return pString


def BuscadorTexto(pNombreCiudad, pStringBusqueda):
   
# Abre el archibo de texto con el nombre de la ciudad para realizar la busqueda

    archivo  = open (str(pNombreCiudad) + ".txt", "r")
    textoArchivo = archivo.read()
    lsIndicesI = []
    lsIndicesF = []
    lsPrecios = []
    contador = 0
    
    encontrado = True


    if pStringBusqueda == "from-price":  # la palabra "from-price" es la inmediatamente anterior a el precio, por eso es el parametro de busqueda
        
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

                # Se ejecuta cuando no hay mas precios
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

                # Se ejecuta cuando no hay mas precios
                break
    
        contador2 = 0
        texto = ""
        for a in lsIndicesI:
            
            texto = textoArchivo[a: lsIndicesF[contador2]]
            lsPrecios.append(limpiarTexto(texto))
            
            contador2 += 1
            
    
        return lsPrecios


    archivo.close()

def organizadorFechaPrecio(pNombreCiudad): # abre el archivo con el nombre de la ciudad y crea un diccionario con los precios como llaves y las horas como valor en una lista (hora de salida y hora de llegada)
		
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

	# Se alamacena el valor dado en un documento especifico, no retorna nada
	msg = ""
	with open("Resultados" + pCiudad + ".txt", "a+") as archivo:

		msg = str(pDiccionarioHorasPrecios) +"\n"
		archivo.write(msg)
	
	
