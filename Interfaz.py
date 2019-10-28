
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
 
####################################### Ventana #############################################
""" Se crea la ventana con su respectivo titulo """

root = tk.Tk()
root.wm_title ("Analisis de vuelo")

####################### Grafico (averiguar el tipo de grafico) ##############################

fig = Figure (figsize = (5, 4), dpi=150)    # dimenciones de la figura ((ancho,alto), escala)---------#Tamaño
t = np.arange(0,3, 0.01)   #intervalo de 0 a 3 en el eje X, con pasos de 0.01  ---------------------- # Rango
fig.add_subplot(111).plot(t,2*np.sin(2*np.pi*t))  #-------------------------------------------------- #"Ecuación"
canvas = FigureCanvasTkAgg (fig, master = root )  #-------------------------------------------------- #Insertar en Ventana
canvas.draw() #---------------------------------------------------------------------------------------# Diduja el Grafico
canvas.get_tk_widget().pack(side= tk.TOP, fill=tk.BOTH, expand = 1) # Se expande de acuerdo al tamaño de la ventana----# Ubicación

############################# Barra herramientas(OPCIONAL)################################### 

toolbar = NavigationToolbar2Tk (canvas, root) #-------------------------------------------------------# Insertar en Ventana
toolbar.update()
canvas.get_tk_widget().pack(side= tk.TOP, fill=tk.BOTH, expand = 1) # Se expande de acuerdo al tamaño de la ventana-------# Ubicación

######################################## Botón ##############################################

"""Se define la funcion que cierra la ventana para luego vincularla a el botón 'Salir' """

def CerrarVentana():
    root.destroy ()
    exit()
boton = tk.Button(root, text = "Salir",command = CerrarVentana, bg = "red", fg = "white") # (texto, comando, color de fondo, color de letra)
boton.pack(side = tk.BOTTOM)   # Ubicación (parte inferior)

######################################### END ###############################################

tk.mainloop()
