import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
 
####################################### Ventana #############################################

root = tk.Tk()
root.wm_title ("Analisis de vuelo")


####################### Grafico (averiguar el tipo de grafico) ##############################

fig = Figure (figsize = (5, 4), dpi=150)                                        #Tamaño
t = np.arange(0,3, 0.01)                                                        # Rango
fig.add_subplot(111).plot(t,2*np.sin(2*np.pi*t))                                # "Ecuación"
canvas = FigureCanvasTkAgg (fig, master = root )                                # Insertar en Ventana
canvas.draw()                                                                   # Diduja el Grafico
canvas.get_tk_widget().pack(side= tk.TOP, fill=tk.BOTH, expand = 1)             # Ubicación

############################# Barra herramientas(OPCIONAL)################################### 

toolbar = NavigationToolbar2Tk (canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side= tk.TOP, fill=tk.BOTH, expand = 1)

######################################## Boton ##############################################

def cerrarVentana():
    root.destroy ()
    exit()
boton = tk.Button(root, text = "Salir",command=cerrarVentana, bg = "red", fg = "white" )
boton.pack(side = tk.BOTTOM)

######################################### END ###############################################

tk.mainloop()
