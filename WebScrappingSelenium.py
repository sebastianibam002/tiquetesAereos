#from selenium import webdriver
from bs4 import BeautifulSoup
from requests_html import HTMLSession




def webScrapping (pUrl):
	"""

	TODO: cambiar la libreeria Selenium por requets_tml ya la descarhgue con pip

	

	url = pUrl
	# create a new Firefox session
	driver = webdriver.Firefox(executable_path="/home/sebastian/Downloads/gecko/geckodriver", log_path="/home/sebastian/Downloads/gecko/geckodriver.log")
	driver.implicitly_wait(30)
	driver.get(url)

	#python_button = driver.find_element_by_id('day selected') #FHSU
	#python_button.click()

	soup= BeautifulSoup(driver.page_source, 'lxml')

	js = soup.find("div", class_="from-price")
	
	
	return soup.prettify()

	"""
	session = HTMLSession()
	resp = session.get(pUrl)
	resp.html.render()
	
	#soup = BeautifulSoup(resp.html.html, 'lxml')
	
	return resp.html.html

	#Para que este codigo funcione hay que hacer un tema con el PATH de Firefox y tener instalado Selsnium
	#Lo que hace es buscar todas las etiquetas from-price

def AlmacenarTexto(pUrl, pNumeroCliente):
	#nombreTexto = "/home/sebastian/Documents/Soups/" + str(pNumeroCliente) + ".txt"
	nombreTexto = str(pNumeroCliente) + ".txt"

	with open(nombreTexto, "w") as texto:
		texto.write(webScrapping(pUrl))


def limpiarTexto(pString):


    pString= pString.replace("\n", "")
    pString = pString.replace(">", "")
    pString = pString.replace("          ", "")
    pString = pString.replace(" ", "")
    return pString


def BuscadorTexto(pNumeroCliente, pStringBusqueda):
   

    archivo  = open (str(pNumeroCliente) + ".txt", "r")
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
                

                #lsPrecios.append(textoArchivo[lsIndicesI[contador] + 2: lsIndicesF[contador]])
                contador += 1
            else:

                #se ejecuta cuando no hay mas precios
                break
    
        contador2 = 0
        texto = ""
        for a in lsIndicesI:
            
            texto = textoArchivo[a: lsIndicesF[contador2]]
            lsPrecios.append(limpiarTexto(texto))
            #lsPrecios.append(textoArchivo[a: lsIndicesF[contador2]])
            contador2 += 1
            
    
        return lsPrecios



    archivo.close()

def organizadorFechaPrecio(pNumeroCliente):
		
		ListaTiempos = BuscadorTexto(pNumeroCliente, "class=\"time\"")
		contador = 0
		diccionarioPrecios = {}
		
		for a in BuscadorTexto(pNumeroCliente, "from-price"):
			
			if a in diccionarioPrecios.keys():
				a = str(contador) + a
			try:
				diccionarioPrecios[a] = [ListaTiempos[contador * 2], ListaTiempos[(contador*2) +1]]
				contador += 1

			except:
				
				print("Error la pagina no cargo de forma correcta")
				break


		return diccionarioPrecios

def almacenarHorasPrecios(pDiccionarioHorasPrecios):
	

	#Se alamacena el valor dado en un documento especifico, no retorna nada
	msg = ""
	with open("textoTabulacion.txt", "a+") as archivo:

		msg = str(pDiccionarioHorasPrecios) + "\n ********************************************** \n"
		archivo.write(msg)
	
	
	


				
	
	
	

"""
ZONA DE PRUEBAS	
AlmacenarTexto("https://www.vivaair.com/co/es/vuelo?DepartureCity=BOG&ArrivalCity=MDE&DepartureDate=2019-10-26&Adults=1&Currency=COP", 2)
#"<div class=\"from-price\""
BuscadorTexto(2, "<div class=\"time\"")

"""

#print(organizadorFechaPrecio(25))



