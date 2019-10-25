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
	
	soup = BeautifulSoup(resp.html.html, 'lxml')

	return soup.prettify()

	#Para que este codigo funcione hay que hacer un tema con el PATH de Firefox y tener instalado Selsnium
	#Lo que hace es buscar todas las etiquetas from-price

def AlmacenarTexto(pUrl, pNumeroCliente):
	#nombreTexto = "/home/sebastian/Documents/Soups/" + str(pNumeroCliente) + ".txt"
	nombreTexto = str(pNumeroCliente) + ".txt"

	with open(nombreTexto, "w") as texto:
		texto.write(webScrapping(pUrl))

def BuscadorTexto(pNumeroCliente, pStringBusqueda):
	#nombreTexto = "/home/sebastian/Documents/Soups/" + str(pNumeroCliente) + ".txt"
	nombreTexto = str(pNumeroCliente) + ".txt"

	with open(nombreTexto, "r") as texto:
		contadorLineas = 0
		listaLineas = []
		lineasTexto = []
		listaPrecios = []
		for line in texto:
			contadorLineas += 1
			lineasTexto.append(line)
			if pStringBusqueda in line:
				listaLineas.append(contadorLineas)
				
		#ahora voy a leer el texto patra poder acceder a los elemntetos de este como si fuera una lista de elementos
		
		#Esta parte esta hecha para quitarles los saltos de linea y los espacios de mas
		for elementos in listaLineas:
			ElementoLista = lineasTexto[elementos].lstrip()
			ElementoLista = ElementoLista.replace("\n", "")
			listaPrecios.append(ElementoLista)

		return listaPrecios

def organizadorFechaPrecio(pNumeroCliente):
		
		ListaTiempos = BuscadorTexto(pNumeroCliente, "<div class=\"time\"")
		contador = 0
		diccionarioPrecios = {}
		for a in BuscadorTexto(pNumeroCliente, "<div class=\"from-price\""):
			
			if a in diccionarioPrecios.keys():
				a = str(contador) + a

			diccionarioPrecios[a] = [ListaTiempos[contador], ListaTiempos[contador +1]]
			contador += 1
		return diccionarioPrecios

def almacenarHorasPrecios(pDiccionarioHorasPrecios):
	

	#Se alamacena el valor dado en un documento especifico, no retorna nada
	with open("textoTabulacion.txt", "a+") as archivo:
		archivo.write(str(pDiccionarioHorasPrecios))
	
	
	


				
	
	
	

"""
ZONA DE PRUEBAS	
AlmacenarTexto("https://www.vivaair.com/co/es/vuelo?DepartureCity=BOG&ArrivalCity=MDE&DepartureDate=2019-10-26&Adults=1&Currency=COP", 2)
#"<div class=\"from-price\""
BuscadorTexto(2, "<div class=\"time\"")
BuscadorTexto(2, "<div class=\"from-price\"")
"""

#organizadorFechaPrecio(2)
