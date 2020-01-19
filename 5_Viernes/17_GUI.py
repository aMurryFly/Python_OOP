"""Biblioteca Tkinter
GUI -> graphical user interface

Otras bibliotecas:
    WxPython
    PyQT -> Tutorial guapo <3
    PyGTK
"""

from tkinter import *

raiz= Tk()#Preguntarles 7u7r
raiz.title("Hola Mundo")

raiz.resizable(True,False)#Ancho - width y largo - height
#Iconos -> formato .ico

raiz.iconbitmap("favicon.ico")
raiz.geometry("650x315")
raiz.config(bg="Blue")

raiz.mainloop()
#Es un bucle para el refresco de la venta 
#y creación de la ventana principal

#COMENTAR LO DE pyw -> window 
#Hacer la explicación respecto a la ventana y consola 







