from bs4 import BeautifulSoup
import urllib.request
import requests
import re

posiblesCiudades = {"Arequipa": "AQP", "Barranquilla": "BAQ", "Bogotá": "BOG", "Bucaramanga": "BGA",  "Cajamarca": "CJA", "Cartagena": "CTG", "Chiclayo": "CIX", "Cusco": "CUZ", "Cúcuta" : "CUC,", "Iquitos": "IQT", "Jaén": "JAE", "Juliaca": "JUL", "Lima": "LIM", "Medellín": "MDE", "Miami": "MIA", "Montería": "MTR", "Pereira": "PEI", "Piura": "PIU", "Rioacha": "RCH", "San Andrés Islas": "ADZ", "Santa Marta": "SMR", "Tacna": "TCQ", "Talara": "TYl", "Tarapoto": "TPP", "Valledupar": "VUP"}


def buscarEnCiudad(pCiudad):

    encontrado = False

    for a in posiblesCiudades.keys():

        if a == ciudadDeOrigen:
            encontrado = True



    return encontrado

def abriendoPagina():

    url = "https://www.vivaair.com/co/es/vuelo?DepartureCity=BOG&ArrivalCity=SMR&DepartureDate=2019-11-25&Adults=2&Currency=COP"
    """
    if buscarEnCiudad(ciudadDeOrigen) and buscarEnCiudad(ciudadDestino):

        try:
            #url = "https://www.vivaair.com/co/es/vuelo?DepartureCity=" +posiblesCiudades[ciudadDeOrigen] +"&ArrivalCity="+posiblesCiudades[ciudadDestino]+"&DepartureDate=" + fechaDeSalida+ "&Adults=" + str(numeroDePasajeros) +"&Currency=COP"

            response = requests.get(url)
            print(response)
        except:

            print("Error en el url")

    """
    #se abre la pagina
    pagina = urllib.request.urlopen(url)
    #Ahora ya se tiene la pagina como un texto
    soup = BeautifulSoup(pagina, 'html.parser')

    print(soup.find_all(attrs={"COP 165,000": "from-price"}))




#PseudoInterfaz gráfica
"""
fechaDeSalida = input("Introduzca la fecha de salida ej:2019-10-25: ")
numeroDePasajeros = int(input("Numero de Pasajeros: "))
ciudadDeOrigen = input("Ciudad de Origen: ")
ciudadDestino = input("Ciudad Destino: ")
"""





abriendoPagina()

