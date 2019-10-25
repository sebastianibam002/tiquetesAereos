#archivo principal que contiene todo

import checkAvailability
import WebScrappingSelenium


#voy a crear una clase con el usuario que quiere obtener esta informacion y que se alamacene en su propio archivo para ser un poco mas organizado

class Cliente():
	def __init__(self, pNombre, pCorreo , numeroSerial= 0):
		#Se le colocan los atributos de una persona, el correo es un adicional para despues
		self.nombre = pNombre
		self.correo = pCorreo
		self.numeroSerial = self.generadorNumeroSerial(numeroSerial)
	def generadorNumeroSerial(self, pNumeroSerial):
		#se abre el archivo de texto con todos los numeros seriales
	
		with open("NumerosSeriales.txt", "+r") as Archivo:
			for a in Archivo:
				#Luego de leer todo el archivo procede a ver el ultimo numero, luego a ese valor le suma uno y en la proxima funcion se lo anade
				if pNumeroSerial <= int(a):
					pNumeroSerial = int(a)+1

			Archivo.close()
			r = open("NumerosSeriales.txt", "a")
			r.write(str(pNumeroSerial)+ "\n")
			r.close()
			
		return pNumeroSerial

	def __str__(self):
		#Este metodo permite ver cual fue el nombre, el correo y el numero serial del cliente uitlizando el software
		return "Hola mi nombre es {0}, mi correo es {1} y mi numero serial {2}".format(self.nombre, self.correo, self.numeroSerial)

	def solicitarVuelo(self, pCiudadSalida, pCiudadDestino, pFechaSalida, pNumeroDePersonas):
		#Le permite al usuario poder solocitar un vuelo, con los datos necesarios para este: ciudad de salida, ciudad de destino, la fecha en que se sale (con el siguiente formato 'ano-mes-dia') y el numero de pasajeros
		url = checkAvailability.modificacionLink(pCiudadSalida, pCiudadDestino, pFechaSalida, pNumeroDePersonas)
		if url != None:
			WebScrappingSelenium.AlmacenarTexto(url, self.numeroSerial)
			print("El vuelo ya se almaceno")
			#si es diferente a nada que se le indique al usuario que hay vuelos disponibles en el sitio o fechas escogidos
			if WebScrappingSelenium.organizadorFechaPrecio(self.numeroSerial) != []:
				diccionarioPrecios = {}
				diccionarioPrecios = WebScrappingSelenium.organizadorFechaPrecio(self.numeroSerial)
				print(diccionarioPrecios)
				WebScrappingSelenium.almacenarHorasPrecios(diccionarioPrecios)
			else:
				print("No hay vuelos disponibles en esas fechas en estos sitios")

			
		else:
			print("Ocurrio un error con el link")
			
	
		
		
		




#Beginning-ofExecution
ciudadOrigen = ""
ciudadDestino = ""

#Parte para hacer pruebas con valores introducidos directamente en la consola
nombreCliente = input("Introduzca su nombre: ")
correoCliente = input("Inntroduzca su correo: ")
fechaDeSalida = input("Introduzca la fecha de salida ej:2019-10-25: ")
numeroDePasajeros = int(input("Numero de Pasajeros: "))
ciudadDeOrigen = input("Ciudad de Origen: ")
ciudadDestino = input("Ciudad Destino: ")

cliente1 = Cliente(nombreCliente, correoCliente)
cliente1.solicitarVuelo(ciudadDeOrigen, ciudadDestino,fechaDeSalida, numeroDePasajeros )
	
