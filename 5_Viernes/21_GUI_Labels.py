from tkinter import *

pant1= Tk()

frame1 = Frame(pant1,width=1200, height=600)
frame1.pack()

entryName=Entry(frame1)
entryName.grid(row=0, column=1,padx=10 , pady=10)
#CONFIGURAR AHORA EL APARTADO DE LA ENTRADA
entryName.config(fg="Red",justify="right")

LabelName = Label(frame1,text="Nombre: ")
LabelName.grid(row=0, column=0,sticky="e",padx=10 , pady=10)

entryApell=Entry(frame1)
entryApell.grid(row=1, column=1,padx=10 , pady=10) 
LabelApell = Label(frame1,text="Apellido: ")
LabelApell.grid(row=1, column=0, sticky="e",padx=10 , pady=10)

entryCasa=Entry(frame1)
entryCasa.grid(row=2, column=1,padx=10 , pady=10) 
LabelCasa = Label(frame1,text="Dirección (Casa): ")
LabelCasa.grid(row=2, column=0, sticky="e",padx=10 , pady=10)

entryPass=Entry(frame1)
entryPass.grid(row=3, column=1,padx=10 , pady=10) 
entryPass.config(show="*")
LabelPass = Label(frame1,text="Password: ")
LabelPass.grid(row=3, column=0, sticky="e",padx=10 , pady=10)

TextComen=Text(frame1,width= 16, height = 5)
TextComen.grid(row=4, column=1,padx=10 , pady=10) 


LabelComen = Label(frame1,text="Comentario: ")
LabelComen.grid(row=4, column=0, sticky="e",padx=10 , pady=10)
#MENCIONAR QUE ES UN SCROLLBAR

scroll=Scrollbar(frame1, command=TextComen.yview)#Por si sólo no sale
scroll.grid(row=4, column=2)
#PARA HACERSE AL TAMAÑO ,sticky="nsew"

#Pero se mueve sin tener nada
#TextComen.config(yscrollcommand=scroll.set)


pant1.mainloop()






