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

#Mencionar que hay contenedores padres -> el frame 1 - Pading

pant1.mainloop()






