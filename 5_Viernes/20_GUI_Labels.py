from tkinter import *

pant1= Tk()

frame1 = Frame(pant1,width=1200, height=600)
frame1.pack()
'''
entry1=Entry(frame1)
entry1.place(x=100,y=100)

LabelName = Label(frame1,text="Nombre: ")
LabelName.place(x=120,y=100)

'''
#MENCIONAR COMO ALINEAR CORRECTAMENTE 
entryName=Entry(frame1)
entryName.grid(row=0, column=1) # row - fila column - columna

LabelName = Label(frame1,text="Nombre: ")
LabelName.grid(row=0, column=0)

entryApell=Entry(frame1)
entryApell.grid(row=1, column=1) # row - fila column - columna

LabelApell = Label(frame1,text="Apellido: ")
#text="Apellido: ") -> Alineado al centro
LabelApell.grid(row=1, column=0, sticky="e")
#Sticky -> está en cordenadas en inglés
#PEDIRLE QUE HAGAN MÁS ->

#DOCUMENTACIÓN
#https://docs.python.org/3/library/tk.html
#https://docs.python.org/3/library/tkinter.html#tkinter-modules


pant1.mainloop()




