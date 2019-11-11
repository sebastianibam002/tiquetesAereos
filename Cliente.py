#archivo principal que contiene todo

import checkAvailability
import WebScrappingSelenium


# Se crea una clase con el usuario que quiere obtener esta informacion y que se alamacene en su propio archivo para ser un poco mas organizado

class Ciudad():
    def __init__(self,pCiudad, numeroSerial= 0):
	#Se le colocan los atributos de una persona, el correo es un adicional para después
        self.nombre = pCiudad #su propio nombre
        self.prefijo = checkAvailability.generarPrefijo(pCiudad)

        self.numeroSerial = self.generadorNumeroSerial(numeroSerial)


    def generadorNumeroSerial(self, pNumeroSerial):

        #se abre el archivo de texto con todos los numeros seriales
	
        try:

            with open(self.prefijo + "NumSerial.txt", "r") as Archivo:
                for a in Archivo:
                    #Luego de leer todo el archivo procede a ver el ultimo numero, luego a ese valor le suma uno y en la proxima funcion se lo anade
					
                    a = a[self.prefijo.__len__(): self.prefijo.__len__() + 1 ]

                    if pNumeroSerial <= int(a):
                        pNumeroSerial = int(a)+1
        except:
	    #En caso de que no exista se crea uno
            name = self.prefijo + "NumSerial.txt"
            print(name)
            Archivo = open(name, "w")
            Archivo.close()
			
			
        r = open(self.prefijo + "NumSerial.txt", "a")
        r.write(self.prefijo + str(pNumeroSerial)+ "\n")
        r.close()
			
        return pNumeroSerial

    def __str__(self):
	#Este metodo permite ver cual fue el nombre, el correo y el numero serial del cliente uitlizando el software
        return "mi numero serial {0}".format (self.numeroSerial)

    def solicitarVuelo(self, pFechaSalida):
    #Le permite al usuario poder solocitar un vuelo, con los datos necesarios para este: ciudad de salida, ciudad de destino, la fecha en que se sale (con el siguiente formato 'AAAA-MM-DD') y el numero de pasajeros
        url = checkAvailability.modificacionLink("Bogota", self.nombre , pFechaSalida, 1)
        

        if url != None:
            WebScrappingSelenium.AlmacenarTexto(url, (self.prefijo + str(self.numeroSerial)))
            #print("El vuelo ya se almaceno")
	    #si es diferente a nada que se le indique al usuario que hay vuelos disponibles en el sitio o fechas escogidos
            if WebScrappingSelenium.organizadorFechaPrecio(self.prefijo + str(self.numeroSerial)) != []:
                diccionarioPrecios = {}
                diccionarioPrecios = WebScrappingSelenium.organizadorFechaPrecio(self.prefijo + str(self.numeroSerial))
                #print(diccionarioPrecios)
                WebScrappingSelenium.almacenarHorasPrecios(diccionarioPrecios, self.prefijo)

                if diccionarioPrecios == {}:

                    return False

                else:

                    return True
            else:
                print("No hay vuelos disponibles en esas fechas en estas ciudades")

			
            
        else:
            print("Ocurrio un error con el link")

	
			
	
        

        
 
#cliente1 = Ciudad("Barranquilla")
#cliente1.solicitarVuelo("2019-11-12")
#cliente1.soliciarVuelo(ciudadDeOrigen, ciudadDestino,fechaDeSalida, numeroDePasajeros )
