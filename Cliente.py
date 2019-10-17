#archivo principal que contiene todo

import checkAvailability
import WebScrappingSelenium


#voy a crear una clase con el usuario que quiere obtener esta informacion y que se alamacene en su propio archivo para ser un poco mas organizado

class Cliente():
	def __init__(self, pNombre, pCorreo , numeroSerial= 0):
		self.nombre = pNombre
		self.correo = pCorreo
		self.numeroSerial = self.generadorNumeroSerial(numeroSerial)
	def generadorNumeroSerial(self, pNumeroSerial):
		#se abre el archivo de texto con todos los numeros seriales
		with open("NumerosSeriales.txt", "a+") as Archivo:
			for a in Archivo:
				if pNumeroSerial <= int(a):
					pNumeroSerial = int(a)+1
			Archivo.write(str(pNumeroSerial)+ "\n")
		return pNumeroSerial

	def __str__(self):
		return "Hola mi nombre es {0}, mi correo es {1} y mi numero serial {2}".format(self.nombre, self.correo, self.numeroSerial)

	def solicitarVuelo(self, pCiudadSalida, pCiudadDestino, pFechaSalida, pNumeroDePersonas):
		url = checkAvailability.modificacionLink(pCiudadSalida, pCiudadDestino, pFechaSalida, pNumeroDePersonas)
		if url != None:
			WebScrappingSelenium.AlmacenarTexto(url, self.numeroSerial)
			print("El vuelo ya se almaceno")
			print(WebScrappingSelenium.organizadorFechaPrecio(self.numeroSerial))
			
		else:
			print("Ocurrio un error con el link")
			
	
		
		
		




#Beginning-ofExecution
ciudadOrigen = ""
ciudadDestino = ""

fechaDeSalida = raw_input("Introduzca la fecha de salida ej:2019-10-25: ")
numeroDePasajeros = int(input("Numero de Pasajeros: "))
ciudadDeOrigen = raw_input("Ciudad de Origen: ")
ciudadDestino = raw_input("Ciudad Destino: ")

cliente1 = Cliente("juan", "correo")
cliente1.solicitarVuelo(ciudadDeOrigen, ciudadDestino,fechaDeSalida, numeroDePasajeros )
	
