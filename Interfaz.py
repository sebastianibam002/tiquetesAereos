import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
#########################################
#import checkAvailability
#import WebScrappingSelenium
#import Cliente
####################


    
####################################### Ventana #############################################

""" Se crea la ventana con su respectivo titulo """


root = tk.Tk()
root.wm_title ("Analisis de vuelo")

####################### Grafico (averiguar el tipo de grafico) ##############################

fig = Figure (figsize = (5, 4), dpi=140)    # dimenciones de la figura ((ancho,alto), escala)---------#Tamaño
t = np.arange(0,3, 0.01)   #intervalo de 0 a 3 en el eje X, con pasos de 0.01  ---------------------- # Rango
fig.add_subplot(111).plot(t,2*np.sin(2*np.pi*t))  #-------------------------------------------------- #"Ecuación"
canvas = FigureCanvasTkAgg (fig, master = root )  #-------------------------------------------------- #Insertar en Ventana
canvas.draw() #---------------------------------------------------------------------------------------# Diduja el Grafico
canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand = 1) # Se expande de acuerdo al tamaño de la ventana----# Ubicación

############################# Barra herramientas(OPCIONAL)################################### 

toolbar = NavigationToolbar2Tk (canvas, root) #-------------------------------------------------------# Insertar en Ventana
toolbar.update()
canvas.get_tk_widget().pack(side= tk.TOP, fill=tk.BOTH, expand = 1) # Se expande de acuerdo al tamaño de la ventana-------# Ubicación

####################################### Cuadro ###############################################

cuadro = tk.Frame (root,bg = "#33d7ff")
cuadro.pack(side= tk.TOP, fill=tk.BOTH, expand = 1)

####################################### Entradas #############################################
 
#def show_entry_fields():
#    print(" Nombre: %s\n Correo: %s\n Origen: %s\n Destino: %s\n Fecha: %s\n Numero de pasajeros: %s" % (entrada_nombre.get(), entrada_correo.get(), entrada_origen.get(), entrada_destino.get(), entrada_fecha.get(), entrada_pasajeros.get())) 
#    

entrada_nombre = tk.Entry (cuadro)
entrada_nombre.place(relx = 0.65, rely = 0.1, relwidth = 0.25, relheight = 0.12)

entrada_correo = tk.Entry (cuadro)
entrada_correo.place(relx = 0.65, rely = 0.25, relwidth = 0.25, relheight = 0.12)

entrada_origen = tk.Entry (cuadro)
entrada_origen.place(relx = 0.65, rely = 0.4, relwidth = 0.25, relheight = 0.12 )

entrada_destino = tk.Entry (cuadro)
entrada_destino.place(relx = 0.65, rely = 0.55, relwidth = 0.25, relheight = 0.12)

entrada_fecha = tk.Entry (cuadro)
entrada_fecha.place(relx = 0.65, rely = 0.7, relwidth = 0.25, relheight = 0.12)

entrada_pasajeros = tk.Entry (cuadro)
entrada_pasajeros.place(relx = 0.65, rely = 0.85, relwidth = 0.25, relheight = 0.12)

##################################### Etiquetas ##############################################

label_nombre = tk.Label(cuadro, text = "Nombre")
label_nombre.place(relx = 0.1, rely = 0.1, relwidth = 0.5, relheight = 0.12)

label_correo = tk.Label(cuadro, text = "Correo Electronico")
label_correo.place(relx = 0.1, rely = 0.25, relwidth = 0.5, relheight = 0.12)

label_origen = tk.Label(cuadro, text = "Ciudad de Origen" )
label_origen.place(relx = 0.1, rely = 0.4, relwidth = 0.5, relheight = 0.12)

label_destino = tk.Label(cuadro, text = "Ciudad de Destino")
label_destino.place(relx = 0.1, rely = 0.55, relwidth = 0.5, relheight = 0.12)

label_fecha = tk.Label(cuadro, text = "Fecha (AAAA-MM-DD)")
label_fecha.place(relx = 0.1, rely = 0.7, relwidth = 0.5, relheight = 0.12)

label_pasajeros = tk.Label(cuadro, text = "Numero de Pasajeros")
label_pasajeros.place(relx = 0.1, rely = 0.85, relwidth = 0.5, relheight = 0.12)


######################################## Botones ##############################################

"""Se define la funcion que cierra la ventana para luego vincularla a el botón 'Salir' """

def CerrarVentana():
    root.destroy ()
    exit()
boton_Salir = tk.Button(root, text = "Salir",command = CerrarVentana, bg = "red", fg = "white") # (texto, comando, color de fondo, color de letra)
boton_Salir.pack(side = tk.BOTTOM)   # Ubicación (parte inferior)

"""Se define la funcion que le permite al usuario poder solocitar un vuelo, con los datos necesarios para este: ciudad de salida, ciudad de destino, la fecha en que se sale (con el siguiente formato 'ano-mes-dia') y el numero de pasajeros """
def listo():
    pass
    

boton_Aceptar = tk.Button(root, text = "Aceptar",command = listo , bg = "blue", fg = "white") # (texto, comando, color de fondo, color de letra)
boton_Aceptar.pack(side = tk.BOTTOM)   # Ubicación (parte inferior)

######################################### END ###############################################
tk.mainloop()
