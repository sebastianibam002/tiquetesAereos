# Tiquetes Aereos

#Ojetivos Cumplidos
a. Se diseñó una interfaz prototipo con los módulos tkinter y matplotlib que permiten que se genere una ventana donde se grafica una función dada. Este es el módulo llamado interfaz.py que mediante la libreria de Matplotlib y Tkinter logra graficar dicha función.

b. Se escribió una función que, dados unos datos como parámetros, los almacena en un archivo de tipo texto para futuros análisis. Para esto se tiene Cliente.py, WebScrappingSelenium.py y CheckAvailability.py.

**Cliente.py**

Es una clase que permite almacenar datos especificos para cada usuario que lo necesite, cada request que se hace a la pàgina es único, ya que se tiene un número serial para cada uno. Se puede decir que es el módulo principal, de donde se basa todo el programa, ya que conecta las funciones de WebScrpping con CheckAvailability.

**ChechAvailability.py**

Este revisa si los datos dados por el usuario son correctos, por ejemplo, revisar si los días colocados sí estan bien, como 32 > 31 que es el máximo número de días que se pueden tener. Esto se hace para que, al conectarse a la interfaz y se pida un input al usuario este sepa que lo que introdujo es correcto y viable.

**WebScrappingSelenium**

Es un módulo que permite, mediante las librerias requests_html y time, que se encargan de hacer que se ejecute el javascript de la página web y obtiene el código fuente (html) de la página con los precios y horas de los vuelos.
