import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import TranformarPuntos 

########################################## Ventana ###########################################

""" Se crea la ventana con su respectivo titulo """

root = tk.Tk()
root.wm_title ("Analisis de vuelo")


################################# Grafico tipo scatter plot  #################################

figure = Figure(figsize=(5, 4), dpi=100) # Dimenciones de la figura ((ancho,alto), escala)
plot = figure.add_subplot(1, 1, 1) # Proporción

""" Datos del grafico"""
listaXBaq, listaYBaq = TranformarPuntos.main("ResultadosBAQ.txt")
listaXCuz, listaYCuz = TranformarPuntos.main("ResultadosCUZ.txt")
listaXCtg, listaYCtg = TranformarPuntos.main("ResultadosCTG.txt")
listaXBga, listaYBga = TranformarPuntos.main("ResultadosBGA.txt")
listaXAdz, listaYAdz = TranformarPuntos.main("ResultadosADZ.txt")
listaXSmr, listaYSmr = TranformarPuntos.main("ResultadosSMR.txt")
listaXVup, listaYVup = TranformarPuntos.main("ResultadosVUP.txt")

# Barranquilla

x1 = listaXBaq
y1 = listaYBaq

# Cusco
x2 = listaXCuz
y2 = listaYCuz

# Cartagena
x3 = listaXCtg
y3 = listaYCtg

# Bucaramanga
x4 = listaXBga
y4 = listaYBga

# San Andrés
x5 = listaXAdz
y5 = listaYAdz

# Santa Marta
x6 = listaXSmr
y6 = listaYSmr

# Valledupar
x7 = listaXVup
y7 = listaYVup

""" (Coordenadas X, Coordenadas Y, Color del punto, Marcador o tipo de punto, Etiqueta) """

Brranquilla = plot.scatter(x1, y1, color="blue", marker="X", label = "Brranquilla")
Cusco = plot.scatter(x2, y2, color="red", marker="D", label = "Cusco")
Cartagena = plot.scatter(x3, y3, color="green", marker="o", label = "Cartagena")
Bucaramanga = plot.scatter(x4, y4, color="orange", marker="s", label = "Bucaramanga")
SanAndres = plot.scatter(x5, y5, color="black", marker="p", label = "San Andrés")
SantaMarta = plot.scatter(x6, y6, color="yellow", marker="H", label = "Santa Marta")
Valledupar = plot.scatter(x7, y7, color="brown", marker="v", label = "Valledupar")

plot.legend() #leyenda del grafico

canvas = FigureCanvasTkAgg(figure, root) #Insertar en Ventana
canvas.get_tk_widget().pack()  #Ubicación

################################## Barra herramientas ####################################### 

toolbar = NavigationToolbar2Tk (canvas, root) # Insertar en Ventana
toolbar.update()
canvas.get_tk_widget().pack(side= tk.TOP, fill=tk.BOTH, expand = 1) # Se expande de acuerdo al tamaño de la ventana---# Ubicación

####################################### Cuadro ###############################################

#cuadro = tk.Frame (root,bg = "#CEF3F1")
#cuadro.pack(side= tk.TOP, fill=tk.BOTH, expand = 1)

####################################### Entradas #############################################
 
#def show_entry_fields():
#    print(" Nombre: %s\n Correo: %s\n Origen: %s\n Destino: %s\n Fecha: %s\n Numero de pasajeros: %s" % (entrada_nombre.get(), entrada_correo.get(), entrada_origen.get(), entrada_destino.get(), entrada_fecha.get(), entrada_pasajeros.get())) 
#    

#entrada_nombre = tk.Entry (cuadro)
#entrada_nombre.place(relx = 0.65, rely = 0.1, relwidth = 0.25, relheight = 0.12)
#
#entrada_correo = tk.Entry (cuadro)
#entrada_correo.place(relx = 0.65, rely = 0.25, relwidth = 0.25, relheight = 0.12)
#
#entrada_origen = tk.Entry (cuadro)
#entrada_origen.place(relx = 0.65, rely = 0.4, relwidth = 0.25, relheight = 0.12 )
#
#entrada_destino = tk.Entry (cuadro)
#entrada_destino.place(relx = 0.65, rely = 0.55, relwidth = 0.25, relheight = 0.12)
#
#entrada_fecha = tk.Entry (cuadro)
#entrada_fecha.place(relx = 0.65, rely = 0.7, relwidth = 0.25, relheight = 0.12)
#
#entrada_pasajeros = tk.Entry (cuadro)
#entrada_pasajeros.place(relx = 0.65, rely = 0.85, relwidth = 0.25, relheight = 0.12)
#
###################################### Etiquetas ##############################################
#
#label_nombre = tk.Label(cuadro, text = "Nombre", bg = "white")
#label_nombre.place(relx = 0.1, rely = 0.1, relwidth = 0.5, relheight = 0.12)
#
#label_correo = tk.Label(cuadro, text = "Correo Electronico", bg = "white")
#label_correo.place(relx = 0.1, rely = 0.25, relwidth = 0.5, relheight = 0.12)
#
#label_origen = tk.Label(cuadro, text = "Ciudad de Origen" , bg = "white")
#label_origen.place(relx = 0.1, rely = 0.4, relwidth = 0.5, relheight = 0.12)
#
#label_destino = tk.Label(cuadro, text = "Ciudad de Destino", bg = "white")
#label_destino.place(relx = 0.1, rely = 0.55, relwidth = 0.5, relheight = 0.12)
#
#label_fecha = tk.Label(cuadro, text = "Fecha (AAAA-MM-DD)", bg = "white")
#label_fecha.place(relx = 0.1, rely = 0.7, relwidth = 0.5, relheight = 0.12)
#
#label_pasajeros = tk.Label(cuadro, text = "Numero de Pasajeros", bg = "white")
#label_pasajeros.place(relx = 0.1, rely = 0.85, relwidth = 0.5, relheight = 0.12)


######################################## Botón ##############################################

"""Se define la funcion que cierra la ventana para luego vincularla a el botón 'Salir' """

def CerrarVentana():
    root.destroy ()
    exit()
    
boton_Salir = tk.Button(root, text = "Salir",command = CerrarVentana, bg = "red", fg = "white") # (Texto, Comando, Color de fondo, Color de letra)
boton_Salir.pack(side = tk.BOTTOM)   # Ubicación (Parte inferior)

######################################### END ###############################################
tk.mainloop()
