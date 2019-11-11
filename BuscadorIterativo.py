import time
import Cliente

""" Se establecieron las siguientes ciudades como muestra: Barranquilla, Cartagena, Bucaramanga, Cusco, San Andres Islas, Santa Marta, Valledupar"""

ciudadesDestino = {"Barranquilla": [0,0], "Cartagena": [0,0], "Bucaramanga": [0,0], "Cusco": [0,0], "San Andres Islas": [0,0], "Santa Marta":[0,0], "Valledupar": [0,0]}


#ciudadesDestino = {"Barranquilla": [0,0]}
#las fechas que se quiere revisar

"""
print("Introduzca las fechas donde quiere hacer la investigacion, separados por -: ")
inputUsuario = input("")
listaFechas = inputUsuario.split("-")
for a in listaFechas:
    listaFechas.append(int(a))

print(listaFechas)
    
"""    
listaFechas = [11,12,13,14]  # 11,12,13 y 14 de noviembre de 2019

def repetirTresVeces(pFecha):  # se solicita un vuelo cada minuto en una fecha especifica

    
    for a in ciudadesDestino.keys():

        fecha = 0
        nombreCiudad = ""

        nombreCiudad = a + "Ciudad"

        while ciudadesDestino[a][0] < 3:
            nombreCiudad = Cliente.Ciudad(a)
            if nombreCiudad.solicitarVuelo("2019-11-" + str(pFecha)):
                print("Listo", ciudadesDestino[a][0])

            fecha += 1

            ciudadesDestino[a][0] = fecha 
            time.sleep(60)
     

            #El primer elemento de la lista corresponde a los tres intentos con la misma fecha

def modificarFecha():

    
    for a in listaFechas:

        repetirTresVeces(a)
        for a in ciudadesDestino.keys():
            ciudadesDestino[a][1] += 1
            ciudadesDestino[a][0] = 0

        time.sleep(180)
        print(ciudadesDestino)



modificarFecha()
