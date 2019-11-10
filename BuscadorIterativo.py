import time
import Cliente

#Barranquilla, Cartagena, Bucaramanga, Cusco, San Andres Islas, Santa Marta, Valledup

ciudadesDestino = {"Barranquilla": [0,0], "Cartagena": [0,0], "Bucaramanga": [0,0], "Cusco": [0,0], "San Andres Islas": [0,0], "Santa Marta":[0,0], "Valledupar": [0,0]}


#ciudadesDestino = {"Barranquilla": [0,0]}
#las fechas que se quiere revisar

listaFechas = [10,11,12,13,14]

def repetirTresVeces(pFecha):

    
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
