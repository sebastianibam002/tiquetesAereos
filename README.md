# Tiquetes Aereos

#Ojetivos Cumplidos
a. Se diseñó una interfaz prototipo con los módulos tkinter y matplotlib
que permiten que se genere una ventana donde se grafica una función
dada. Este es el módulo llamado interfaz.py que mediante la libreria de Matplotlib y Tkinter logra graficar una funciòn dada.

b. Se escribió una función que dados unos datos como parámetros, los
almacena en un archivo de tipo texto para futuros análisis. Para esto se tiene Cliente.py, WebScrappingSelenium.py y CheckAvailability.py.

**Cliente.py**

Es una clase que permite almacenar datos especificos para cada usuario que lo necesite, es unico cada request que se hace a la pàgina porque tiene un nùmero serial para cada uno. Se puede decir que es el mòdulo principàl de donde se basa todo el programa, ya que conecta las funciones de WebScrpping con CheckAvailability.

**ChechAvailability.py**

Este revisa si los datos dados por el usuario son correctos, por ejemplo revisar si los dias colocados si estan bien como 32 > 31 que es el màximo nùmero de dias que se pueden tener. Esto para que cuando se conecte a la interfaz y se le pida un input al usuario este sepa que lo que introdujo es correcto.

**WebScrappingSelenium**

Es un mòdulo que permite mediante las librerias requests_html y Bs4 que se encargan de hacer que se ejecute el javascript de la pàgina web y obtiene el còdigo fuente (html) de la pàgina con los precios y horas de los vuelos.
